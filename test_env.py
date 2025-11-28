from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="my_agent/.env")

print("API KEY =", os.getenv("GEMINI_API_KEY"))
# print("BASE URL =", os.getenv("OPENAI_BASE_URL"))
