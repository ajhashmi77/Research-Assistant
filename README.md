# Research Assistant Agent 🕵️‍♂️

[![LangChain](https://img.shields.io/badge/LangChain-0.1.0-blue)](https://python.langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.0.10-orange)](https://langchain-ai.github.io/langgraph)

An intermediate-level research assistant built with LangChain and LangGraph that:
1. Plans search strategies for complex questions
2. Gathers information from multiple sources in parallel
3. Synthesizes answers with proper citations
4. Automatically generates follow-up questions

## 🚀 Quick Start
```bash
# Clone repository
git clone https://github.com/<your-username>/research-assistant.git

# Install dependencies
pip install -r requirements.txt

# Set environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
echo "TAVILY_API_KEY=your_key_here" >> .env

# Run sample query
python src/main.py "Impact of quantum computing on RSA encryption?"