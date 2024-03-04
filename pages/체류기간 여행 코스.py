import streamlit as st
import numpy as np
import pandas as pd



restaurant_df_raw=pd.read_excel('data/평점 4이상 맛집리스트.xlsx').drop('Unnamed: 0',axis=1)
hotel_df_raw=pd.read_excel('data/평점 4이상 숙박업소.xlsx').drop('Unnamed: 0',axis=1)

busanport_coord=[35.1029191, 129.0407161]
@st.cache_data
def base_osmnx_gen():
    G=ox.graph_from_point(busanport_coord,network_type='all',dist=5000)
    return G

restaurant_type_list=list(set(restaurant_df_raw['구분']))
restaurant_type_selet=st.selectbox('식당 분류 선택',restaurant_type_list)
restaurant_df=restaurant_df_raw.query(f"구분=={str(restaurant_type_selet)}")
st.dataframe(restaurant_df)
restaurant_df_selected=st.selectbox('식당 선택',restaurant_df_raw['가게명'])

hotel_type_list=list(set(hotel_df_raw['구분']))
hotel_type_select=st.selectbox('호텔 등급 선택',hotel_type_list)
hotel_df=hotel_df_raw.query(f"구분=={str(hotel_type_list)}")

G1=base_osmnx_gen()
busan_port=ox.didstance.nearest_nodes(G1,
                                      busanport_coord[1],
                                      busanport_coord[0])

