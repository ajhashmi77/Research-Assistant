from typing import Dict, List
from .rag import RAGSystem
from .web_search import web_search
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class ResearchAgent:
    def __init__(self):
        self.rag = RAGSystem()
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")
        
    def initialize(self):
        self.rag.ingest_documents()
        
    def query(self, question: str) -> Dict:
        if not self.rag.vectorstore:
            self.initialize()
        
        # Get research results
        rag_results = self.rag.retrieve_documents(question)
        web_results = web_search(question)
        
        # Synthesize answer
        synthesized_answer = self._synthesize_answer(question, rag_results, web_results)
        
        return {
            "question": question,
            "answer": synthesized_answer,
            "sources": {
                "documents": len(rag_results),
                "web": len(web_results)
            },
            "confidence": self._calculate_confidence(rag_results, web_results)
        }
    
    def _synthesize_answer(self, question: str, rag_results: list, web_results: list) -> str:
        """Synthesize answer from multiple sources"""
        if not rag_results and not web_results:
            return "No relevant information found."
        
        # Prepare context
        context = "SOURCES:\n"
        
        # Add document context
        for i, doc in enumerate(rag_results[:2]):  # Top 2 documents
            context += f"\nDocument {i+1}:\n{doc.page_content[:500]}...\n"
        
        # Add web context  
        for i, result in enumerate(web_results[:3]):  # Top 3 web results
            context += f"\nWeb Result {i+1}:\n{result.get('content', result.get('title', 'No content'))[:300]}...\n"
        
        # Create prompt
        prompt = ChatPromptTemplate.from_template("""
        Based on the following sources, answer the question clearly and concisely.
        
        QUESTION: {question}
        
        {context}
        
        ANSWER:
        """)
        
        # Generate answer
        try:
            chain = prompt | self.llm
            response = chain.invoke({
                "question": question,
                "context": context
            })
            return response.content
        except Exception as e:
            return f"Failed to generate answer: {str(e)}"
    
    def _calculate_confidence(self, rag_results, web_results) -> float:
        total_sources = len(rag_results) + len(web_results)
        return min(0.95, 0.3 + (total_sources * 0.1))