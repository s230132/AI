# 분류 모델 웹앱 만들기

import streamlit as st
import joblib
model = joblib.load('찐.pkl') 


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
     st.image('222222222222.png')
     st.write('시각화 자료 2')
a = st.number_input('총 플라스틱 폐기물(백만톤) ', value=0)
b = st.number_input(' 일인당 재활용률(%) ', value=0)
c = st.number_input(' 일인당 폐기물(kg)', value=0)

if st.button('입력확인'):              # 사용자가 '합불분류' 버튼을 누르면
        st.write('해안 생태계가 수많은 위협에 휩싸여 있습니다, 그 중 해안의 폐기물이 가장 큰 영향을 미칩니다. 각자의 폐기물의 양을 줄임으로 해안 폐기물로 인한 위험도를 낮춰주세요.')   
        input_data = [[ a ,b,c]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)      # model이 분류한 값을 p에 저장한다
        
        if p[0] == 1 or p[0] == 0 :
              st.success('(매우) 위험 등급입니다.')
              st.write('플라스틱 배달용기 사용을 자제하고, 스테인리스 빨대 등을 사용해 불필요한 생활 플라스틱을 줄이는 것이 도움이 된므로 더 노력하세요!') 
        if p[0] == 2 :
              st.success('중간 등급입니다.')          
              st.write('쓰레기섬 랜드마크가 오픈했어요! 당신이 만든 쓰레기들이 섬을 이뤘군요! ') 
        if p[0] == 3 :
              st.success('낮음 등급입니다.')
    
     
     

# 1. 기계학습 모델 파일 로드


# 2. 모델 설명
 

# 3. 데이터시각화


# 4. 모델 활용
