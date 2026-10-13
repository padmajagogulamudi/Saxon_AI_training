import asyncio
import os

from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.functions import KernelArguments
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.prompt_template import (
    PromptTemplateConfig,
    HandlebarsPromptTemplate,
    InputVariable
)


async def main():
    load_dotenv()

    kernel = Kernel()

    kernel.add_service(
        AzureChatCompletion(
           deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
               endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
               api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
    )

    prompt = """
    <message role="system">
    You are a helpful AI assistant.
    The user's name is {{customer.first_name}}.
    Answer questions clearly and simply.
    </message>

    {{#each history}}
    <message role="{{role}}">
    {{content}}
    </message>
    {{/each}}
    """

    config = PromptTemplateConfig(
        name="HandlebarsChat",
        template=prompt,
        template_format="handlebars",
        input_variables=[
            InputVariable(
                name="customer",
                allow_dangerously_set_content=True
            ),
            InputVariable(
                name="history",
                allow_dangerously_set_content=True
            )
        ]
    )

    template = HandlebarsPromptTemplate(
        prompt_template_config=config,
        allow_dangerously_set_content=True
    )

    customer = {
        "first_name": "Padmaja"
    }

    history = [
        {
            "role": "user",
            "content": "What is Semantic Kernel?"
        }
    ]

    arguments = KernelArguments(
        customer=customer,
        history=history
    )

    rendered_prompt = await template.render(
        kernel,
        arguments
    )

    print("Rendered Prompt:")
    print(rendered_prompt)

    chat_function = kernel.add_function(
        function_name="HandlebarsChat",
        plugin_name="ChatPlugin",
        prompt_template_config=config
    )

    response = await kernel.invoke(
        chat_function,
        arguments
    )

    print("\nAI Response:")
    print(response)


if __name__ == "__main__":
    asyncio.run(main())