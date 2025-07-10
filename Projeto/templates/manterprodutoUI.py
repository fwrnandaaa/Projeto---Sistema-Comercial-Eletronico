import streamlit as st
import pandas as pd
from views import View
import time

class ManterProdutoUI:
    @staticmethod
    def main():
        st.header("Cadastro de Produtos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterProdutoUI.listar()
        with tab2: ManterProdutoUI.inserir()
        with tab3: ManterProdutoUI.atualizar()
        with tab4: ManterProdutoUI.excluir()

    @staticmethod
    def listar():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:    
            list_dic = []
            for obj in produtos:
                dic_produto = obj.to_dict() 
                list_dic.append(dic_produto)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)

    @staticmethod
    def inserir():
        descricao = st.text_input("Informe a descricao")
        preco = st.number_input("Informe o preço")
        estoque = st.number_input("Informe a quantidade no estoque", value = 0, step = 1)
        categorias = View.categoria_listar()
        if len(categorias) == 0:
            st.write("Nenhuma categoria cadastrada")
        else:
            categoria = st.selectbox("Selecione a categoria", categorias)

        if st.button("Inserir"):
            try:
                View.produto_inserir(descricao, preco, estoque, categoria.get_id())
                st.success("Produto adicionado")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)

    @staticmethod
    def atualizar():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Atualização de produto", produtos)
            descricao = st.text_input("Informe a nova descrição", op.get_descricao())
            preco = st.text_input("Informe o novo preço (use ponto para decimais)", str(op.get_preco()))
            estoque = st.text_input("Informe o novo estoque", str(op.get_estoque()))
            categorias = View.categoria_listar()
            categoria = st.selectbox("Selecione a nova categoria", categorias, 
                                   index=[cat.get_id() for cat in categorias].index(op.get_id_categoria()))
            
            if st.button("Atualizar"):
                try:
                    preco_float = float(preco)
                    estoque_int = int(estoque)
                    View.produto_atualizar(op.get_id(), descricao, preco_float, estoque_int, categoria.get_id())
                    st.success("Produto atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(f"Valor inválido: {erro}")    
                    time.sleep(2)
                    st.rerun()

    @staticmethod
    def excluir():
        produtos = View.produto_listar()
        if len(produtos) == 0: 
            st.write("Nenhum produto cadastrado")
        else:
            op = st.selectbox("Exclusão de produto", produtos)
            if st.button("Excluir"):
                try:
                    View.produto_excluir(op.get_id())
                    st.success("Produto excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))
                    time.sleep(2)
                    st.rerun()