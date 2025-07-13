import streamlit as st
import pandas as pd
from views import View
import time

class EntregasEmAndamentoUI:
    def main():
        st.title("Entregas em Andamento")
        entregas = View.vendas_listar()  
        andamento = [v for v in entregas if v.get_status() == "Em andamento"]

        if andamento:
            df = pd.DataFrame([{
                "ID": v.get_id(),
                "Data": v.get_data(),
                "Cliente": v.get_id_cliente(),
                "Status": v.get_status(),
                "Entregador": v.get_id_entregador()
            } for v in andamento])
            st.dataframe(df)
        else:
            st.write("Nenhuma entrega em andamento.")
