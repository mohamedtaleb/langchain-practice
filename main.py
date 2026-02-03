from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_community.chat_models import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
import os
import google.genai as genai
load_dotenv()

@tool
def search(query: str) ->str:
    """
    Tool that searches over internet
    Args:
        query: The query to search for
    Returns:
        The search result
    """

    print(f"Searching for {query}")
    return "Tokyo weather is sunny"
def main():
    print("Hello from langchain-course!")
    information = """ Elon Musk, né le 28 juin 1971 à Pretoria (Afrique du Sud)"""
    print(information)
if __name__ == "__main__":
    main()
