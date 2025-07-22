from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

# Load environment variables
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Validate API key
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Gemini via OpenAI-compatible endpoint (reference: https://ai.google.dev/gemini-api/docs/openai)
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Define config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define agent with valid arguments only
agent = Agent(
    name="Gemini Agent",
    instructions="You are a helpful assistant that can answer questions and help with tasks.",
    tools=[],
)

# Run the agent synchronously
response = Runner.run_sync(
    agent,
    input="What is the capital of the Pakistan?",
    run_config=config,
)

print(response)
