# Chapter 6-3: Google Gen AI Embeddings API 호출 및 유사도 비교
# 용도: 텍스트를 벡터로 변환하고, 코사인 유사도로 의미적 유사성을 비교하는 실습

from google import genai
from google.genai import types
import numpy as np

# Google Gen AI 클라이언트 초기화
client = genai.Client(vertexai=True, project="your-project-id", location="us-central1")

# 1. 임베딩 모델 설정 (최신 다국어 모델 사용)
EMBEDDING_MODEL = "text-multilingual-embedding-002"

def get_embedding(text):
    """텍스트를 입력받아 벡터(숫자 리스트)를 반환하는 함수"""
    result = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )
    return result.embeddings[0].values

# 2. 텍스트 임베딩 테스트
text = "Vertex AI는 Google Cloud의 머신러닝 플랫폼입니다."
vector = get_embedding(text)

print(f"텍스트: {text}")
print(f"벡터 길이(차원 수): {len(vector)}")
print(f"벡터 앞부분 10개: {vector[:10]}")

# 3. 코사인 유사도 비교 실습
def cosine_similarity(a, b):
    """두 벡터 사이의 유사도를 계산하는 함수 (코사인 유사도)"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

vec1 = get_embedding("맛있는 사과")
vec2 = get_embedding("달콤한 과일")
vec3 = get_embedding("빠른 자동차")

score1 = cosine_similarity(vec1, vec2)  # 사과 vs 과일 (의미 유사)
score2 = cosine_similarity(vec1, vec3)  # 사과 vs 자동차 (의미 상이)

print(f"\n=== 유사도 비교 결과 ===")
print(f"사과 vs 과일 유사도: {score1:.4f}")
print(f"사과 vs 자동차 유사도: {score2:.4f}")
print(f"→ '사과'는 '자동차'보다 '과일'에 의미적으로 훨씬 가깝습니다!")
