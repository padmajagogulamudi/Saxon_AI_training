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
    system_message="You are a Python programming assistant. When appropriate, provide executable Python code.",
    llm_config=llm_config
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=4,
    code_execution_config={
        "work_dir": "coding",
        "use_docker": False
    }
)

user_proxy.initiate_chat(
    assistant,
    message="Calculate the sum of numbers from 1 to 10. Write Python code to calculate it."
)