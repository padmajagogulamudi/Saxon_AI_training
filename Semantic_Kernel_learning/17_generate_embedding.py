import asyncio
import os

from dotenv import load_dotenv
from semantic_kernel.connectors.ai.open_ai import AzureTextEmbedding


async def main():
    load_dotenv()
    print("Embedding deployment:", os.getenv("CORE_AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"))
    print("Endpoint:", repr(os.getenv("CORE_AZURE_OPENAI_ENDPOINT")))
    print("API key present:", bool(os.getenv("CORE_AZURE_OPENAI_API_KEY")))
    print("API version:", os.getenv("CORE_AZURE_OPENAI_API_VERSION"))
    deployment_name = os.getenv("CORE_AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME")
    endpoint = os.getenv("CORE_AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("CORE_AZURE_OPENAI_API_KEY")
    api_version = os.getenv("CORE_AZURE_OPENAI_API_VERSION")

    if not all([deployment_name, endpoint, api_key, api_version]):
        raise ValueError("Missing required Azure OpenAI environment variables.")

    embedding_service = AzureTextEmbedding(
        deployment_name=deployment_name,
        endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
    )

    text = "Employees can take sick leave when they are unwell."

    embeddings = await embedding_service.generate_embeddings([text])
    embedding = embeddings[0]

    print("Embedding generated successfully.")
    print("Number of dimensions:", len(embedding))
    print("First five values:", embedding[:5])


if __name__ == "__main__":
    asyncio.run(main())