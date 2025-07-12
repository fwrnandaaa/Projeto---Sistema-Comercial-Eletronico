import streamlit as st
import pandas as pd
from views import View

class InserirProdutoCarrinhoUI:
    @staticmethod
    def main():
        st.title('Inserir Produto no Carrinho')

        # 🔑 Verifica se o cliente está logado e tem id_cliente
        #if 'id_cliente' not in st.session_state:
         #   st.error("Você precisa estar logado para adicionar produtos ao carrinho.")
         #   return

        produtos = View.produto_listar()

        if len(produtos) == 0:
            st.write("Nenhum produto disponível")
        else:
            with st.form(key="adicionar_form"):
                op = st.selectbox(
                    "Selecione o produto",
                    produtos,
                    format_func=lambda p: f"{p.get_descricao()} - R$ {p.get_preco():.2f}"
                )
                qtd = st.number_input("Quantidade", min_value=1, max_value=100, step=1)

                if st.form_submit_button("Adicionar ao carrinho"):
                    try:
                        # ✅ Se ainda não existe carrinho, cria um
                        if 'carrinho_id' not in st.session_state:
                            id_carrinho = View.inicializar_carrinho(st.session_state.id_cliente)
                            st.session_state.carrinho_id = id_carrinho

                        View.inserir_produto_no_carrinho(
                            st.session_state.carrinho_id,
                            op.get_id(),
                            qtd
                        )

                        st.success(f"Adicionado {qtd} unidades ao carrinho!")
                    except ValueError as e:
                        st.error(str(e))
