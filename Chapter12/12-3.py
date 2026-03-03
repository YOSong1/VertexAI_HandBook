@st.cache_resource
def get_rag_backend():
    return RAGBackend() # 벡터 DB 로드

rag = get_rag_backend()
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    project="your-project-id"
)  # Gemini 모델 설정
