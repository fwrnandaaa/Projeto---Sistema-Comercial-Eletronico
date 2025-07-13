import streamlit as st
import pandas as pd
from views import View
import time

class ManterEntregadoresUI:
    def main():
        st.header("Cadastro de Entregadores")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterEntregadoresUI.listar()
        with tab2: ManterEntregadoresUI.inserir()
        with tab3: ManterEntregadoresUI.atualizar()
        with tab4: ManterEntregadoresUI.excluir()
    def listar():
        entregador = View.entregadores_listar()
        if len(entregador) == 0: 
            st.write("Nenhum entregador cadastrado")
        else:    
            list_dic = []
            for obj in entregador:
                dic_entregador = obj.to_dict() 
                del dic_entregador["senha"] 
                list_dic.append(dic_entregador)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    def inserir():
        nome = st.text_input("Informe o nome: ")
        email = st.text_input("Informe o e-mail: ")
        fone = st.text_input("Informe o fone: ")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Cadastrar"):
            # usuário é cadastrado com senha padrão
            try:
                View.entregador_inserir(nome, email, fone, senha)
                st.success("Entregador inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(erro)    
                time.sleep(2)
                st.rerun()
    def atualizar():
        entregador = View.entregadores_listar()
        if len(entregador) == 0: 
            st.write("Nenhum entregador cadastrado")
        else:
            op = st.selectbox("Atualização de cliente", entregador)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            email = st.text_input("Informe o novo e-mail", op.get_email())
            fone = st.text_input("Informe o novo fone", op.get_fone())
            if st.button("Atualizar"):
                try:
                    View.entregador_atualizar(op.get_id(), nome, email, fone, op.get_senha())
                    st.success("entregador atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)    
                    time.sleep(2)
                    st.rerun()

    def excluir():
        entregador = View.entregadores_listar()
        if len(entregador) == 0: 
            st.write("Nenhum entregadr cadastrado")
        else:
            op = st.selectbox("Exclusão de entregador", entregador)
            if st.button("Excluir"):
                View.entregador_excluir(op.get_id())
                st.success("Entregador excluído com sucesso")
                time.sleep(2)
                st.rerun()

