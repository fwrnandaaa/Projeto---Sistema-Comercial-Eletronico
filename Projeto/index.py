import streamlit as st
from views import View
from templates.mantercategoria import ManterCategoriaUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.loginUI import LoginUI
from templates.listarcomprasUI import ListarComprasUI
from templates.AbrirContaUI import AbrirContaUI
from templates.listarProduto import ListarProdutoUI


class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()
    
    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Manter Categorias", "Manter Clientes", "Manter Produtos", "Sair"])
        if op == "Manter Categorias": ManterCategoriaUI.main()
        if op == "Manter Clientes": ManterClienteUI.main()
        if op == "Manter Produtos": ManterProdutoUI.main()
        if op == "Sair": 
            del st.session_state["cliente_id"]
            del st.session_state["cliente_nome"]
            del st.session_state["admin"]
            st.rerun()
            
    def menu_usuario():
           op = st.sidebar.selectbox("Menu", ["Listar minhas compras", "Comprar novamente", "Listar produtos","Inserir produto no carrinho", "Visualizar o carrinho", "Confirmar a compra", "Sair"])
           if op == "Listar minhas compras": ListarComprasUI.main()
           if op == "Listar produtos": ListarProdutoUI.main()
    
           if op == "Sair": 
               del st.session_state["cliente_id"]
               del st.session_state["cliente_nome"]
               del st.session_state["usuario"]
               st.rerun()
    def menu_entregador():
          op = st.sidebar.selectbox("Menu", ["Listar minhas entregas","Confirmar entrega", "Sair"])

        
    @staticmethod
    def main():
        if "cliente_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            if "admin" in st.session_state and st.session_state["admin"]:
                IndexUI.menu_admin()
            else:
                IndexUI.menu_usuario()

View.cadastrar_admin()

IndexUI.main()