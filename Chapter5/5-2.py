# Chapter 5-3: ChatSession 패턴으로 멀티턴 대화 구현
# 용도: 이전 대화를 기억하는 챗봇 구현 (ChatSession 객체 활용)

from google import genai

# Google Gen AI 클라이언트 초기화
client = genai.Client(vertexai=True, project="your-project-id", location="us-central1")

# 1. 채팅 세션 시작 (history를 자동으로 관리함)
chat = client.chats.create(model="gemini-2.5-flash")
print("Gemini 챗봇과 대화를 시작합니다. (종료하려면 'quit' 입력)")

while True:
    # 사용자 입력 받기
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break

    # 2. 채팅 메시지 전송 (send_message 사용)
    response = chat.send_message(user_input)

    # 3. 모델 응답 출력
    print(f"Gemini: {response.text}")
    print("-" * 20)

# 대화 기록 확인
print("\n=== 대화 기록 ===")
for message in chat.history:
    role = message.role
    text = message.parts[0].text[:80]
    print(f"[{role}]: {text}...")
