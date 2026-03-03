import streamlit as st
from rag_backend import RAGBackend # Ch8에서 만든 백엔드 클래스
from langchain_google_genai import ChatGoogleGenerativeAI

# 페이지 기본 설정 (탭 이름, 아이콘 등)
st.set_page_config(page_title="Vertex AI RAG Chatbot", page_icon="🤖")
st.title("🤖 나만의 AI 문서 비서")
