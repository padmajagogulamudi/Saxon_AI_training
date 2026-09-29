import os
from dotenv import load_dotenv
from autogen import AssistantAgent, UserProxyAgent

load_dotenv()

llm_config = {
    "config_list": [
        {
            "model": os.getenv("AZURE_OPENAI_MODEL"),
            "api_key": os.getenv("AZURE_OPENAI_API_KEY"),
            "base_url": os.getenv("AZURE_OPENAI_BASE_URL"),
            "api_type": os.getenv("AZURE_OPENAI_API_TYPE"),
            "api_version": os.getenv("AZURE_OPENAI_API_VERSION")
        }
    ]
}

assistant = AssistantAgent(
    name="assistant",
    system_message="You are a helpful Java programming assistant.",
    llm_config=llm_config
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="ALWAYS",
    code_execution_config=False
)

user_proxy.initiate_chat(
    assistant,
    message="Explain method overloading in Java.",
     max_turns=2
)