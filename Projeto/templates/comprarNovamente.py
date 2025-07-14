import streamlit as st
import pandas as pd
from views import View

class ComprarNovamenteUI:
    @staticmethod
    def main():
        st.title("Comprar Novamente")

        try:
            if "id_cliente" not in st.session_state:
                st.error("Você precisa estar logado para repetir uma compra.")
                return

            id_cliente = st.session_state["id_cliente"]
            compras = View.listar_compras_cliente(id_cliente)

            if compras:
                df = pd.DataFrame([{
                    "ID": c.get_id(),
                    "Data": c.get_data(),  # já retorna string formatada
                    "Valor Total (R$)": f"R$ {c.get_total():.2f}",
                    "Status": c.get_status()
                } for c in compras])

                st.dataframe(df, use_container_width=True)

                op = st.selectbox(
                    "Selecione uma compra para repetir",
                    compras,
                    format_func=lambda v: f"ID: {v.get_id()} - {v.get_data()} - R$ {v.get_total():.2f}"
                )

                if st.button("Repetir Compra"):
                    novo_id = View.comprar_novamente(op.get_id())
                    if novo_id:
                        st.success("Compra repetida com sucesso!")
                    else:
                        st.warning("Não foi possível repetir a compra.")
            else:
                st.info("Nenhuma compra disponível para repetir.")

        except Exception as e:
            st.error(f"Erro inesperado: {str(e)}")
