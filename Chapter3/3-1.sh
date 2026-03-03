#!/bin/bash
# Chapter 3 실습: GCP 프로젝트 및 환경 설정 명령어 모음

# ===== 3-1 프로젝트 관리 =====

# 프로젝트 삭제 (30일 유예기간 후 영구 삭제)
# gcloud projects delete PROJECT_ID

# 프로젝트 복구 (삭제 후 30일 이내)
# gcloud projects undelete PROJECT_ID

# ===== 3-4 API 활성화 및 할당량 확인 =====

# Vertex AI API 활성화
gcloud services enable aiplatform.googleapis.com

# 활성화된 API 목록 확인
gcloud services list --enabled

# 할당량 확인 (콘솔에서 IAM 및 관리자 > 할당량 및 시스템 한도 > Generative AI API 검색)
