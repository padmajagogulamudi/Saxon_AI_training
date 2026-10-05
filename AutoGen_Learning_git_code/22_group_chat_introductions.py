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

number_agent = ConversableAgent(
    name="Number_Agent",
    system_message="You return the numbers I give you.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

adder_agent = ConversableAgent(
    name="Adder_Agent",
    system_message="You add 1 to each number you receive.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

multiplier_agent = ConversableAgent(
    name="Multiplier_Agent",
    system_message="You multiply each number you receive by 2.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

subtracter_agent = ConversableAgent(
    name="Subtracter_Agent",
    system_message="You subtract 1 from each number you receive.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

divider_agent = ConversableAgent(
    name="Divider_Agent",
    system_message="You divide each number you receive by 2.",
    llm_config=llm_config,
    human_input_mode="NEVER"
)

number_agent.description = "Return the numbers given."
adder_agent.description = "Add 1 to each input number."
multiplier_agent.description = "Multiply each input number by 2."
subtracter_agent.description = "Subtract 1 from each input number."
divider_agent.description = "Divide each input number by 2."

group_chat = GroupChat(
    agents=[
        adder_agent,
        multiplier_agent,
        subtracter_agent,
        divider_agent,
        number_agent
    ],
    messages=[],
    max_round=6,
    send_introductions=True,
    speaker_selection_method="random"
)

group_chat_manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config
)

chat_result = number_agent.initiate_chat(
    group_chat_manager,
    message="My number is 3, I want to turn it into 13.",
    summary_method="reflection_with_llm"
)

print("Final Summary:")
print(chat_result.summary)