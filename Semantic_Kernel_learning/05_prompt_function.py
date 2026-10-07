import asyncio
import os

from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion


async def main():

    load_dotenv()

    kernel = Kernel()

    kernel.add_service(
        AzureChatCompletion(
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            endpoint=os.getenv("AZURE_OPENAI_BASE_URL"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
    )

    prompt = """
    Explain {{$topic}} in simple words.
    """

    explain_function = kernel.add_function(
        function_name="ExplainTopic",
        plugin_name="Education",
        prompt=prompt
    )

    result = await kernel.invoke(
        explain_function,
        topic="java"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())