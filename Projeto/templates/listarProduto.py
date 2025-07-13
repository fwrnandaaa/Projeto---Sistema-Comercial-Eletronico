import streamlit as st
import pandas as pd
from views import View

class ListarProdutoUI:
    @staticmethod
    def main():
        st.head = ("Produtos")
        tab1, = st.tabs(["Listar"])
        with tab1:
            ListarProdutoUI.listar() 

    @staticmethod
    def listar():
        produtos = View.produto_listar()
        try:
            if not produtos:
                st.info("Nenhum produto Disponível.")
            else:
                df = pd.DataFrame([produto.to_dict() for produto in produtos])
                st.dataframe(df)
                st.success("Produtos listados com sucesso!")
        except Exception as e:
            st.error(f"Erro ao listar produtos: {str(e)}")