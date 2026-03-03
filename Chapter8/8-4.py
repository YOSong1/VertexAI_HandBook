# Chapter 8-4: RAGBackend 클래스 및 Retriever 인터페이스
# 용도: 재사용 가능한 RAG 백엔드 클래스 구현 (웹 UI, 챗봇 서버 등에서 활용)

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings


class RAGBackend:
    """RAG 시스템의 검색 백엔드 클래스"""

    def __init__(self, persist_dir="./chroma_db"):
        # 1. 임베딩 모델 설정
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="text-multilingual-embedding-002",
            project="your-project-id"
        )

        # 2. 이미 저장된 DB를 로드 (데이터를 다시 넣는 게 아니라, 읽어오기만 함)
        self.vector_store = Chroma(
            persist_directory=persist_dir,
            embedding_function=self.embeddings
        )

    def retrieve_documents(self, query, k=3):
        """
        사용자의 질문(query)을 받아 가장 관련성 높은 k개의 문서를 반환합니다.
        """
        return self.vector_store.similarity_search(query, k=k)


# ===== 사용 예시 =====
if __name__ == "__main__":
    rag = RAGBackend()
    docs = rag.retrieve_documents("임베딩 모델의 가격 정책은 어떻게 되나요?")
    print(f"검색된 문서 수: {len(docs)}")
    print(f"가장 관련성 높은 내용: \n{docs[0].page_content}")

    # LangChain 표준 Retriever 인터페이스로 변환
    retriever = rag.vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )
    relevant_docs = retriever.invoke("RAG란 무엇인가?")
    print(f"\nRetriever 검색 결과: {len(relevant_docs)}건")
