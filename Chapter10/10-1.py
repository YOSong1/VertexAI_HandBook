# Chapter 10-1: Few-shot 프롬프팅 실습
# 용도: 예시를 포함한 Few-shot 프롬프트로 모델의 응답 패턴을 유도하는 방법

from google import genai

# Google Gen AI 클라이언트 초기화
client = genai.Client(vertexai=True, project="your-project-id", location="us-central1")

# ===== Zero-shot (예시 없이 바로 질문) =====
zero_shot_prompt = """이 리뷰의 감정을 분석해줘: '음식이 식어서 왔어요.'"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=zero_shot_prompt
)
print("=== Zero-shot 결과 ===")
print(response.text)

# ===== Few-shot (예시를 포함하여 질문) =====
few_shot_prompt = """다음은 고객 리뷰에 대한 감정 분석 예시입니다.

리뷰: "배송이 정말 빠르네요!"
감정: 긍정

리뷰: "박스가 찌그러져서 왔어요."
감정: 부정

리뷰: "그냥 평범합니다."
감정: 중립

리뷰: "음식이 식어서 왔어요."
감정:"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=few_shot_prompt
)
print("\n=== Few-shot 결과 ===")
print(response.text)
