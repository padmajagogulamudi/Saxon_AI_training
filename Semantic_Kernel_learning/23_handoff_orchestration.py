import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from semantic_kernel.agents import (
    ChatCompletionAgent,
    HandoffOrchestration,
    OrchestrationHandoffs,
)
from semantic_kernel.agents.runtime import InProcessRuntime
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import AuthorRole, ChatMessageContent


load_dotenv(Path(__file__).resolve().parent / ".env")


def agent_response_callback(message: ChatMessageContent) -> None:
    print(f"\n{message.name}: {message.content}")


def human_response_function() -> ChatMessageContent:
    user_input = input("\nYou: ")
    return ChatMessageContent(
        role=AuthorRole.USER,
        content=user_input,
    )


async def main():
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION")

    if not all([endpoint, api_key, deployment, api_version]):
        raise ValueError("Check your Azure OpenAI settings in .env")

    service = AzureChatCompletion(
        deployment_name=deployment,
        endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
    )

    support_agent = ChatCompletionAgent(
        service=service,
        name="SupportAgent",
        description="Handles general customer support and routes requests.",
        instructions=(
            "You are the first point of contact for customer support. "
            "Identify whether the customer needs order-status or billing "
            "assistance. Hand off to the appropriate specialist. "
            "If the customer says they have no more questions, summarize "
            "the conversation and finish."
        ),
    )

    order_agent = ChatCompletionAgent(
        service=service,
        name="OrderAgent",
        description="Handles order-status questions.",
        instructions=(
            "You specialize in order-status questions. Ask for an order ID "
            "if needed. This is a demonstration, not a real order system, "
            "so never claim to have checked an actual order. "
            "Hand off to SupportAgent if the request is outside your role. "
            "If the customer has no more questions, hand off to SupportAgent."
        ),
    )

    billing_agent = ChatCompletionAgent(
        service=service,
        name="BillingAgent",
        description="Handles billing and payment questions.",
        instructions=(
            "You specialize in billing and payment questions. "
            "Ask for clarification when necessary. This is a demonstration, "
            "not a real payment system. Never claim to have processed a "
            "payment or refund. Hand off to SupportAgent if the request "
            "is outside your role or the customer has no more questions."
        ),
    )

    handoffs = (
        OrchestrationHandoffs()
        .add_many(
            source_agent=support_agent.name,
            target_agents={
                order_agent.name: "Transfer order-status questions here.",
                billing_agent.name: "Transfer billing or payment questions here.",
            },
        )
        .add(
            source_agent=order_agent.name,
            target_agent=support_agent.name,
            description="Transfer back when the order question is resolved or unrelated.",
        )
        .add(
            source_agent=billing_agent.name,
            target_agent=support_agent.name,
            description="Transfer back when the billing question is resolved or unrelated.",
        )
    )

    orchestration = HandoffOrchestration(
        members=[support_agent, order_agent, billing_agent],
        handoffs=handoffs,
        agent_response_callback=agent_response_callback,
        human_response_function=human_response_function,
    )

    runtime = InProcessRuntime()
    runtime.start()

    try:
        result = await orchestration.invoke(
            task="I need help checking my order status.",
            runtime=runtime,
        )

        final_output = await result.get(timeout=300)

        print("\n========== FINAL RESULT ==========")
        print(final_output)

    finally:
        await runtime.stop_when_idle()


if __name__ == "__main__":
    asyncio.run(main())