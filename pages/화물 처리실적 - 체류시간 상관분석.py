import streamlit as st
import numpy as np
import pandas as pd
import plotly
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler
import scipy.stats as stats

st.title('연간 화물처리량-체류시간 상관분석')
ship_stayed_df=pd.read_csv('data/처리실적-체류시간_상관분석.csv').drop('Unnamed: 0',axis=1)
ship_stayed_df.rename(columns={'컨테이너':'화물처리량',
                               '체류시간_totalTime(시간)':'체류시간'},
                      inplace=True)
ship_stayed_df=ship_stayed_df.groupby('년도',as_index=False).sum()
st.dataframe(ship_stayed_df,use_container_width=True)

scaler=MinMaxScaler()
ship_stayed_df.set_index('년도',inplace=True)
ship_stayed_scaled=pd.DataFrame(
    scaler.fit_transform(ship_stayed_df.copy()),
    columns=ship_stayed_df.columns
)
ship_stayed_scaled.index=ship_stayed_df.index
ship_stayed_scaled.reset_index(inplace=True)

corr=stats.pearsonr(ship_stayed_scaled['화물처리량'],
                    ship_stayed_scaled['체류시간'])
st.write(f'상관계수 : {round(corr[0],3)}')
st.write(f'P-value : {round(corr[1],3)}')

def plotly_gen_corr():
    fig=go.Figure()
    fig.add_trace(go.Scatter(
        x=ship_stayed_scaled['화물처리량'],y=ship_stayed_scaled['체류시간'],
        name='실측값',mode='markers'
    ))
    fig.add_trace(go.Scatter(
        x=ship_stayed_scaled['화물처리량'],
        y=np.poly1d(np.polyfit(ship_stayed_scaled['화물처리량'],ship_stayed_scaled['체류시간'],1))\
            (ship_stayed_scaled['화물처리량']),
        mode='lines',line=dict(color='red'),name='추세선'
    ))
    fig.update_layout(title='연간 화물처리량 - 체류시간',
                    xaxis=dict(title='화물처리량'),
                    yaxis=dict(title='체류시간'),
                    annotations=[
                        dict(x=-0.02,
                            y=1.15,
                            xref='paper',
                            yref='paper',
                            text=f'상관계수 : {round(corr[0],3)}',
                            showarrow=False)])
    return fig
st.plotly_chart(plotly_gen_corr())

def ts_plotly_gen():
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=ship_stayed_scaled['년도'],
                             y=ship_stayed_scaled['화물처리량'],
                             name='화물처리량'))
    fig.add_trace(go.Scatter(x=ship_stayed_scaled['년도'],
                             y=ship_stayed_scaled['체류시간'],
                             name='체류시간'))
    fig.update_layout(
        title='연간 화물처리량, 체류시간 추이',
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