from dotenv import load_dotenv
from agents import Agent, Runner, ModelSettings

load_dotenv()

agent = Agent(
    name = "myagent",
    instructions="you are a helpful assistant",
    model_settings=ModelSettings(temperature=1)# temperature controls randomness in output (0-1) by default 0.7 1 is more random/creative
)

result = Runner.run_sync(starting_agent=agent, input="write a poem about AI")
print(result.final_output)
