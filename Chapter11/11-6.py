# 채팅 세션 생성 (도구가 포함된 설정 전달)
chat = client.chats.create(
    model="gemini-2.5-pro",
    config=config
)

# 질문: 복합적인 추론이 필요한 질문
query = "나 오늘 서울에 있는데, 오후에 야외 운동 해도 될까? 내 일정 확인해서 알려줘."

response = chat.send_message(query)

# Gemini가 함수 호출을 요청했는지 확인
function_calls = response.function_calls
if function_calls:
    for fc in function_calls:
        name = fc.name
        args = fc.args
        print(f"🤖 Gemini가 함수 호출을 요청함: {name}({args})")

        # 실제 함수 실행 (매핑 로직 필요)
        if name == "get_current_weather":
            api_result = get_current_weather(args["location"])
        elif name == "get_my_schedule":
            api_result = get_my_schedule("today")  # 날짜 파싱은 생략

        # 결과를 다시 모델에게 전달 (FunctionResponse 사용)
        print(f"📡 API 결과 전송: {api_result}")
        response = chat.send_message(
            types.Part.from_function_response(
                name=name,
                response={"content": api_result}
            )
        )

# 최종 답변 출력
print(f"🏁 최종 답변: {response.text}")
