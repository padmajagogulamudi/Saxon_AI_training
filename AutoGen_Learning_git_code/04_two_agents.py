import os
from dotenv import load_dotenv
from autogen import ConversableAgent

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

java_teacher = ConversableAgent(
    name="java_teacher",
    system_message="You are an expert Java teacher. Explain Java concepts clearly.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

java_interviewer = ConversableAgent(
    name="java_interviewer",
    system_message="You are a Java interviewer. Ask Java interview questions and evaluate the teacher's answers.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

chat_result = java_interviewer.initiate_chat(
    java_teacher,
    message="Ask the Java teacher one interview question about inheritance.",
    max_turns=2
)

print(chat_result)