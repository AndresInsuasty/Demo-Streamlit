import streamlit as st

st.title('Generador de numeros de la suerte')
st.text('Con esto podrás ganar la loteria')

edad = st.slider('Ingrese la edad',0,100)
altura = st.slider("Ingrese la altura en cm",10,200)


def mi_numero_suerte(edad,altura):
    numero_ganador = edad*altura/2 + 1000
    return numero_ganador

resultado = mi_numero_suerte(edad,altura)
st.header(f"Mi numero de la suerte es: {resultado}")