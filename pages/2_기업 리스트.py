import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout='wide')
st.title('업종별 기업 리스트 소싱')
company_list_df=pd.read_csv('data/카테고리별 기업 리스트 최종본.csv').drop('Unnamed: 0',axis=1)
company_type_list=list(set(company_list_df['카테고리']))
company_type=st.multiselect('업종 선택',
                            company_type_list)
company_selected_type=company_list_df.query(f'카테고리 in {company_type}').reset_index().drop('index',axis=1)
st.dataframe(company_selected_type,
             use_container_width=True,
             height=600)
download_df=company_selected_type.to_csv().encode('utf-8-sig')

st.download_button(
    label='다운로드',
    data=download_df,
    file_name='기업 리스트.csv',
    mime='text/csv'
)