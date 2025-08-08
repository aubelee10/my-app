import streamlit as st
import pandas as pd

# 페이지 설정
st.set_page_config(
    page_title="성평등 영화 목록",
    page_icon="🎬",
    layout="wide"
)

# 제목
st.title("🎬 성평등 영화 목록")
st.markdown("### 성평등과 여성의 권리를 다룬 추천 영화 모음")

# 샘플 영화 데이터
movies_data = {
    "제목": [
        "그녀가 말했다",
        "우먼 토킹",
        "유망주",
        "더 라스트 듀얼",
        "프로미싱 영 우먼"
    ],
    "연도": [2022, 2022, 2020, 2021, 2020],
    "감독": [
        "마리아 슈라더",
        "사라 폴리",
        "키태 킨",
        "리들리 스콧",
        "에메랄드 페넬"
    ],
    "테마": [
        "미투운동, 언론과 정의",
        "종교 공동체와 성폭력",
        "스포츠계 성폭력",
        "중세시대 여성인권",
        "복수와 정의"
    ],
    "설명": [
        "할리우드의 성폭력 사건을 폭로한 여성 기자들의 용기 있는 이야기",
        "종교 공동체 내 성폭력 문제를 고발하고 맞서 싸우는 여성들의 이야기",
        "체조계의 성폭력 사건을 다룬 실화 기반 영화",
        "14세기 프랑스에서 일어난 실제 사건을 바탕으로 한 영화",
        "현대 사회의 성폭력 문제를 다룬 스릴러"
    ]
}

# 데이터프레임 생성
df = pd.DataFrame(movies_data)

# 사이드바 - 필터
st.sidebar.header("필터")

# 연도 필터
year_range = st.sidebar.slider(
    "연도 선택",
    min_value=int(df["연도"].min()),
    max_value=int(df["연도"].max()),
    value=(int(df["연도"].min()), int(df["연도"].max()))
)

# 테마 필터
themes = st.sidebar.multiselect(
    "테마 선택",
    options=df["테마"].unique(),
    default=[]
)

# 검색 기능
search_term = st.text_input("영화 제목 검색")

# 필터링 적용
mask = (
    (df["연도"].between(year_range[0], year_range[1]))
    & (df["제목"].str.contains(search_term, case=False))
)

if themes:
    mask = mask & (df["테마"].isin(themes))

filtered_df = df[mask]

# 결과 표시
st.subheader(f"검색 결과: {len(filtered_df)}개의 영화")

# 영화 목록 표시
for _, movie in filtered_df.iterrows():
    with st.expander(f"{movie['제목']} ({movie['연도']})"):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown("**감독**")
            st.write(movie["감독"])
            st.markdown("**테마**")
            st.write(movie["테마"])
        with col2:
            st.markdown("**설명**")
            st.write(movie["설명"])

# 푸터
st.markdown("---")
st.markdown("이 앱은 성평등 의식 향상을 위해 제작되었습니다.")
