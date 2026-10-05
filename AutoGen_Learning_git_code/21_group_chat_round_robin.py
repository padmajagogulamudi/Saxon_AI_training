import os
from autogen import ConversableAgent, GroupChat, GroupChatManager
from dotenv import load_dotenv

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

agent_a = ConversableAgent(
    name="Agent_A",
    system_message="You are Agent A. Respond briefly.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

agent_b = ConversableAgent(
    name="Agent_B",
    system_message="You are Agent B. Respond briefly.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

agent_c = ConversableAgent(
    name="Agent_C",
    system_message="You are Agent C. Respond briefly.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

group_chat = GroupChat(
    agents=[agent_a, agent_b, agent_c],
    messages=[],
    max_round=6,
    speaker_selection_method="manual"
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)

agent_a.initiate_chat(
    group_chat_manager,
    message="Start a short discussion about artificial intelligence."
)