# Chapter 5-4: System Instruction으로 AI 페르소나 부여
# 용도: 모델에 역할과 규칙을 설정하여 일관된 답변 스타일을 유지하는 방법 실습

from google import genai
from google.genai import types

# Google Gen AI 클라이언트 초기화
client = genai.Client(vertexai=True, project="your-project-id", location="us-central1")

# 시스템 지침 정의: 수학 선생님 페르소나 부여
system_prompt = """
당신은 초등학생에게 수학을 가르치는 친절한 선생님입니다.
다음 규칙을 반드시 지키세요:
1. 어려운 수학 용어 대신 쉬운 비유를 사용하세요.
2. 정답을 바로 알려주지 말고, 힌트를 주어 스스로 풀게 유도하세요.
3. 항상 존댓말을 사용하고 칭찬을 많이 해주세요.
"""

# 시스템 지침을 포함한 생성 설정
config = types.GenerateContentConfig(
    system_instruction=system_prompt
)

# 테스트
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="선생님, 피타고라스 정리가 뭐예요?",
    config=config
)
print("=== System Instruction 적용 결과 ===")
print(response.text)
