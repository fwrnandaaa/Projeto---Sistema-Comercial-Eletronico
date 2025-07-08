import streamlit as st
from views import View

class AbrirContaUI:
    def main():
        st.header("Criar Nova Conta")
        nome = st.text_input("Informe seu nome")
        email = st.text_input("Informe seu e-mail")
        fone = st.text_input("Informe seu telefone")
        senha = st.text_input("Informe sua senha", type="password")
        
        if st.button("Criar Conta"):
                # Verifica se o email já está cadastrado
                clientes = View.cliente_listar()
                email_existente = any(cliente.get_email() == email for cliente in clientes)
                
                if email_existente:
                    st.error("Este e-mail já está cadastrado")
                else:
                    try:
                        View.cliente_inserir(nome, email, fone, senha)
                        st.success("Conta criada com sucesso!")
                        st.write("Faça login para continuar")
                    except Exception as erro:
                        st.error(f"Erro ao criar conta: {erro}")