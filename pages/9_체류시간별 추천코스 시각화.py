import streamlit as st
import numpy as np
import pandas as pd
import osmnx as ox
import networkx as nx
from streamlit_folium import st_folium
import folium

st.markdown(
    '''
    ## 체류 7시간 추천코스(5개 경로)
    -----
    ### 코스: 부산신항 - 관광지1 - 관광지2 - 맛집1 - 부산신항
    1. 부산신항 - 감천문화마을 - 오륙도 스카이워크 - 생강나무 - 부산신항(2시간 33분)
    2. 부산신항 - 해동용궁사 - 오륙도 스카이워크 - 오오키니-부산신항(2시간 50분)
    3. 부산신항 - 오시리아 해안산책로 - 태종대유원지 - 할매복국 -부산신항(3시간 10분)
    4. 부산신항 - 역사의 디오라마 -  감천문화마을 - 새포항물회 - 부산신항(2시간 34분)
    5. 부산신항 - 용두산공원입구 - 역사의 디오라마- 에몽데 - 부산신항(2시간 24분)
'''
    )