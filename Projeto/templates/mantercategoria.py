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
    def listar(cls):
        cls.abrir()
        return cls.objetos 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for x in cls.objetos:
            if x.get_id() > m: m = x.get_id()
        obj.set_id(m + 1)  
        cls.objetos.append(obj)
        cls.salvar() 

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for i, x in enumerate(cls.objetos):
            if x.get_id() == obj.get_id():
                cls.objetos[i] = obj
                cls.salvar()
                break
                
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()