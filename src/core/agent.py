from typing import Dict
from .rag import ingest_documents  # Your existing RAG functions

class ResearchAgent:
    def __init__(self):
        self.vectorstore = None
        
    def initialize(self):
        """Initialize RAG system"""
        self.vectorstore = ingest_documents()
        
    def query(self, question: str) -> Dict:
        """Core research functionality"""
        if not self.vectorstore:
            self.initialize()
            
        return {
            "question": question,
            "answer": "",  # Your implementation
            "sources": [],
            "confidence": 0.0
        }