import streamlit as st
import numpy as np
import pandas as pd
import osmnx as ox
import networkx as nx
from streamlit_folium import st_folium
import folium

st.markdown(
    '''
    # 체류시간별 추천코스 시각화
    -----
    ## 체류 7시간 추천코스(5개 경로)
    ### 코스: 부산신항 - 관광지1 - 관광지2 - 맛집1 - 부산신항
    1. 부산신항 - 감천문화마을 - 오륙도 스카이워크 - 생강나무 - 부산신항(2시간 33분)
    2. 부산신항 - 해동용궁사 - 오륙도 스카이워크 - 오오키니-부산신항(2시간 50분)
    3. 부산신항 - 오시리아 해안산책로 - 태종대유원지 - 할매복국 -부산신항(3시간 10분)
    4. 부산신항 - 역사의 디오라마 -  감천문화마을 - 새포항물회 - 부산신항(2시간 34분)
    5. 부산신항 - 용두산공원입구 - 역사의 디오라마- 에몽데 - 부산신항(2시간 24분)
'''
    )

# 부산신항 좌표
point=[35.078205, 128.832975]

# 1. 부산신항 - 감천문화마을 - 오륙도 스카이워크 - 생강나무 - 부산신항(2시간 33분)
@st.cache_data
def folium_gen_1_1():
# # 지역 설정
    busan = "부산광역시, 대한민국"
    targetPoint = ox.graph_from_point(point, network_type="drive",dist=15000)
    tour1 = [35.097486,129.0105996]  #관광지1
    tour2 = [35.0993277,129.1202127]  #관광지2
    food = [35.1071441,129.0387649]  #맛집

    port_Point=ox.distance.nearest_nodes(targetPoint,point[1],point[0])  #부산항 좌표
    tour1_Point = ox.distance.nearest_nodes(targetPoint, tour1[1], tour1[0]) #관광지1 좌표
    tour2_Point = ox.distance.nearest_nodes(targetPoint, tour2[1], tour2[0]) #관광지1 좌표
    food_Point = ox.distance.nearest_nodes(targetPoint, food[1], food[0]) #맛집 좌표

    route1=nx.shortest_path(targetPoint,port_Point,tour1_Point)  #부산항 - 관광지1 최단 경로
    route2=nx.shortest_path(targetPoint,tour1_Point,tour2_Point)  #관광지1- 관광지2 최단 경로
    route3= nx.shortest_path(targetPoint,tour2_Point,food_Point) #관광지2 - 맛집 최단 경로
    route4= nx.shortest_path(targetPoint,food_Point,port_Point) #맛집- 부산항 최단경로

    # 부산항 근처 2km 운전 도로망에 루트1, 2 표시
    # 파란색이 부산항 - 맛집
    # 붉은색이 맛집 호텔
    folium1=ox.plot_route_folium(targetPoint,route1,
                                 color='red')
    folium2=ox.plot_route_folium(targetPoint,route_map=folium1,
                                 route=route2,color='orange')
    folium3=ox.plot_route_folium(targetPoint,route_map=folium2,
                                 route=route3,color='yellow')
    folium4=ox.plot_route_folium(targetPoint,route_map=folium3,
                                 route=route4,color='blue')
    return folium4

st_folium(folium_gen_1_1(),use_container_width=True)