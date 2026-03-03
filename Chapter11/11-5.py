# 함수 선언부 정의 (Google Gen AI SDK 방식)
# Python 함수를 직접 도구로 전달 가능 (SDK가 JSON 스키마를 자동 생성)

# GenerateContentConfig에 tools로 함수 리스트 전달
# automatic_function_calling을 비활성화하여 수동 제어 가능
config = types.GenerateContentConfig(
    tools=[get_current_weather, get_my_schedule],
    automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)
)
