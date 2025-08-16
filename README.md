# 🔍 Research Assistant Agent with RAG Integration

[![LangChain](https://img.shields.io/badge/LangChain-0.1.0-blue)](https://python.langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.0.10-orange)](https://langchain-ai.github.io/langgraph)
[![RAG Enabled](https://img.shields.io/badge/RAG-Enabled-success)](https://arxiv.org/abs/2005.11401)

An intermediate-level research assistant that combines web research with private document analysis using Retrieval-Augmented Generation (RAG).

## ✨ Key Features
1. **Intelligent Query Planning**  
   Automatically decomposes complex questions into optimized search queries
2. **Multi-Source Research**  
   Parallel web search + RAG-based document retrieval
3. **Citation-Aware Answers**  
   Answers with proper source attribution (web + document/page numbers)
4. **Self-Correction**  
   Automatic follow-up questions for low-confidence answers

## 🧠 Architecture Overview
```mermaid
graph TD
    A[User Question] --> B(Planning Node)
    B --> C[Web Search]
    B --> D[RAG Document Retrieval]
    C --> E[Evaluation Node]
    D --> E
    E --> F{Confidence > 80%?}
    F -->|Yes| G[Final Answer]
    F -->|No| B
    G --> H[Response with Citations]

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/<your-username>/research-assistant.git
cd research-assistant

# Install dependencies
python3 -m pip install -r requirements.txt

# Set environment variables
echo "OPENAI_API_KEY=your_key_here" > .env
echo "TAVILY_API_KEY=your_key_here" >> .env

# Set up sample documents
mkdir -p data/documents
cp data/sample-docs/* data/documents/

# Ingest documents into vector store
python3 src/rag/ingestion.py

# Run sample query
python3 src/main.py "What are the key principles of AI ethics?"