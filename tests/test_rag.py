from src.core.agent import ResearchAgent

def test_hybrid_research():
    agent = ResearchAgent()
    result = agent.query("AI ethics principles")
    
    print("Question:", result["question"])
    print("Answer:", result["answer"])
    print("Document sources:", len(result["sources"]["documents"]))
    print("Web sources:", len(result["sources"]["web"]))
    print("Confidence:", result["confidence"])

if __name__ == "__main__":
    test_hybrid_research()