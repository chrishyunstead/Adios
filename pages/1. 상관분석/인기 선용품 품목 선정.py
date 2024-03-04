import numpy as np
import pandas as pd
import streamlit as st

popular_ship_goods_18_df=pd.read_csv('data/18년도-선용품-품목.csv').drop('Unnamed: 0',axis=1)
st.dataframe(popular_ship_goods_18_df,use_container_width=True)