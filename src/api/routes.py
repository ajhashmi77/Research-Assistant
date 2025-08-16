from fastapi import FastAPI
from src.core.agent import ResearchAgent

app = FastAPI()
agent = ResearchAgent()

@app.get("/query/{question}")
async def research(question: str):
    return agent.query(question)