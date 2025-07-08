import streamlit as st
from views import View
import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        
        if st.button("Entrar"):
            try:
                cliente = View.cliente_autenticar(email, senha)
                if cliente is None:
                    st.error("E-mail ou senha inválidos")
                else:
                    st.session_state["cliente_id"] = cliente["id"]
                    st.session_state["cliente_nome"] = cliente["nome"]
                    st.session_state["admin"] = cliente["admin"]
                    st.success("Login realizado com sucesso!")
                    st.rerun()
            except Exception as e:
                st.error(f"Erro ao autenticar: {str(e)}")