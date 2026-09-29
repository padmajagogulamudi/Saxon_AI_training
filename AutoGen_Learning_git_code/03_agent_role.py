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
    system_message="You are a strict Java interviewer. Ask difficult Java interview questions and expect precise answers.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

reply = java_teacher.generate_reply(
    messages=[
        {
            "role": "user",
            "content": "Ask me one Java interview question."
        }
    ]
)

print(reply)