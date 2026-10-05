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
    system_message="You are a helpful mathematical assistant.",
    llm_config=llm_config
)

user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=1,
    code_execution_config=False
)


def add_numbers(a: int, b: int) -> int:
    return a + b


assistant.register_for_llm(
    name="add_numberss",
    description="Add two numbers together."
)(add_numbers)

user_proxy.register_for_execution(
    name="add_numberss"
)(add_numbers)


user_proxy.initiate_chat(
    assistant,
    message="What is 25 plus 17? Use the add_numbers tool."
)