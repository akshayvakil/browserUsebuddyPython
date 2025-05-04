import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import  SecretStr
import asyncio


async def Sitevalidation():
    os.environ["GEMIMI_API_KEY"]= "zaSyCrM2P1Mm5e95rpzGXDWTGlLCZR3BPVQU" # add s
    print("Starting AI Agent code")
    task = (
        'I am automation tester validating a task '
        'Open website https://www.amazon.in/ '
        'search iphone 16 '
        'verify Supersmart word on page'
    )
    api_key=os.environ["GEMIMI_API_KEY"]

    llm = ChatGoogleGenerativeAI(
        model='gemini-2.0-flash-exp' ,
        api_key=SecretStr(api_key) ,
        use_vision=True
    )

    agent = Agent(task, llm)
    history=await agent.run()
    testResult = history.final_result()
    print(testResult)

asyncio.run(Sitevalidation())
