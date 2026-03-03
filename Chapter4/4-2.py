# Chapter 4-4: Google Gen AI SDK 초기화 및 첫 번째 Gemini 모델 호출
# 용도: 개발 환경이 정상적으로 구축되었는지 확인하는 연결 테스트

from google import genai

# 1. Google Gen AI 클라이언트 초기화 (Vertex AI 백엔드 사용)
# ★ 본인의 GCP 프로젝트 ID로 변경해야 합니다.
PROJECT_ID = "your-project-id"
LOCATION = "us-central1"

client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)
print("Google Gen AI SDK 초기화 성공!")

# 2. Gemini 모델 호출 테스트
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Vertex AI 개발자가 된 것을 축하해줘!"
)
print(response.text)
