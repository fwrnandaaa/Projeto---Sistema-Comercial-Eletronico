import streamlit as st
from views import View

class ListarComprasUI:
    @staticmethod
    def main():
        st.title("Minhas Compras")

        if "id_cliente" not in st.session_state:
            st.error("Você precisa estar logado.")
            return

        compras = View.listar_compras_cliente(st.session_state["id_cliente"])

        if not compras:
            st.info("Nenhuma compra confirmada.")
            return

        for venda in compras:
            st.subheader(f"Compra #{venda.get_id()} - Data: {venda.get_data()} - Total: R$ {venda.get_total():.2f}")
            itens = View.listar_itens_venda(venda.get_id())
            for item in itens:
                st.write(
                    f"- Produto ID: {item.get_id_produto()} | "
                    f"Qtd: {item.get_qtd()} | "
                    f"Preço: R$ {item.get_preco():.2f} | "
                    f"Subtotal: R$ {item.get_qtd() * item.get_preco():.2f}"
                )
