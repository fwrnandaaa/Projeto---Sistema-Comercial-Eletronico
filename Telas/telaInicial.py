import streamlit as st

class TelaInicial:

    carrinho = None
    usuario_logado = None

    @staticmethod
    def mostrar_menu():
        st.title("Sistema Comercial Eletrônico")

        opcao = st.radio("Selecione uma opção:", ("Fazer login", "Fazer cadastro", "Visualizar carrinho"))

        if st.button("Confirmar"):
            if opcao == "Fazer login":
                TelaInicial.fazer_login()
            elif opcao == "Fazer cadastro":
                TelaInicial.fazer_cadastro()
            elif opcao == "Visualizar carrinho":
                TelaInicial.visualizar_carrinho()

    @staticmethod
    def fazer_login():
        st.header("Login")
        email = st.text_input("Email")
        senha = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            # Aqui você faria a verificação real, por enquanto só mostra o que digitou
            TelaInicial.usuario_logado = email
            st.success(f"Usuário {email} logado com sucesso!")

    @staticmethod
    def fazer_cadastro():
        st.header("Cadastro")
        nome = st.text_input("Nome")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        if st.button("Cadastrar"):
            # Salvar cadastro (simulação)
            st.success(f"Usuário {nome} cadastrado com email {email}!")

    @staticmethod
    def visualizar_carrinho():
        st.header("Carrinho")
        if TelaInicial.usuario_logado is None:
            st.warning("Você precisa estar logado para visualizar o carrinho.")
            return
        # Aqui você pode mostrar os itens do carrinho (exemplo estático)
        st.write(f"Mostrando o carrinho do usuário {TelaInicial.usuario_logado}")
        st.write("- Produto A")
        st.write("- Produto B")
        st.write("Total: R$ 100,00")

def main():
    TelaInicial.mostrar_menu()

if __name__ == "__main__":
    main()
