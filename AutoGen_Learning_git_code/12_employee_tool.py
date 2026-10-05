def get_employee(name: str) -> str:
    employees = {
        "Padmaja": "Java Backend Developer",
        "Rahul": "Python Developer",
        "Anu": "QA Engineer"
    }

    return employees.get(name, "Employee not found")
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
assistant.register_for_llm(
    name="get_employee",
    description="Get an employee's job role by their name."
)(get_employee)

user_proxy.register_for_execution(
    name="get_employee"
)(get_employee)


user_proxy.initiate_chat(
    assistant,
    message="What is Padmaja's job role?"
)