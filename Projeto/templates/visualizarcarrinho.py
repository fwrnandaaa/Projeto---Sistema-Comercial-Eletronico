import streamlit as st
import pandas as pd
from views import View

class VisualizarCarrinhoUI:
    @staticmethod
    def main():
        st.title('Seu Carrinho de Compras')
        
        if 'carrinho_id' not in st.session_state:
            st.warning("Carrinho vazio")
            return
            
        carrinho_id = st.session_state.carrinho_id
        
        # Usando os métodos da View
        itens = View.listar_carrinho(carrinho_id)
        total = View.total_carrinho(carrinho_id)
        desconto_info = View.verificar_desconto_carrinho(carrinho_id)
        
        if not itens:
            st.warning("Carrinho vazio")
            return
            
        # Exibição dos itens
        df = pd.DataFrame(itens)
        st.dataframe(df)
        
        # Exibição do total e descontos
        if "Total após desconto" in desconto_info:
            st.markdown(f"""
            **Total Bruto:** R$ {desconto_info['Total sem desconto']:.2f}  
            **Desconto ({desconto_info['Percentual do desconto']}%):** R$ {desconto_info['Total sem desconto'] - desconto_info['Total após desconto']:.2f}  
            **Total com Desconto:** R$ {desconto_info['Total após desconto']:.2f}
            """)
        else:
            st.markdown(f"**Total do Carrinho:** R$ {total:.2f}")
        
        # Botões de ação
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Atualizar Carrinho"):
                st.rerun()
        with col2:
            if st.button("✅ Finalizar Compra"):
                try:
                    View.finalizar_venda(carrinho_id)
                    st.success("Compra finalizada com sucesso!")
                    del st.session_state['carrinho_id']
                    st.rerun()
                except ValueError as e:
                    st.error(str(e))
        
        if st.button("🗑️ Limpar Carrinho"):
            View.limpar_carrinho(carrinho_id)
            st.success("Carrinho limpo!")
            st.rerun()