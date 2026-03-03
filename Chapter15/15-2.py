# Chapter 15 보충: 구조화된 로깅 및 에러 핸들링 패턴
# 용도: 운영 환경에서 필수적인 JSON 구조화 로깅과 핵심 에러 처리 포인트 예시

import logging
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Vertex AI RAG API")

# ===== 구조화된 JSON 로깅 설정 =====
class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            "severity": record.levelname,
            "message": record.getMessage(),
            "timestamp": self.formatTime(record),
        }
        if hasattr(record, "extra_data"):
            log_entry.update(record.extra_data)
        return json.dumps(log_entry, ensure_ascii=False)

handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger = logging.getLogger("rag-api")
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# ===== 헬스체크 엔드포인트 =====
@app.get("/health")
async def health_check():
    """로드밸런서나 Cloud Run이 서버 상태를 확인하기 위해 호출하는 API"""
    return {"status": "ok", "service": "vertex-rag-api"}

# ===== 에러 핸들링이 포함된 채팅 엔드포인트 =====
class QueryRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    try:
        logger.info("질문 수신", extra={"extra_data": {"user_input": request.question}})

        # 1. RAG 검색 (에러 포인트: DB 연결 실패 가능)
        # docs = rag_backend.retrieve_documents(request.question)

        # 2. LLM 호출 (에러 포인트: API 호출 실패, 타임아웃 가능)
        # response = llm.invoke(full_prompt)

        # 3. 응답 반환
        return {"question": request.question, "answer": "생성된 답변"}

    except Exception as e:
        logger.error(json.dumps({
            "event": "rag_generation_failed",
            "error_message": str(e),
            "user_input": request.question,
            "severity": "ERROR"
        }, ensure_ascii=False))
        raise HTTPException(status_code=500, detail=str(e))
