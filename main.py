from agents import Agent, Runner ,OpenAIChatCompletionsModel,AsyncOpenAI
GEMINI_API_KEY="AIzaSyDKh43nO1AhlKti6pMfGQJi2k6nq6Q-fQ0"
import os
from dotenv import load_dotenv,find_dotenv
load_dotenv(find_dotenv())

#whcih llm service to use
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
#which llm model to use
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",
    openai_client=external_client
)
#Creating the agent
agent = Agent(name="Assistant", model=llm_model)

result = Runner.run_sync(starting_agent=agent,input= "Write a haiku about recursion in programming.")
print("Agent Respone",result.final_output)

# Code within the code,
# Functions calling themselves,
# Infinite loop's dance.