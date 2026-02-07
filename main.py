from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_models import ChatOllama
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
import os
#from tavily import TavilyClient
from langchain_tavily import TavilySearch
load_dotenv(override=True)


llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
tools = [TavilySearch()]
agent = create_agent(model = llm, tools = tools ) 
def main():
    print("Hello form langchain-course!")
    result = agent.invoke({"messages": HumanMessage(content="Search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)
   
if __name__ == "__main__":
    main()
