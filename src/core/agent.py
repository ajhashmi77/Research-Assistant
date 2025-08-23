from typing import Dict
from .rag import RAGSystem

class ResearchAgent:
    def __init__(self):
        self.rag = RAGSystem()
        
    def initialize(self):
        """Initialize RAG system"""
        self.rag.ingest_documents()
        
    def query(self, question: str) -> Dict:
        if not self.rag.vectorstore:
            self.initialize()
        
        retrieved_docs = self.rag.retrieve_documents(question)
        
        return {
            "question": question,
            "answer": f"Found {len(retrieved_docs)} relevant document chunks",
            "sources": [str(doc.metadata) for doc in retrieved_docs] if retrieved_docs and hasattr(retrieved_docs[0], 'metadata') else [],
            "confidence": min(0.9, 0.3 + len(retrieved_docs) * 0.2)
        }