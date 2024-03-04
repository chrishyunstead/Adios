import streamlit as st
import glob

st.title('품목별 워드 클라우드')
st.markdown('''
-----
''')
img_list=glob.glob('img/*워드클라우드.png')

keyword=[]
for i in img_list:
    keyword.append(i.split('/')[1].split(' ')[0])

select_keyword=st.selectbox('품목 키워드 선택',keyword)

def img_gen():
    for i in img_list:
        if select_keyword in i:
            img=i
        else: pass
    return img

st.image(img_gen(),use_column_width=True)