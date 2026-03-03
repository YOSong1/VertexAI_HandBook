# Chapter 7-3: 문서 청킹 파이프라인 구현
# 용도: PDF 문서를 로드하고 RecursiveCharacterTextSplitter로 청킹하는 전체 파이프라인

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# ===== 7-3-1 환경 설정 =====
# 실습할 PDF 파일 경로 지정 (프로젝트 폴더에 PDF 파일을 미리 넣어두세요)
FILE_PATH = "./sample_data/vertex_guide.pdf"

# ===== 7-3-2 문서 로드 및 텍스트 분할기 설정 =====

# 1. 문서 로드 (PyPDFLoader: 텍스트 위주의 간단한 PDF에 적합)
loader = PyPDFLoader(FILE_PATH)
documents = loader.load()
print(f"총 페이지 수: {len(documents)}")

# 2. 분할기(Splitter) 설정
# RecursiveCharacterTextSplitter: 문단 → 문장 → 단어 순서로 의미 단위가 깨지지 않도록 자름
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,     # 청크 당 약 500자 (권장: 500~1000자)
    chunk_overlap=50,   # 50자 정도 겹치게 설정 (10~20% 슬라이딩 윈도우)
    separators=["\n\n", "\n", " ", ""]  # 자르는 우선순위
)

# 3. 문서 분할 실행
split_docs = text_splitter.split_documents(documents)
print(f"분할된 총 청크 수: {len(split_docs)}")

# ===== 7-3-3 분할 결과 확인 =====

# 첫 번째 청크의 내용과 메타데이터 확인
first_chunk = split_docs[0]
print("\n=== 첫 번째 청크 내용 ===")
print(first_chunk.page_content)
print("\n=== 메타데이터 ===")
print(first_chunk.metadata)
# metadata에 {'source': ..., 'page': ...} 정보가 자동으로 포함됨
