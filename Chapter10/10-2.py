# Chapter 10-2: Chain-of-Thought(CoT) 및 도메인 전용 지시문 실습
# 용도: 단계적 추론(CoT)과 페르소나/스타일 프리셋을 적용하여 응답 품질을 높이는 방법

from google import genai
from google.genai import types

# Google Gen AI 클라이언트 초기화
client = genai.Client(vertexai=True, project="your-project-id", location="us-central1")

# ===== Chain-of-Thought (CoT): 단계적 추론 =====
# 일반 프롬프트 vs CoT 프롬프트 비교
normal_prompt = "사과 5개가 있는데 2개를 먹고 3개를 더 샀어. 몇 개야?"
cot_prompt = """사과 5개가 있는데 2개를 먹고 3개를 더 샀어. 몇 개야?
단계별로 차근차근 생각해보자. (Let's think step by step)"""

print("=== 일반 프롬프트 ===")
response = client.models.generate_content(model="gemini-2.5-flash", contents=normal_prompt)
print(response.text)

print("\n=== CoT 프롬프트 ===")
response = client.models.generate_content(model="gemini-2.5-flash", contents=cot_prompt)
print(response.text)

# ===== 도메인 전용 지시문 (IT 헬프데스크 봇) =====
it_helpdesk_system = """당신은 10년 차 IT 시스템 관리자입니다.
비전문가인 직원들에게 기술적인 문제를 아주 쉽게 설명해야 합니다.
답변 시 다음 원칙을 따르세요:
1. 전문 용어(예: DNS, DHCP)를 사용할 때는 반드시 괄호 안에 풀어서 설명하세요.
2. 해결 방법은 항상 1, 2, 3 번호가 매겨진 리스트 형태로 제공하세요.
3. 마지막에는 "해결되지 않으면 02-1234로 전화주세요"라는 문구를 덧붙이세요."""

config = types.GenerateContentConfig(
    system_instruction=it_helpdesk_system
)

print("\n=== 도메인 전용 지시문 적용 ===")
response = client.models.generate_content(
    model="gemini-2.5-pro",
    contents="인터넷이 안 돼요",
    config=config
)
print(response.text)

# ===== 출력 스타일 프리셋 (회의록 요약) =====
style_prompt = """[요청]
다음 회의록을 요약해줘.

[회의록]
2025년 3월 10일 마케팅팀 주간 회의. 참석자: 김팀장, 이대리, 박사원.
김팀장이 신제품 런칭 일정이 4월 1일로 확정되었다고 공지함.
이대리가 SNS 광고 예산을 200만원에서 300만원으로 증액 요청, 승인됨.
박사원에게 경쟁사 분석 보고서를 3월 15일까지 작성하여 제출하도록 지시함.

[출력 형식]
- **주요 안건**: (한 줄 요약)
- **결정 사항**: (글머리 기호로 나열)
- **Action Item**: (담당자) - (할 일)"""

print("\n=== 출력 스타일 프리셋 ===")
response = client.models.generate_content(model="gemini-2.5-flash", contents=style_prompt)
print(response.text)
