import streamlit as st
from views import View

class AbrirContaUI:
    def entregador_conta():
        st.header("Criar Nova Conta Como Entregador")
        nome = st.text_input("Informe seu nome", key="entregador_nome")
        email = st.text_input("Informe seu e-mail", key="entregador_email")
        fone = st.text_input("Informe seu telefone", key="entregador_fone")
        senha = st.text_input("Informe seu senha", type="password", key="entregador_senha")
        if st.button("Cadastrar como cliente"):
            st.session_state.tipo_conta = "cliente"
            c =  AbrirContaUI.cliente_conta()
            st.rerun()
        
        if st.button("Confirmar"):
                # Verifica se o email já está cadastrado
                clientes = View.cliente_listar()
                entregadores = View.entregadores_listar()
                email_existente = any(cliente.get_email() == email for cliente in clientes) or any(entregador.get_email() == email for entregador in entregadores)
                
                if email_existente:
                    st.error("Este e-mail já está cadastrado")
                else: 
                    c = View.entregador_inserir(nome, email, fone, senha)
                    st.success("Entregador cadastrado com sucesso!")

             
    def cliente_conta():
        st.header("Criar Nova Conta Como Cliente")
        nome = st.text_input("Informe seu nome", key="cliente_nome")
        email = st.text_input("Informe seu e-mail", key="cliente_email")
        fone = st.text_input("Informe seu telefone", key="cliente_fone")
        senha = st.text_input("Informe seu senha", type="password", key="cliente_senha")
        if st.button("Cadastrar como entregador"):
            st.session_state.tipo_conta = "entregador"
            c = AbrirContaUI.entregador_conta()
            st.rerun()
        
        if st.button("Confirmar"):
                # Verifica se o email já está cadastrado
                clientes = View.cliente_listar()
                entregadores = View.entregadores_listar()
                email_existente = any(cliente.get_email() == email for cliente in clientes) or any(entregador.get_email() == email for entregador in entregadores)
                
                if email_existente:
                    st.error("Este e-mail já está cadastrado")
                else: 
                    c = View.cliente_inserir(nome, email, fone, senha)
                    st.success("Cliente cadastrado com sucesso!")

    def main():
        if "tipo_conta" not in st.session_state:
            st.session_state.tipo_conta = None

        # Exibir botões apenas se nenhum tipo foi escolhido
        if st.session_state.tipo_conta is None:
            st.header("Criar Nova Conta!")
            if st.button("Criar Conta Como Cliente"):
                st.session_state.tipo_conta = "cliente"
                st.rerun()
            if st.button("Criar Conta Como Entregador"):
                st.session_state.tipo_conta = "entregador"
                st.rerun()
        # Agora renderiza a UI com base na escolha do usuário
        if st.session_state.tipo_conta == "cliente":
            AbrirContaUI.cliente_conta()
        elif st.session_state.tipo_conta == "entregador":
            AbrirContaUI.entregador_conta()
