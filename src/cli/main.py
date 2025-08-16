import typer
from src.core.agent import ResearchAgent

app = typer.Typer()
agent = ResearchAgent()

@app.command()
def ask(question: str):
    """CLI interface for research queries"""
    result = agent.query(question)
    print(f"🔍 Results for: {result['question']}")
    print(f"💡 Answer: {result['answer']}")
    print(f"📚 Sources: {len(result['sources'])} found")

if __name__ == "__main__":
    app()