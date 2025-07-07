import streamlit as st
from views import View
from templates.mantercategoria import ManterCategoriaUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.loginUI import LoginUI

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        #if op == "Abrir Conta": AbrirContaUI.main()
if __name__ == "__main__":
    IndexUI.menu_visitante()