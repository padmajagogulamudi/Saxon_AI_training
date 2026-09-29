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

agent = ConversableAgent(
    name="my_agent",
    llm_config=llm_config,
    human_input_mode="NEVER"
)
reply=agent.generate_reply(
    messages=[{
        "role":"user",
        "content":"What is the difference between an embedding and a vector?"
    }]
)
print("reply : ",reply)