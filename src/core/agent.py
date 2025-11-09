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
        
        # Parallel research: RAG + Web Search
        rag_results = self.rag.retrieve_documents(question)
        web_results = web_search(question)
        
        # Synthesize answer using LLM
        synthesized_answer = self._synthesize_answer(question, rag_results, web_results)

        return {
            "question": question,
            "answer": synthesized_answer,
            "sources": {
                "documents": rag_results,
                "web": web_results
            },
            "confidence": self._calculate_confidence(rag_results, web_results)
        }
    
    def _synthesize_answer(self, question: str, rag_results: list, web_results: list) -> str:
        """Synthesize answer from multiple sources using LLM"""
        if not rag_results and not web_results:
            return "No relevant information found."

        # Prepare context from sources
        context = "SOURCES:\n"

        # Add document context
        for i, doc in enumerate(rag_results[:3]):  # Top 3 documents
            content = getattr(doc, 'page_content', str(doc))[:400]
            context += f"\nDocument {i+1}: {content}...\n"

        # Add web context
        for i, result in enumerate(web_results[:3]):  # Top 3 web results
            content = result.get('content', result.get('title', 'No content'))[:300]
            context += f"\nWeb Source {i+1}: {content}...\n"

        # Create synthesis prompt
        prompt = ChatPromptTemplate.from_template("""
        Based on the following sources, provide a comprehensive answer to the question.
        Include specific details and cite relevant information where appropriate.

        QUESTION: {question}

        {context}

        SYNTHESIZED ANSWER:
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
        """Calculate confidence based on source count"""
        total_sources = len(rag_results) + len(web_results)
        return min(0.95, 0.2 + (total_sources * 0.1))