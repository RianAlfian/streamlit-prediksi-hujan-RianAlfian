import pickle
import streamlit as st

# membaca model
seattleWeather_model =  pickle.load(open('seattleWeather.sav', 'rb'))

#Judul Web
st.title('Data Mining Prediksi Hujan')

PRCP = st.text_input('Jumlah presipitasi dalam inci')

TMAX = st.text_input('Suhu maksimum dalam derajat Fahrenheit')

TMIN = st.text_input('Suhu minimum dalam derajat Fahrenheit')

# code untuk diagnosis hujan
hujan_prediksi = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi'):
    hujan_prediction = seattleWeather_model.predict([[PRCP, TMAX, TMIN]])
    
    if(hujan_prediction[0] == 1):
        hujan_prediksi = 'Hujan'
    else :
        hujan_prediksi = 'Tidak hujan'

    st.success(hujan_prediksi)
