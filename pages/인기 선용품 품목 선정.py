import numpy as np
import pandas as pd
import plotly.express as px
import glob
import streamlit as st

file_list_18=glob.glob('data/2018.*')
df_list=[]
for i in file_list_18:
    df=pd.read_csv(i)
    df['년도']=2018
    df['분기']=i[10:13]
    df_list.append(df)

popular_ship_goods_df_18=pd.concat(df_list).sort_values('년도').reset_index().drop('index',axis=1)
st.dataframe(popular_ship_goods_df_18,use_container_width=True)