# Chapter 6-4: 임베딩 결과 저장 형식 설계 (벡터 + 메타데이터)
# 용도: 벡터와 메타데이터를 결합하여 저장하는 JSON 구조 설계 예시

import json
from datetime import datetime

def create_embedding_record(doc_id, text, vector, filename, page_number):
    """
    임베딩된 텍스트 조각을 저장용 JSON 레코드로 생성하는 함수

    Args:
        doc_id: 문서 고유 식별자 (예: "doc_001_chunk_05")
        text: 원본 텍스트 내용
        vector: 임베딩 벡터 (숫자 리스트)
        filename: 원본 파일명
        page_number: 페이지 번호
    """
    record = {
        "id": doc_id,
        "values": vector,  # [0.0123, -0.0456, ...]
        "metadata": {
            "text": text,
            "filename": filename,
            "page_number": page_number,
            "created_at": datetime.now().strftime("%Y-%m-%d")
        }
    }
    return record


# 사용 예시
sample_record = create_embedding_record(
    doc_id="doc_001_chunk_05",
    text="임베딩은 텍스트를 벡터로 변환하는 기술입니다.",
    vector=[0.0123, -0.0456, 0.0789],  # 실제로는 768차원
    filename="lecture_note_ch6.pdf",
    page_number=3
)

print("=== 벡터 + 메타데이터 저장 구조 ===")
print(json.dumps(sample_record, ensure_ascii=False, indent=2))
