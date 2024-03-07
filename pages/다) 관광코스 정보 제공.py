import streamlit as st
import numpy as np

col1, col2= st.columns(['이미지:describe', '연도별 평균체류시간'])
with col1:
    st.image('img/stayed_time_describe.png')
with col2:
    st.image('imp/yearly_stayed_time_mean.png')
st.markdown('''### 3. 년도별 체류시간의 집계를 위해, 데이터 전처리 후 describe() 함수를 적용하여 최소/최대/평균 체류시간을 분석했음.''')