# AlfaProvas - Aplicação Principal

import streamlit as st
from auth import login
from provas import painel_professor, painel_aluno

st.set_page_config(page_title='AlfaProvas', layout='centered')

user, role = login()

if user:
    st.success(f'Bem-vindo, {user}!')
    if role == 'professor':
        painel_professor()
    elif role == 'aluno':
        painel_aluno()
else:
    st.warning('Por favor, faça login para acessar o sistema.')
