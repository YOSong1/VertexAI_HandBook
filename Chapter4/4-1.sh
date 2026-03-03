#!/bin/bash
# Chapter 4 실습: 개발 환경 구축 명령어 모음

# ===== 4-2 gcloud 기본 설정 =====

# gcloud CLI 버전 확인
gcloud --version

# 구글 계정 로그인 및 프로젝트 초기화
gcloud init

# ADC(Application Default Credentials) 설정
# -> Python 코드가 사용자 권한을 빌려 GCP에 접속할 수 있게 해주는 인증 파일 생성
gcloud auth application-default login

# ===== 4-3 Python 가상환경 및 라이브러리 설치 =====

# 가상환경 생성 (Windows)
# python -m venv venv
# .\venv\Scripts\activate

# 가상환경 생성 (macOS / Linux)
python3 -m venv venv
source venv/bin/activate

# Google Gen AI SDK 설치 (Vertex AI 통합 SDK)
pip install --upgrade google-genai

# 추가 유용 패키지 설치
pip install python-dotenv pandas
