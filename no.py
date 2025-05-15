import streamlit as st

st.title ('Hitung luas persegi panjang')

panjang = st.number_input ("Masukkan nilai panjang", 0)
lebar = st.number_input ("Masukkan nilai lebar", 0)
hitung = st.button ("Luas persegi panjang")

if hitung :
    luas = panjang * lebar
    st.write ("Luas persegi panjang adalah = ", luas)
