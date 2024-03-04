import streamlit as st
import numpy as np
import pandas as pd
import osmnx as ox
import networkx as nx


restaurant_df_raw=pd.read_excel('data/평점 4이상 맛집리스트.xlsx').drop('Unnamed: 0',axis=1)
hotel_df_raw=pd.read_excel('data/평점 4이상 숙박업소.xlsx').drop('Unnamed: 0',axis=1)

restaurant_type_list=list(set(restaurant_df_raw['구분']))
restaurant_type_selet=st.selectbox('식당 분류 선택',restaurant_type_list)
restaurant_df=restaurant_df_raw.query(f"구분=='{restaurant_type_selet}'")\
    .reset_index().drop('index',axis=1)
st.dataframe(restaurant_df)
restaurant_select=st.selectbox('식당 선택',restaurant_df['가게명'])
restaurant_selected_df=restaurant_df.query(f"가게명=='{restaurant_select}'")

hotel_type_list=list(set(hotel_df_raw['구분']))
hotel_grade_select=st.selectbox('호텔 등급 선택',hotel_type_list)
hotel_df=hotel_df_raw.query(f"구분=='{hotel_grade_select}'")\
    .reset_index().drop('index',axis=1)
st.dataframe(hotel_df)
hotel_select=st.selectbox('호텔 선택',hotel_df['업소명'])
hotel_selected_df=hotel_df.query(f"업소명=='{hotel_select}'")

busanport_coord=[35.1029191, 129.0407161]

def base_osmnx_gen():
    G=ox.graph_from_point(busanport_coord,network_type='drive',dist=5000)
    return ox.plot_graph(G,node_color='black',node_size=5,bgcolor='w')

def osmnx_gen():
    G1=base_osmnx_gen()
    restaurant_coord=[restaurant_selected_df['lat'],restaurant_selected_df['lng']]
    hotel_coord=[hotel_selected_df['lat'],hotel_selected_df['lng']]
    busan_port_point=ox.distance.nearest_nodes(G1,busanport_coord[1],busanport_coord[0])
    restaurant_point=ox.distance.nearest_nodes(G1,restaurant_coord[1],restaurant_coord[0])
    hotel_point=ox.distance.nearest_nodes(G1,hotel_coord[1],hotel_coord[0])

    route1=nx.shortest_path(G1,busan_port_point,restaurant_point)
    route2=nx.shortest_path(G1,restaurant_point,hotel_point)

    fig,ax=ox.plot_graph_routes(G1,[route1,route2],node_size=0.5,
                          edge_linewidth=0.5,edge_color='w',
                          route_colors=['blue','red'])
    return(fig)

base_osmnx_gen()
