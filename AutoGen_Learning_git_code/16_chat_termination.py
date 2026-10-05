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

cathy = ConversableAgent(
    name="cathy",
    system_message="Your name is Cathy. Tell jokes.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

joe = ConversableAgent(
    name="joe",
    system_message="Your name is Joe. Ask Cathy for a joke.",
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "good bye" in msg["content"].lower()
)

result = joe.initiate_chat(
    cathy,
    message="Cathy, tell me a joke and then say GOOD BYE."
)