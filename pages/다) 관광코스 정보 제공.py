import streamlit as st
import numpy as np
st.image('img/나).png')
st.markdown(
    '''
        ### 1. 위 이미지 내용 중 여행/숙박 코스 추천서비스 관련하여, 해당 서비스 대상을 해외 선사에 탑승한 외국인 선원으로 선정하였음.
        ### 2. 외국인 선원의 체류시간 파악을 위해 가-2) 화물처리실적-체류시간 상관분석 을 위해 수집한 부산항 체류시간 데이터를 활용함.
    '''
)
col1, col2= st.columns(['이미지:describe', '연도별 평균체류시간'])
with col1:
    st.image('img/stayed_time_describe.png',use_column_width=True)
with col2:
    st.image('img/yearly_stayed_time_mean.png',use_column_width=True)