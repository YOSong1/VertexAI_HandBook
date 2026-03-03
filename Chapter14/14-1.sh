#!/bin/bash
# Chapter 14 실습: Cloud Run 배포 명령어 모음
# 용도: 도커 이미지를 Artifact Registry에 푸시하고 Cloud Run에 배포하는 전체 과정

# ===== 14-2-1 Artifact Registry 저장소 생성 =====
gcloud artifacts repositories create my-repo \
  --repository-format=docker \
  --location=us-central1

# ===== 14-2-2 이미지 태깅 및 푸시 =====
# 1. 태그 붙이기 (주소 형식: 리전-docker.pkg.dev/프로젝트ID/저장소명/이미지명:태그)
docker tag vertex-rag-server:v1 \
  us-central1-docker.pkg.dev/my-project/my-repo/vertex-rag-server:v1

# 2. 업로드 (Push)
docker push us-central1-docker.pkg.dev/my-project/my-repo/vertex-rag-server:v1

# ===== 14-2-3 Cloud Run 서비스 배포 =====
gcloud run deploy vertex-rag-service \
  --image us-central1-docker.pkg.dev/my-project/my-repo/vertex-rag-server:v1 \
  --region us-central1 \
  --allow-unauthenticated

# ===== 14-4-1 Streamlit 앱 배포 (Cloud Build 사용) =====
# Google Cloud Build로 빌드 + 푸시를 한 번에 처리
gcloud builds submit \
  --tag us-central1-docker.pkg.dev/my-project/my-repo/streamlit-ui:v1 .
