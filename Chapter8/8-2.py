# Chapter 8-2: 벡터 스토어 생성 및 데이터 저장
# 용도: Chapter 7의 split_docs를 ChromaDB에 벡터로 변환하여 저장

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# 1. Google Gen AI 임베딩 모델을 LangChain 래퍼로 설정
# 이 객체는 텍스트가 들어오면 자동으로 Google API를 호출해 벡터로 변환
embeddings = GoogleGenerativeAIEmbeddings(
    model="text-multilingual-embedding-002",
    project="your-project-id"
)

# 2. ChromaDB 생성 및 데이터 입력
# persist_directory: 내 PC의 폴더에 파일로 영구 저장
# ★ split_docs는 Chapter 7에서 만든 청크 리스트를 사용
vector_store = Chroma.from_documents(
    documents=split_docs,           # Ch7에서 만든 청크 리스트
    embedding=embeddings,           # 임베딩 모델
    persist_directory="./chroma_db" # 저장 경로
)
print("벡터 스토어 구축 완료! 데이터가 './chroma_db' 폴더에 저장되었습니다.")
