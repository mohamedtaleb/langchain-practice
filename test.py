from dotenv import load_dotenv
import os

load_dotenv(override=True)

print("CWD =", os.getcwd())
print("GOOGLE_API_KEY =", os.getenv("GOOGLE_API_KEY"))


print("Tracing:", os.getenv("LANGCHAIN_TRACING_V2"))
print("API key smith:", os.getenv("LANGSMITH_API_KEY"))