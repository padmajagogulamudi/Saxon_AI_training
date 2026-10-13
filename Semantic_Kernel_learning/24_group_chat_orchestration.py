import asyncio
import os
from pathlib import Path

from dotenv import load_dotenv
from semantic_kernel.agents import (
    ChatCompletionAgent,
    GroupChatOrchestration,
    RoundRobinGroupChatManager,
)
from semantic_kernel.agents.runtime import InProcessRuntime
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.contents import ChatMessageContent


load_dotenv(Path(__file__).resolve().parent / ".env")


def agent_response_callback(message: ChatMessageContent) -> None:
    print(f"\n--- {message.name} ---")
    print(message.content)


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

    idea_agent = ChatCompletionAgent(
        service=service,
        name="IdeaAgent",
        description="Suggests practical AI internship project ideas.",
        instructions=(
            "You are an AI project ideation specialist. Propose a practical "
            "mini-project suitable for an AI internship. Explain the problem, "
            "target users, and key features. Keep your response concise."
        ),
    )

    technical_agent = ChatCompletionAgent(
        service=service,
        name="TechnicalAgent",
        description="Evaluates technical feasibility and project architecture.",
        instructions=(
            "You are an AI engineer. Review the previous proposal and discuss "
            "technical feasibility, architecture, and suitable technologies. "
            "Build on the existing discussion rather than starting over."
        ),
    )

    reviewer_agent = ChatCompletionAgent(
        service=service,
        name="ReviewerAgent",
        description="Reviews and improves the final project proposal.",
        instructions=(
            "You are a project reviewer. Evaluate the discussion, identify "
            "improvements, and produce a concise project recommendation with "
            "features and a suggested technology stack."
        ),
    )

    orchestration = GroupChatOrchestration(
        members=[idea_agent, technical_agent, reviewer_agent],
        manager=RoundRobinGroupChatManager(max_rounds=3),
        agent_response_callback=agent_response_callback,
    )

    runtime = InProcessRuntime()
    runtime.start()

    try:
        result = await orchestration.invoke(
            task=(
                "Suggest and plan a mini-project that will help two interns "
                "stand out during an AI internship. We have studied Python, "
                "FastAPI, RAG, and Semantic Kernel. Keep the scope realistic."
            ),
            runtime=runtime,
        )

        final_output = await result.get(timeout=180)

        print("\n========== FINAL RESULT ==========")
        print(final_output)

    finally:
        await runtime.stop_when_idle()


if __name__ == "__main__":
    asyncio.run(main())