import os
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

class RAGSystem:
    def __init__(self):
        self.vectorstore = None
        self.embeddings = OpenAIEmbeddings()
        
    def ingest_documents(self):
        """Document ingestion implementation"""
        try:
            # Load sample document
            loader = TextLoader("data/sample-docs/ai_ethics.txt")
            documents = loader.load()
            
            # Split into chunks
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
            chunks = text_splitter.split_documents(documents)
            
            # Create vector store
            self.vectorstore = Chroma.from_documents(
                documents=chunks,
                embedding=self.embeddings,
                persist_directory="data/vectorstore"
            )
            
            print(f"✅ Ingested {len(chunks)} document chunks")
            return len(chunks)
            
        except Exception as e:
            print(f"❌ Ingestion failed: {e}")
            return None

    def retrieve_documents(self, query: str, k: int = 3):
        """Retrieval functionality"""
        if self.vectorstore is None:
            return ["RAG system not initialized. Run ingestion first."]
        
        try:
            results = self.vectorstore.similarity_search(query, k=k)
            return results
        except Exception as e:
            return [f"Retrieval error: {str(e)}"]