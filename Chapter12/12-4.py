# 1. 세션 스테이트 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 2. 이전 대화 내용 화면에 출력 (History)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 3. 사용자 입력 처리
if prompt := st.chat_input("궁금한 점을 물어보세요!"):
    # 사용자 메시지 표시 및 저장
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # AI 답변 생성 과정
    with st.chat_message("assistant"):
        message_placeholder = st.empty() # 답변이 들어갈 빈 공간
        
        # RAG 검색 수행 (Ch8 기능)
        docs = rag.retrieve_documents(prompt)
        context_text = "\n".join([doc.page_content for doc in docs])
        
        # 프롬프트 구성 및 Gemini 호출 (Ch9 기능 간소화)
        full_prompt = f"Context:\n{context_text}\n\nQuestion:\n{prompt}\nAnswer:"
        response = llm.invoke(full_prompt)
        
        # 답변 출력
        message_placeholder.markdown(response)
        
        # ★ 근거 문서(Expander) 보여주기
        with st.expander("참고 문서 확인하기"):
            for i, doc in enumerate(docs):
                st.info(f"📄 문서 {i+1} (p.{doc.metadata.get('page', '?')})\n{doc.page_content[:100]}...")

    # AI 메시지 저장
    st.session_state.messages.append({"role": "assistant", "content": response})