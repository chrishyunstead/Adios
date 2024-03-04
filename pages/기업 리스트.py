import streamlit as st
import numpy as np
import pandas as pd

st.title('업종별 기업 리스트 소싱')

company_list_df=pd.read_excel('data/기업엑셀화.xlsx').drop('Unnamed: 0',axis=1)
company_type_list=list(set(company_list_df['업종']))
company_type=st.multiselect('업종 선택',company_type_list)
company_selected_type=company_list_df.query(f'업종 in {company_type}').reset_index().drop('index',axis=1)
st.dataframe(company_selected_type)
download_df=company_selected_type.to_csv().encode('utf-8-sig')

st.download_button(
    label='다운로드',
    data=download_df,
    file_name='기업 리스트.csv',
    mime='text/csv'
)