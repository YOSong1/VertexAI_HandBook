# Chapter 5-2: 기본 텍스트 생성 및 생성 제어 파라미터
# 용도: Gemini API의 기본 텍스트 생성과 temperature, max_output_tokens 등의 파라미터 조절 실습

from google import genai
from google.genai import types

# Google Gen AI 클라이언트 초기화
client = genai.Client(vertexai=True, project="your-project-id", location="us-central1")

# 1. 기본 텍스트 생성 (Flash 모델 - 가성비 최고)
prompt = "인공지능 개발자가 되기 위해 공부해야 할 3가지를 요약해줘."
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)
print("=== 기본 텍스트 생성 ===")
print(response.text)

# 2. 생성 제어 파라미터 (Configuration)
config = types.GenerateContentConfig(
    temperature=0.7,        # 0~2, 높을수록 창의적 (0.2: 사실적, 0.8: 창의적)
    max_output_tokens=500   # 답변 최대 길이 제한
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="창의적인 마케팅 슬로건 5개 만들어줘",
    config=config
)
print("\n=== 파라미터 조절 텍스트 생성 ===")
print(response.text)
