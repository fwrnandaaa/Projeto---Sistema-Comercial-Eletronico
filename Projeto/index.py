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
        elif op == "Sair":
          
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
            
    def menu_usuario():
           op = st.sidebar.selectbox("Menu", ["Listar minhas compras", "Comprar novamente", "Listar produtos","Inserir produto no carrinho", "Visualizar o carrinho", "Confirmar a compra", "Sair"])
           if op == "Listar minhas compras": ListarComprasUI.main()
           if op == "Listar produtos": ListarProdutoUI.main()
    
           elif op == "Sair":
            
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()
    def menu_entregador():
        op = st.sidebar.selectbox("Menu", ["Listar minhas entregas", "Confirmar entrega", "Sair"])
        if op == "Listar minhas entregas":
            
            pass
        elif op == "Confirmar entrega":
           
            pass
        elif op == "Sair":
            
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
        
    @staticmethod
    def main():
        if "tipo_usuario" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            if st.session_state["tipo_usuario"] == "admin":
                IndexUI.menu_admin()
            elif st.session_state["tipo_usuario"] == "usuario":
                IndexUI.menu_usuario()
            elif st.session_state["tipo_usuario"] == "entregador":
                IndexUI.menu_entregador()

    # ... (mantenha os outros métodos igual)
View.cadastrar_admin()

IndexUI.main()