import streamlit as st
from views import View

class ConfirmarEntregasUI:
    def main():
        id_entregador = st.session_state.entregador_id


        todas = View.entregas_por_entregador(id_entregador)
        entregas = [v for v in todas if v.get_status() == "Em andamento"]


        if entregas:
            op = st.selectbox(
                "Selecione uma entrega",
                entregas,
                format_func=lambda v: f"ID: {v.get_id()} - Cliente: {v.get_id_cliente()} - Status: {v.get_status()}"
            )

            if st.button("Marcar como Entregue"):
                View.entrega_marcar_entregue(op.get_id())
                st.success("Status atualizado para Entregue.")
        else:
            st.write("Você não tem entregas atribuídas.")
