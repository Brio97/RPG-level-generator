from dotenv import load_dotenv
import os

load_dotenv()

print("OPENAI_API_KEY:", "FOUND" if os.getenv("OPENAI_API_KEY") else "MISSING")
print("LITELLM_API_KEY:", "FOUND" if os.getenv("LITELLM_API_KEY") else "MISSING")
print("LITELLM_API_BASE:", os.getenv("LITELLM_API_BASE"))
