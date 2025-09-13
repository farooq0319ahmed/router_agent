# code name -> Basic Agent with OpenRouter API_Key | Openai Agent-SDK
import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled
import rich

load_dotenv()
set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# --------------------------
client = AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

agent = Agent(
    name="my agent",
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="deepseek/deepseek-r1-0528:free",openai_client=client),
)
# --------------------------
result = Runner.run_sync(starting_agent=agent, input="hi, who are you?")
rich.print(result.final_output)
