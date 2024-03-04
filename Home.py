import streamlit as st
from st_pages import Page,show_pages,add_page_title,Section

st.title('Adios Team Project\n부산항 입항 외국인 선원 대상 마케팅 인사이트 및 서비스 제공')
    
st.markdown(
    '''
    ### Update log
    -----
    * 페이지 업데이트
        - 인기 선용품 기업 리스트 소싱
'''
)

show_pages([
    Page('Adios/Home.py','Home'),
    Section(name='1. 상관분석'),
    Page('Adios/pages/연도별 물동량 변화 - Flourish.py',
         '연도별 물동량 변화'),  #추후 업데이트 예정
    Page('Adios/pages/물동량 - 화물처리실적 상관분석.py',
         '물동량 - 화물 처리량 상관분석'),
    Page('Adios/pages/화물 처리실적 - 체류시간 상관분석.py',
         '화물 처리량 - 체류시간 상관분석'),
    Section(name='2. 선용품 구매플랫폼 구축을 위한 데이터 분석'),
    Page('Adios/pages/인기 선용품 품목 선정.py',
         '선용품 팜매 품목 선정 분석')
])