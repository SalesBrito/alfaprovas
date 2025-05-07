# Módulo de autenticação
import streamlit as st

def login():
    st.title('AlfaProvas - Login')
    user = st.text_input('Usuário')
    pwd = st.text_input('Senha', type='password')
    if st.button('Entrar'):
        if user == 'professor' and pwd == 'alfa123':
            return user, 'professor'
        elif user == 'aluno' and pwd == 'prova123':
            return user, 'aluno'
        else:
            st.error('Usuário ou senha incorretos.')
    return None, None
