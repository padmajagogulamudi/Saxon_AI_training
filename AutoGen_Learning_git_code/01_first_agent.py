from autogen import ConversableAgent

agent = ConversableAgent(
    name="my_agent",
    llm_config=False,
    human_input_mode="NEVER"
)

print(agent.name)