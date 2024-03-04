import streamlit as st
import numpy as np
import pandas as pd
import osmnx as ox
import networkx as nx
from streamlit_folium import st_folium
import folium

restaurant_df_raw=pd.read_excel('data/평점 4이상 맛집리스트.xlsx').drop('Unnamed: 0',axis=1)
hotel_df_raw=pd.read_excel('data/평점 4이상 숙박업소.xlsx').drop('Unnamed: 0',axis=1)
hotel_df_raw['구분'][50]='호텔'

restaurant_type_list=list(set(restaurant_df_raw['구분']))
restaurant_type_selet=st.selectbox('식당 분류 선택',restaurant_type_list)
restaurant_df=restaurant_df_raw.query(f"구분=='{restaurant_type_selet}'")\
    .reset_index().drop('index',axis=1)
st.dataframe(restaurant_df,use_container_width=True)
restaurant_select=st.selectbox('식당 선택',restaurant_df['가게명'])
restaurant_selected_df=restaurant_df.query(f"가게명=='{restaurant_select}'")\
    .reset_index().drop('index',axis=1)

hotel_type_list=list(set(hotel_df_raw['구분']))
hotel_grade_select=st.selectbox('호텔 등급 선택',hotel_type_list)
hotel_df=hotel_df_raw.query(f"구분=='{hotel_grade_select}'")\
    .reset_index().drop('index',axis=1)
st.dataframe(hotel_df,use_container_width=True)
hotel_select=st.selectbox('호텔 선택',hotel_df['업소명'])
hotel_selected_df=hotel_df.query(f"업소명=='{hotel_select}'")\
    .reset_index().drop('index',axis=1)


# 부산 신항 좌표
busanport_coord=[35.078205, 128.832975]

restaurant_coord=[restaurant_selected_df['lat'][0],
                  restaurant_selected_df['lng'][0]]
hotel_coord=[hotel_selected_df['lat'][0],hotel_selected_df['lng'][0]]

def base_osmnx_gen():
    G=ox.graph_from_point(busanport_coord,network_type='all',dist=7000)
    return G

@st.cache_resource
def osmnx_gen():
    target_point=ox.graph_from_point(busanport_coord,network_type='all',dist=7000)
    busan_port_point=\
        ox.distance.nearest_nodes(target_point,
                                  busanport_coord[1],busanport_coord[0])
    restaurant_point=\
        ox.distance.nearest_nodes(target_point,
                                  restaurant_coord[1],restaurant_coord[0])
    hotel_point=\
        ox.distance.nearest_nodes(target_point,
                                  hotel_coord[1],hotel_coord[0])

    route1=nx.shortest_path(target_point,busan_port_point,restaurant_point)
    route2=nx.shortest_path(target_point,restaurant_point,hotel_point)
    
    folium_final=ox.plot_graph_folium(target_point,color=None,zoom=5)
    folium_1=ox.plot_route_folium(target_point,route=route1,
                                  route_map=folium_final,
                                  popup_attribute='length',
                                  color='blue')
    folium_2=ox.plot_route_folium(target_point,route=route2,
                                route_map=folium_final,
                                popup_attribute='length',
                                color='red')
    
    return(folium_final)

folium=osmnx_gen()
st_folium(folium,width=2000,height=1500)