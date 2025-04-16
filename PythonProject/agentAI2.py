import os

from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import  SecretStr
import asyncio


async def Sitevalidation():
    os.environ["GEMIMI_API_KEY"]= "AIzaSyCrM2P1Mm5e95rpzGXDWTGlLCZR3BPVQUs"
    print("Starting AI Agent code")
    task = (
        'Important: I am UI Automation tester validating the tasks'
        'Open website https://rahulshettyacademy.com/loginpagePractise'
        'Login with username and password. Login Details available in the same page'
        'After login, select first 2 products and add them to cart'
        'Then checkout and store the total value you see in screen'
        'Increase the quantity of any product and check if total value update accordingly'
        'checkout and select country, agree terms and purchase'
        'verify thankyou message is displayed'
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
