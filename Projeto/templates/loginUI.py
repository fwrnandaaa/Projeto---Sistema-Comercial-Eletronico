import streamlit as st
from views import View

class LoginUI:
    def main():
        st.header("Entrar no Sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        
        if st.button("Entrar"):
            try:
                # Tenta autenticar como cliente primeiro
                cliente = View.cliente_autenticar(email, senha)
                if cliente is not None:
                    st.session_state["id_cliente"] = cliente["id"]
                    st.session_state["cliente_nome"] = cliente["nome"]
                    st.session_state["admin"] = cliente["admin"]
                    st.session_state["tipo_usuario"] = "admin" if cliente["admin"] else "usuario"
                    st.success("Login realizado com sucesso!")
                    st.rerun()
                else:
                    # Se não for cliente, tenta como entregador
                    entregador = View.entregador_autenticar(email, senha)
                    if entregador is not None:
                        st.session_state["entregador_id"] = entregador["id"]
                        st.session_state["entregador_nome"] = entregador["nome"]
                        st.session_state["tipo_usuario"] = "entregador"
                        st.success("Login como entregador realizado!")
                        st.rerun()
                    else:
                        st.error("E-mail ou senha inválidos")
            except Exception as e:
                st.error(f"Erro ao autenticar: {str(e)}")