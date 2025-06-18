import streamlit as st
from ui import UI

class TelaInicial:
    def main():
        st.title("Tela Inicial do Sistema Comercial Eletrônico")
        st.write("Bem-vindo ao sistema! Selecione uma opção abaixo para continuar:")

        num = st.number_input("Digite um número")
        st.write(f"Você digitou: {num}")

        