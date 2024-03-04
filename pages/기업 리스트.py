import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(layout='wide')
st.title('업종별 기업 리스트 소싱')
company_list_df=pd.read_excel('data/기업엑셀화.xlsx').drop('Unnamed: 0',axis=1)
for i in list(company_type_list.index):
    if company_list_df['업종'][i] in ['과자류','당류','초콜릿 도매업','빵류','낙농품 및 동ㆍ식물성 유지 도매업','수산물 가공식품 도매업','기타 가공식품 도매업']:
        company_list_df['대분류'][i]='식품'
    elif company_list_df['업종'][i] in ['육류 가공식품 도매업','육류 도매업']:
        company_list_df['대분류'][i]='육류'
    elif company_list_df['업종'][i]=='주류 도매업':
        company_list_df['대분류'][i]='주류'
    else:
        company_list_df['대분류'][i]='기념품'
company_type_list=list(set(company_list_df['대분류']))
company_type=st.multiselect('업종 선택',
                            company_type_list)
company_selected_type=company_list_df.query(f'대분류 in {company_type}').reset_index().drop('index',axis=1)
st.dataframe(company_selected_type,
             use_container_width=True)
download_df=company_selected_type.to_csv().encode('utf-8-sig')

st.download_button(
    label='다운로드',
    data=download_df,
    file_name='기업 리스트.csv',
    mime='text/csv'
)