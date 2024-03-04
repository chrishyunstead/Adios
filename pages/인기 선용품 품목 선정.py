import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus']=False
f_path='Font/경기천년바탕OTF_BOLD.OTF'
font_name=font_manager.FontProperties(fname=f_path).get_name()
st.write(f'{font_name}')
rc('font',family=font_name)

popular_ship_goods_18_df=pd.read_csv('data/2018년도 분기별 품목 합.csv')
popular_ship_goods_18_df['년도']=2018
popular_ship_goods_19_df=pd.read_csv('data/2019년도 분기별 품목 합.csv')
popular_ship_goods_19_df['년도']=2019
popular_ship_goods_20_df=pd.read_csv('data/2020년도 분기별 품목 합.csv')
popular_ship_goods_20_df['년도']=2020
popular_ship_goods_21_df=pd.read_csv('data/2021년도 분기별 품목 합.csv')
popular_ship_goods_21_df['년도']=2021
popular_ship_goods_22_df=pd.read_csv('data/2022년도 분기별 품목 합.csv')
popular_ship_goods_22_df['년도']=2022
popular_ship_goods_23_df=pd.read_csv('data/2023년도 분기별 품목 합.csv')
popular_ship_goods_23_df['년도']=2023

st.dataframe(popular_ship_goods_18_df,use_container_width=True)
title_list=['2018년도 1분기 선용품 품목',
            '2018년도 2분기 선용품 품목',
            '2018년도 3분기 선용품 품목',
            '2018년도 4분기 선용품 품목']
def plotly_gen():
    fig=make_subplots(rows=2,cols=2,column_titles=title_list)
    fig.add_trace(go.Bar(x=popular_ship_goods_18_df['품목'],
                             y=popular_ship_goods_18_df['2018.1분기'],
                             marker_color='#ffff00'),row=1,col=1)
    fig.add_trace(go.Bar(x=popular_ship_goods_18_df['품목'],
                             y=popular_ship_goods_18_df['2018.2분기'],
                             marker_color='#40e0d0'),row=1,col=2)
    fig.add_trace(go.Bar(x=popular_ship_goods_18_df['품목'],
                             y=popular_ship_goods_18_df['2018.3분기'],
                             marker_color='#ff6600'),row=2,col=1)
    fig.add_trace(go.Bar(x=popular_ship_goods_18_df['품목'],
                             y=popular_ship_goods_18_df['2018.4분기'],
                             marker_color='#7749f5'),row=2,col=2)
    fig.update_layout(width=1500,height=900)
    return fig

st.plotly_chart(plotly_gen())