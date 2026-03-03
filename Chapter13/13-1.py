from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_backend import RAGBackend # Ch8에서 만든 클래스

# 1. FastAPI 앱 인스턴스 생성
app = FastAPI(title="Vertex AI RAG API")

# 2. RAG 백엔드 로드 (서버 시작 시 1회만 실행)
# 실제 운영 환경에서는 DB 연결 등을 여기서 수행합니다.
rag_backend = RAGBackend()

# 3. 요청 데이터 구조 정의 (Pydantic 모델)
class QueryRequest(BaseModel):
    question: str

# 4. API 엔드포인트 정의
@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    """
    사용자의 질문을 받아 RAG 검색 및 답변을 반환하는 API
    """
    try:
        # 질문에 대한 관련 문서 검색
        docs = rag_backend.retrieve_documents(request.question)
        
        # (여기서 LLM 호출 로직이 추가될 수 있음)
        # 예시를 위해 검색된 문서 내용만 반환
        context = "\n".join([d.page_content for d in docs])
        
        return {
            "question": request.question,
            "answer": "생성된 답변이 여기 들어갑니다.",
            "context": context
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))