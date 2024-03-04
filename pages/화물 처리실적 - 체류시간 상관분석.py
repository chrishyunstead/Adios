import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats

st.title('화물처리실적-체류시간 상관분석')
ship_stayed_df=pd.read_csv('data/처리실적-체류시간_상관분석.csv').drop('Unnamed: 0',axis=1)
ship_stayed_df.rename(columns={'컨테이너':'물동량'},inplace=True)
st.dataframe(ship_stayed_df,use_container_width=True)

scaler=MinMaxScaler()
ship_stayed_scaled=pd.DataFrame(
    scaler.fit_transform(ship_stayed_df.copy()),
    columns=ship_stayed_df.columns
)
ship_stayed_scaled.index=ship_stayed_df.index
ship_stayed_scaled.reset_index(inplace=True)

def ts_plotly_gen():
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=ship_stayed_scaled['년도'],
                             y=ship_stayed_scaled['물동량'],
                             name='물동량'))
    fig.add_trace(go.Scatter(x=ship_stayed_scaled['년도'],
                             y=ship_stayed_scaled['체류시간'],
                             name='체류시간'))
    fig.update_layout(
        title='연간 물동량, 체류시간 추이',
        xaxis=dict(title='년도'),
        annotations=[
            dict(x=-0.03,
                y=1.15,
                xref='paper',
                yref='paper',
                text='(모든 수치는 정규화된 수치임)',
                showarrow=False)])
    return fig

st.plotly_chart(ts_plotly_gen())