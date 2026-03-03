# 간단한 A/B 테스트 및 평가 의사코드
questions = ["질문1", "질문2", "질문3"]
prompt_a_results = []
prompt_b_results = []

for q in questions:
    ans_a = model.generate(prompt_a + q)
    ans_b = model.generate(prompt_b + q)
    
    # 평가용 LLM에게 두 답변을 비교하게 시킴
    eval_prompt = f"""
    질문: {q}
    답변 A: {ans_a}
    답변 B: {ans_b}
    
    어느 답변이 더 정확하고 친절한지 평가하고, 승자를 선택해줘.
    """
    verdict = evaluator_model.generate(eval_prompt)
    print(f"질문: {q} => 승자: {verdict}")