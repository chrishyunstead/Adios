import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats

ship_stayed_df=pd.read_csv('data/처리실적-체류시간_상관분석.csv').drop('Unnamed: 0',axis=1)
st.dataframe(ship_stayed_df,use_container_width=True)