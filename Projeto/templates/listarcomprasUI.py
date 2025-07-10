# import streamlit as st
# class ListarComprasUI:
#     def main():
#         st.header("Listar minhas Compras")
#         tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
#         with tab1: ListarComprasUI.listar()
#         with tab2: ListarComprasUI.inserir()
#         with tab3: ListarComprasUI.atualizar()
#         with tab4: ListarComprasUI.excluir()

# #tenho verificar se daqui pra baixo ta certo msm
#     @classmethod
#     def listar(cls):
#         cls.abrir()
#         return cls.objetos 

#     @classmethod
#     def inserir(cls, obj):
#         cls.abrir()
#         m = 0
#         for x in cls.objetos:
#             if x.get_id() > m: m = x.get_id()
#         obj.set_id(m + 1)  
#         cls.objetos.append(obj)
#         cls.salvar() 

#     @classmethod
#     def atualizar(cls, obj):
#         cls.abrir()
#         for i, x in enumerate(cls.objetos):
#             if x.get_id() == obj.get_id():
#                 cls.objetos[i] = obj
#                 cls.salvar()
#                 break
                
#     @classmethod
#     def excluir(cls, obj):
#         x = cls.listar_id(obj.get_id())
#         if x != None: 
#             cls.objetos.remove(x)
#             cls.salvar()

import streamlit as st
import pandas as pd
from views import View

class ListarComprasUI:
    @staticmethod
    def main():
        st.title("Minhas Compras")
        
        (tab1,) = st.tabs(["Listar"])
        with tab1:
            ListarComprasUI.listar()

        

    @staticmethod
    def listar():
        carrinho = View.listar_carrinho(id_carrinho=st.session_state["cliente_id"])

        if not carrinho:
            st.info("Carrinho vazio.")
        else:
            df = pd.DataFrame([item.to_dict() for item in carrinho])
            st.dataframe(df)
            st.success("Carrinho listado com sucesso!")
