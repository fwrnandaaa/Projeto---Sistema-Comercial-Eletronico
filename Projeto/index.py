import streamlit as st
from views import View
from templates.mantercategoria import ManterCategoriaUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterprodutoUI import ManterProdutoUI
from templates.loginUI import LoginUI
from templates.listarcomprasUI import ListarComprasUI
from templates.AbrirContaUI import AbrirContaUI
from templates.listarProduto import ListarProdutoUI
from templates.inserirprodutonocarrinhoUI import InserirProdutoCarrinhoUI
from templates.visualizarcarrinho import VisualizarCarrinhoUI
from templates.manterentregadores import ManterEntregadoresUI
from templates.EntregasEmAndamento import EntregasEmAndamentoUI
from templates.listarminhasentregasUI import MinhasEntregasUI
from templates.confirmarentrega import ConfirmarEntregasUI
from templates.comprarNovamente import ComprarNovamenteUI

class IndexUI:
    @staticmethod
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema":
            LoginUI.main()
        elif op == "Abrir Conta":
            AbrirContaUI.main()

    @staticmethod
    def menu_admin():
        op = st.sidebar.selectbox("Menu", [
            "Manter Categorias",
            "Manter Clientes",
            "Manter Produtos",
            "Manter Entregadores",
            "Entregas em Andamento",
            "Entregas feitas",
            "Sair"
        ])
        if op == "Manter Categorias":
            ManterCategoriaUI.main()
        elif op == "Manter Clientes":
            ManterClienteUI.main()
        elif op == "Manter Entregadores":
            ManterEntregadoresUI.main()
        elif op == "Entregas em Andamento":
            EntregasEmAndamentoUI.main()
        elif op == "Manter Produtos":
            ManterProdutoUI.main()
        elif op == "Sair":
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    @staticmethod
    def menu_usuario():
        op = st.sidebar.selectbox("Menu", [
            "Listar minhas compras",
            "Comprar novamente",
            "Listar produtos",
            "Inserir produto no carrinho",
            "Visualizar o carrinho",
            "Sair"
        ])
        if op == "Listar minhas compras":
            ListarComprasUI.main()
        elif op == "Listar produtos":
            ListarProdutoUI.main()
        elif op == "Comprar novamente":
            ComprarNovamenteUI.main()
        elif op == "Inserir produto no carrinho":
            InserirProdutoCarrinhoUI.main()
        elif op == "Visualizar o carrinho":
            VisualizarCarrinhoUI.main()
        elif op == "Sair":
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    @staticmethod
    def menu_entregador():
        op = st.sidebar.selectbox("Menu", [
            "Listar minhas entregas",
            "Confirmar entrega",
            "Sair"
        ])
        if op == "Listar minhas entregas":
            MinhasEntregasUI.main()
        elif op == "Confirmar entrega":
            ConfirmarEntregasUI.main()
        elif op == "Sair":
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

    @staticmethod
    def main():
        if "tipo_usuario" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            tipo = st.session_state["tipo_usuario"]
            if tipo == "admin":
                IndexUI.menu_admin()
            elif tipo == "usuario":
                IndexUI.menu_usuario()
            elif tipo == "entregador":
                IndexUI.menu_entregador()

View.cadastrar_admin()
IndexUI.main()
