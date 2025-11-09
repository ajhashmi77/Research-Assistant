import typer
from src.core.agent import ResearchAgent

app = typer.Typer()
agent = ResearchAgent()

@app.command()
def ask(question: str):
    """CLI interface for research queries"""
    result = agent.query(question)

    print(f"\n🔍 Query: {result['question']}")
    print("=" * 60)

    print(f"\n💡 Answer:")
    print(result['answer'])

    print(f"\n📊 Research Summary:")
    print(f"   📚 Documents found: {len(result['sources']['documents'])}")
    print(f"   🌐 Web sources: {len(result['sources']['web'])}")
    print(f"   🎯 Confidence: {result['confidence']:.1%}")
    print()

if __name__ == "__main__":
    app()