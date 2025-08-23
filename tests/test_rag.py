from src.core.agent import ResearchAgent

def test_rag():
    agent = ResearchAgent()
    result = agent.query("What are AI ethics principles?")
    print("Question:", result["question"])
    print("Answer:", result["answer"])
    print("Sources:", result["sources"][:1])
    print("Confidence:", result["confidence"])

if __name__ == "__main__":
    test_rag()