from crewai import Agent
from textwrap import dedent
from langchain_community.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_anthropic import ChatAnthropic


class CustomAgents:
    def __init__(self):
        # self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4o", temperature=0.7)
        # self.AnthropicLLM = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0.7)
        # self.Ollama = ChatOpenAI(model_name="devainllama3", base_url = "http://localhost:11434/v1") 
        self.GroqLLM = ChatGroq(model_name="mixtral-8x7b-32768", temperature=0.7)
        
    def architect_agent(self, tools):
        return Agent(
            role="Software Architect",
            backstory=dedent(f"""\
            With years of experience in system design, 
            you excel at breaking down complex problems into manageable solutions,
            providing a solid foundation for implementation."""),
            goal=dedent(f"""\
            Provide a high-level solution overview for a given problem"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.GroqLLM,
        )

    def programmer_agent(self, tools):
        return Agent(
            role="Software Programmer",
            backstory=dedent(f"""\
            You havea keen eye for detail and a knack for translating high-level design solutions into robust,
            efficient code."""),
            goal=dedent(f"""Implement the solution provided by the architect"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.GroqLLM,
        )

    def tester_agent(self, tools):
        return Agent(
            role="Software Tester",
            backstory=dedent(f"""\
            Your passion for quality ensures that every piece of code meets the highest
            standards through rigorous testing."""),
            goal = dedent("""\
            Write and run test cases for the code implemented by the programmer"""),
            tools=tools,
            allow_delegation=False,
            verbose=True,
            llm=self.GroqLLM,
        )

    def reviewer_agent(self, tools):
        return Agent(
            role="Software Reviewer",
            backstory=dedent("""\
            With a critical eye, you review each step of the development process, ensuring quality and consistency."""),
            goal=dedent("""\
            Review the work of each agent at each step"""),
            tools=tools,            
            allow_delegation=False,
            verbose=True,
            llm=self.GroqLLM,
        )
