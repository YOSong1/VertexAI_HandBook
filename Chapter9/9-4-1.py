# Chapter 9-4: RAG 기반 질의응답 체인 구현
# 용도: create_retrieval_chain + create_stuff_documents_chain 패턴으로 RAG QA 구현

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# Chapter 8에서 만든 벡터 DB 클래스 임포트 (파일이 분리되어 있다고 가정)
# from rag_backend import RAGBackend
# 실습 편의상 여기서는 직접 vector_store를 로드한다고 가정합니다.


# 1. LLM 설정 (Gemini Pro)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    temperature=0,
    project="your-project-id"
)

# 2. 프롬프트 템플릿 설정 (ChatPromptTemplate 사용)
system_prompt = """당신은 기업 내부 문서를 기반으로 답변하는 전문 어시스턴트입니다.
반드시 아래의 [Context]에 있는 내용만을 바탕으로 답변하세요.
만약 문맥에서 답을 찾을 수 없다면 "문서에 해당 내용이 없습니다"라고 답하세요.

[Context]
{context}"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# 3. 체인 생성 (최신 LCEL 패턴)
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(
    rag_backend.vector_store.as_retriever(search_kwargs={"k": 3}),  # Ch8의 검색기
    question_answer_chain
)

def ask_question(query):
    # 체인 실행 (input 키 사용)
    result = rag_chain.invoke({"input": query})

    # 결과 파싱 (answer 키와 context 키)
    answer = result["answer"]
    sources = result["context"]  # 검색된 Document 리스트

    # 출력
    print(f"\n[질문]: {query}")
    print(f"[답변]: {answer}")
    print("-" * 30)
    print("[참고 문서]")
    for doc in sources:
        source_name = doc.metadata.get('source', 'Unknown')
        page_num = doc.metadata.get('page', 0)
        print(f"- {source_name} (p.{page_num})")


ask_question("RAG 파이프라인 구축 시 주의할 점은?")
