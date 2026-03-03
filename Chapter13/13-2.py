# 1. 베이스 이미지 선택: Python 3.10이 설치된 가벼운 리눅스(Slim) 사용
FROM python:3.10-slim

# 2. 작업 디렉토리 설정: 컨테이너 내부의 작업 공간을 /app으로 지정
WORKDIR /app

# 3. 의존성 파일 복사 및 설치
# (캐시 효율을 위해 소스코드보다 먼저 복사함)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. 소스 코드 전체 복사
COPY . .

# 5. 환경 변수 설정 (옵션)
# 파이썬 출력이 버퍼링 없이 즉시 로그에 찍히도록 설정
ENV PYTHONUNBUFFERED=1

# 6. 포트 개방 알림 (문서화 목적)
EXPOSE 8080

# 7. 컨테이너 실행 시 작동할 명령어 (Uvicorn으로 FastAPI 실행)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]