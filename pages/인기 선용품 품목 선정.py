import numpy as np
import pandas as pd
import streamlit as st

popular_ship_goods_18_df=pd.read_csv('data/2018년도 분기별 품목 합.csv').drop('Unnamed: 0',axis=1)
st.dataframe(popular_ship_goods_18_df,use_container_width=True)
