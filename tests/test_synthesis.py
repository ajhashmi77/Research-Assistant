from src.core.agent import ResearchAgent

def test_answer_synthesis():
    agent = ResearchAgent()
    result = agent.query("What are the main principles of AI ethics?")
    
    print("🔍 Question:", result["question"])
    print("💡 Answer:", result["answer"])
    print("📊 Sources:", result["sources"])
    print("🎯 Confidence:", result["confidence"])

if __name__ == "__main__":
    test_answer_synthesis()