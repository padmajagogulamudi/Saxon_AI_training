import os
from dotenv import load_dotenv

from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

load_dotenv()

kernel = Kernel()

chat_service = AzureChatCompletion(
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY")
)

kernel.add_service(chat_service)

print("Kernel and AI service configured successfully!")