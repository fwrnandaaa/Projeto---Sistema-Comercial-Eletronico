import streamlit as st
import pandas as pd
from views import View

class ListarComprasUI:
    @staticmethod
    def main():
        st.title("Minhas Compras")
        
        (tab1,) = st.tabs(["Listar"])
        with tab1:
            ListarComprasUI.listar()

    @staticmethod
    def listar():
        carrinho = View.listar_carrinho(id_carrinho=st.session_state["id_cliente"])
        try:
            if not carrinho:
                st.info("Nenhuma compra feita.")
            else:
                df = pd.DataFrame([item.to_dict() for item in carrinho])
                st.dataframe(df)
                st.success("Carrinho listado com sucesso!")
        except Exception as e:
            st.error(f"Erro ao adicionar produto: {str(e)}")
