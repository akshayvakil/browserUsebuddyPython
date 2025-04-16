from browser_use.agent.service import Agent
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio


async def test_validation():
    task = (
        'I am automation tester validating a task '
        'Open website https://www.amazon.in/ '
        'search iphone 16 '
        'verify Supersmart word on page'
    )

    llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro-exp-03-25', api_key='testkey')
    agent = Agent(task, llm)
    await agent.run()


# Run the async function
asyncio.run(test_validation())