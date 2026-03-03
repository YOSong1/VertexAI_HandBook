# Chapter 8-3: 유사도 검색(Top-k), 점수 확인, 메타데이터 필터링
# 용도: 벡터 스토어에서 다양한 방식으로 검색하는 방법 실습

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# 저장된 DB 로드
embeddings = GoogleGenerativeAIEmbeddings(
    model="text-multilingual-embedding-002",
    project="your-project-id"
)
vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

query = "Vertex AI의 주요 기능은 무엇인가요?"

# ===== 8-3-1 기본 유사도 검색 (Top-k) =====
results = vector_store.similarity_search(query, k=3)

print(f"검색된 문서 개수: {len(results)}")
for i, doc in enumerate(results):
    print(f"--- [문서 {i+1}] ---")
    print(doc.page_content[:100] + "...")

# ===== 8-3-2 유사도 점수 확인 (Score) =====
# 거리가 0에 가까울수록 의미가 유사, 클수록 관련 없음
results_with_score = vector_store.similarity_search_with_score(query, k=3)

print("\n=== 점수(거리)와 함께 검색 ===")
for doc, score in results_with_score:
    print(f"거리(Distance): {score:.4f} | 내용: {doc.page_content[:50]}...")

# ===== 8-3-3 메타데이터 필터링 =====
# 특정 조건(예: 페이지 10 이상)의 문서 중에서만 검색
results = vector_store.similarity_search(
    query,
    k=2,
    filter={"page": {"$gte": 10}}  # MongoDB 스타일의 쿼리 문법
)
print("\n=== 메타데이터 필터링 검색 ===")
for doc in results:
    print(f"페이지: {doc.metadata.get('page')} | 내용: {doc.page_content[:50]}...")
