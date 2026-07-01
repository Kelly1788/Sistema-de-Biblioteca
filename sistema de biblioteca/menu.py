import streamlit as st
from funcoes import *

def menu():
    
    if "biblioteca" not in st.session_state:
        st.session_state.biblioteca = carregar_dados()

    st.title("📚 Sistema de Biblioteca")


    op = st.sidebar.selectbox(
        "Escolha uma opção",
        ["Listar livros", "Adicionar livro", "Buscar livro", "Atualizar livro", "Remover livro"]
    )

    if op == "Adicionar livro":
        adicionar_livro(st.session_state.biblioteca)
        
    elif op == "Listar livros":
        lista(st.session_state.biblioteca)
        
    elif op == "Buscar livro":
        buscar(st.session_state.biblioteca)
        
    elif op == "Atualizar livro":
        atualizar(st.session_state.biblioteca)
        
    elif op == "Remover livro":
        remover(st.session_state.biblioteca)

menu()