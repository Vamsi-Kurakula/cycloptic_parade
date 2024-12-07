from crewai import Agent
from textwrap import dedent
from langchain_community.chat_models import ChatOpenAI

from crewai_tools  import SerperDevTool


search_tool = SerperDevTool()

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)

    def moderator(self):
        return Agent(
            role="Conversation Moderator",
            backstory=dedent(
                f"""Expert moderating conversations between two indivduals."""),
            goal=dedent(f"""
                        Facilitate a conversation between two indivudals. 
                        Do not insert yourself into the conversation, 
                        make sure the conversation between the two remains engaging
                        """),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def character(self):
        return Agent(
            role="Character",
            backstory=dedent(
                f"""Expert doing research on a character and embodying their personality and manorisms"""),
            goal=dedent(
                f"""Become the selected character by searching the internet for information on them 
                and respond to conversations and questions exactly as if you were that character"""),
            tools=[search_tool],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

