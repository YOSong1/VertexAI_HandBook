from google import genai
from google.genai import types

# Google Gen AI 클라이언트 초기화
client = genai.Client(vertexai=True, project="your-project-id", location="us-central1")

# 1. 날씨 조회 함수
def get_current_weather(location: str):
    """지정된 도시의 현재 날씨를 조회합니다."""
    # 실제로는 API를 호출해야 하지만, 여기선 하드코딩
    if "서울" in location:
        return {"weather": "맑음", "temp": 25}
    elif "부산" in location:
        return {"weather": "비", "temp": 20}
    else:
        return {"weather": "흐림", "temp": 22}

# 2. 일정 조회 함수
def get_my_schedule(date: str):
    """특정 날짜의 사용자 일정을 조회합니다."""
    return ["오후 2시: 팀 미팅", "오후 6시: 헬스장"]
