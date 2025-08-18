from src.core.agent import ResearchAgent

def test_agent_response():
    agent = ResearchAgent()
    result = agent.query("Test question")
    assert isinstance(result, dict)
    assert "answer" in result