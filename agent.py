from google.adk.agents.llm_agent import Agent
from google.adk.models.google_llm import Gemini
from google.adk.tools import google_search
from google.genai import types

# 1. Mock tool implementation for time
def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    # This is the mock data the agent will return
    return {"status": "success", "city": city, "time": "10:30 AM"}

# 2. Model Definition
# You must define the model object here if you use an LLM that is not the default
model = Gemini(
    model='gemini-2.5-flash-lite', # Using the model you previously defined
    retry_options=types.HttpRetryOptions(
        attempts=5,
        exp_base=5,
        initial_delay=1,
        http_status_codes=[429, 500, 503, 504]
    )
)

# 3. Agent Definition (Using the required name: root_agent)
root_agent = Agent(
    name="search_agent",
    model=model,
    description="A helpful assistant that can answer questions using real-time information from Google Search.",
    instruction="You are a helpful assistant. Use the 'google_search' tool for current information, facts, or any query requiring external knowledge.",
    # The tools list now includes the imported google_search function
    tools=[google_search],
)