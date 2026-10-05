import os
import json

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
    system_message="You are a helpful employee information assistant. Use the available tools when needed.",
    llm_config=llm_config
)


user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",max_consecutive_auto_reply=1,
    code_execution_config=False
)


def get_employee(name: str) -> str:

    with open("employees.json", "r") as file:
        employees = json.load(file)

    return employees.get(name, "Employee not found")


def add_employee(name: str, role: str) -> str:

    with open("employees.json", "r") as file:
        employees = json.load(file)

    employees[name] = role

    with open("employees.json", "w") as file:
        json.dump(employees, file, indent=4)

    return f"Employee {name} added successfully."


assistant.register_for_llm(
    name="get_employee",
    description="Get an employee's job role by their name."
)(get_employee)


assistant.register_for_llm(
    name="add_employee",
    description="Add a new employee with their name and job role."
)(add_employee)


user_proxy.register_for_execution(
    name="get_employee"
)(get_employee)


user_proxy.register_for_execution(
    name="add_employee"
)(add_employee)

user_proxy.initiate_chat(
    assistant,
    message="What is Kiran's job role?"
)