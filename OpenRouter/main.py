import os 
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import rich

load_dotenv()

set_tracing_disabled(disabled=True)

OPEN_ROUTER_KEY= os.getenv("OPEN_ROUTER_KEY")

client = AsyncOpenAI(
    api_key=OPEN_ROUTER_KEY,
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(
    name="My Agent",
    instructions="You are a helpful assistant .",
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1-0528:free",openai_client=client)
)

result = Runner.run_sync(starting_agent=agent, input="hy, who are you? and also tell company. given answer within 30 words")

print(result.final_output)