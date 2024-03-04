import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
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

