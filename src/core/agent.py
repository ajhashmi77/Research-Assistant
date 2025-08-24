from typing import Dict, List
from .rag import RAGSystem
from .web_search import web_search

class ResearchAgent:
    def __init__(self):
        self.rag = RAGSystem()
        
    def initialize(self):
        self.rag.ingest_documents()
        
    def query(self, question: str) -> Dict:
        if not self.rag.vectorstore:
            self.initialize()
        
        # Parallel research: RAG + Web Search
        rag_results = self.rag.retrieve_documents(question)
        web_results = web_search(question)
        
        return {
            "question": question,
            "answer": self._synthesize_answer(rag_results, web_results),
            "sources": {
                "documents": rag_results,
                "web": web_results
            },
            "confidence": self._calculate_confidence(rag_results, web_results)
        }
    
    def _synthesize_answer(self, rag_results, web_results) -> str:
        """Combine RAG and web results"""
        total_sources = len(rag_results) + len(web_results)
        return f"Found {total_sources} total sources ({len(rag_results)} documents, {len(web_results)} web results)"
    
    def _calculate_confidence(self, rag_results, web_results) -> float:
        """Calculate confidence based on source count"""
        total_sources = len(rag_results) + len(web_results)
        return min(0.95, 0.2 + (total_sources * 0.1))