"""
Este script es un demo de como usar Streamlit
"""
import streamlit as st

st.title('Generador de números de la suerte')
st.text('Con esto podrás ganar la loteria')

edad = st.slider('Ingrese la edad',0,100)
altura = st.slider("Ingrese la altura en cm",10,200)


def mi_numero_suerte(v_edad,v_altura):
    """
    Esta función genera numeros de la suerte
    depende de la edad
    y de la altura
    Arg:
        v_edad (int): edad de la persona
        v_altura (int): altura en cms de la persona
    return:
        numero_ganador (float): numero de la suerte
    """
    numero_ganador = v_edad*v_altura/2 + 1000
    return numero_ganador

resultado = mi_numero_suerte(edad,altura)
st.header(f"Mi numero de la suerte es: {resultado}")
