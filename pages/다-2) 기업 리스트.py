import streamlit as st
import numpy as np
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import st_folium

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

def folium_gen():
    # 지도 생성
    map = folium.Map(location=[37.5502, 126.982], zoom_start=7)

    # 각 카테고리별로 마커 클러스터 관리를 위한 딕셔너리 생성
    category_marker_clusters = {}

    # 카테고리에 따라 색상을 지정
    colors = {
        '육류': 'red',
        '식품': 'blue',
        '주류': 'green',
        '기타': 'purple'
    }

    # cate 데이터프레임에 대한 마커 생성
    for index, row in company_selected_type.iterrows():
        category = row['카테고리']
        tooltip = \
            f"카테고리: {row['카테고리']}<br>회사명: {row['회사명']}<br>주소: {row['주소']}<br>전화번호: {row['전화번호']}"
        
        if category not in category_marker_clusters:
            category_marker_clusters[category] = MarkerCluster().add_to(map)
        
        folium.Marker([row['lat'], row['lng']], tooltip=tooltip, icon=folium.Icon(color='blue'))\
            .add_to(category_marker_clusters[category])
    return map

st_folium(folium_gen())