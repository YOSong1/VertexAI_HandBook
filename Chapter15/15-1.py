@app.get("/health")
async def health_check():
    """
    로드밸런서나 Cloud Run이 서버 상태를 확인하기 위해 호출하는 API
    """
    return {"status": "ok", "service": "vertex-rag-api"}



print(f"Error: {e}") -> 단순 텍스트라 검색이 어려움.


import logging
# ... 설정 생략 ...
logger.error({
    "event": "rag_generation_failed",
    "error_message": str(e),
    "user_input": request.question,
    "severity": "ERROR"
})