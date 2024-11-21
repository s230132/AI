# 분류 모델 웹앱 만들기

import streamlit as st
import joblib
model = joblib.load('logistic_regression_model.pkl') 


st.title('해안의 폐기물 위험 정도 평가')
st.subheader('우리나라의   해안 폐기물 위험 정도는 몇일까?')
st.write('우리나라의 총 플라스틱 배출량은 2.91(백만톤), 재활용률 59.1%, 일인당 폐기물 56.7kg로') 
st.write('중간 정도의 위험 정도를 나타낸다.') 

col1, col2 = st.columns(2)       
with col1:    
     st.image('시각화1.png')
     st.write('시각화 자료 1')
     st.image('brian_yurasits_y8k_dMPNWNI_unsplash.jpg')
     st.write('해안 쓰레기의 위험')
with col2:
     st.image('시각화2.png')
     st.write('시각화 자료 1')
a = st.number_input('촐 플라스틱 폐기물(백만톤) ', value=0)
b = st.number_input(' 일인당 폐기물(kg) ', value=0)
c = st.number_input(' 일인당 재활용률(%) ', value=0)

if st.button('입력확인'):              # 사용자가 '합불분류' 버튼을 누르면
        input_data = [[ a ],[b],[c]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)      # model이 분류한 값을 p에 저장한다
        if p[0] == 0 :
              st.success('매우 위험 등급입니다.')
        if p[0] == 1 :
              st.success('위험 등급입니다.')
        if p[0] == 2 :
              st.success('중간 등급입니다.')
        if p[0] == 3 :
              st.success('낮음 등급입니다.')
        
     
     

# 1. 기계학습 모델 파일 로드


# 2. 모델 설명
 

# 3. 데이터시각화


# 4. 모델 활용
