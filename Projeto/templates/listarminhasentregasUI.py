import streamlit as st
import pandas as pd
from views import View

class MinhasEntregasUI:
    def main():
        id_entregador = st.session_state.entregador_id

        entregas = View.entregas_por_entregador(id_entregador)

        if entregas:
            df = pd.DataFrame([{
                "ID": v.get_id(),
                "Data": v.get_data(),
                "Cliente": v.get_id_cliente(),
                "Status": v.get_status(),
                "Valor Total": f"R$ {v.get_total():.2f}"
            } for v in entregas])

            st.title("Minhas Entregas")
            st.dataframe(df)
        else:
            st.write("Você não tem entregas.")
