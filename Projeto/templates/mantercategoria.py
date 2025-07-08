import streamlit as st
import pandas as pd
from views import View
import time

class ManterCategoriaUI:
    def main():
        st.header("Cadastro de Categorias")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterCategoriaUI.listar()
        with tab2: ManterCategoriaUI.inserir()
        with tab3: ManterCategoriaUI.atualizar()
        with tab4: ManterCategoriaUI.excluir()
    def listar():
        categorias = View.categoria_listar()
        if len(categorias) == 0: 
            st.write("Nenhuma categoria cadastrada")
        else:    
            list_dic = []
            for obj in categorias:
                dic = obj.__dict__ 
                list_dic.append(dic)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
#tenho verificar se daqui pra baixo ta certo msm
    @classmethod
    def listar():
      pass

    @classmethod
    def inserir():
       pass

    @classmethod
    def atualizar():
       pass
                
    @classmethod
    def excluir():
        pass