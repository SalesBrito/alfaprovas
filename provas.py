# Módulo de provas
import streamlit as st

def painel_professor():
    st.header('Painel do Professor')
    uploaded_file = st.file_uploader('Enviar prova (PDF ou imagem)')
    if uploaded_file:
        st.success('Prova enviada com sucesso!')
        st.write('Nome do arquivo:', uploaded_file.name)
        st.image(uploaded_file)
    gabarito = st.text_input('Gabarito (ex: ABCDA)')
    if st.button('Corrigir Provas'):
        st.success('Correção realizada com sucesso (simulado).')

def painel_aluno():
    st.header('Painel do Aluno')
    st.text_input('Nome do aluno')
    respostas = st.text_input('Respostas (ex: ABCDB)')
    if st.button('Enviar Respostas'):
        st.success('Respostas enviadas com sucesso (simulado).')
