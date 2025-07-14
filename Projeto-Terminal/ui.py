from venda import Venda, Vendas
from view import View

class UI:
    carrinho = None
    usuario_logado = None

    @staticmethod
    def menu():
        print("|------------------------------------------------|")
        print("|                BEM-VINDO                       |")
        print("| 1 - Fazer login                                |")
        print("| 2 - Fazer cadastro                             |")
        print("| 3 - Visualizar produtos                        |")
        print("|------------------------------------------------|")
        try:
            op = int(input("Selecione uma opção: "))
        except ValueError:
                print("Por favor, insira um número válido.")
                UI.menu()
        if op == 1:
            email = input("Email: ")
            senha = input("Senha: ")

            cliente = next((c for c in View.cliente_listar() if c.get_email() == email and c.get_senha() == senha), None)
            if not cliente:
                print("Cliente não encontrado. Faça o cadastro.")
                return 
            UI.usuario_logado = cliente

        if op == 2:
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            fone = input("Número para contato: ")
            cliente = View.cliente_inserir(nome, email, fone, senha)
            UI.menu()
        
        if op == 3:
            for c in View.produto_listar():
                print(c)
            UI.menu()

        if UI.usuario_logado is None:
            print("Erro: Nenhum usuário logado.")
            return
        while True:
            if UI.usuario_logado.get_email() == "admin" and UI.usuario_logado.get_senha() == "admin":

                print("|------------------------------------------------|")
                print("| Cadastro de Categorias                         |")
                print("| 1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir    |")
                print("|------------------------------------------------|")
                print("| Cadastro de Produtos                           |")
                print("| 5-Inserir, 6-Listar, 7-Atualizar, 8-Excluir    |")
                print("|------------------------------------------------|")
                print("|------------------------------------------------|")
                print("| Cadastro de Clientes                           |")
                print("| 9-Inserir, 10-Listar, 11-Atualizar, 12-Excluir |")
                print("|------------------------------------------------|")
                print("| 99-Logout                                      |")
                print("|------------------------------------------------|")
            else:
                print("|------------------------------------------------|")
                print("| 13-Iniciar um carrinho de compra               |")
                print("| 14-Listar as compras                           |")
                print("| 15-Visualizar carrinho                         |")
                print("| 16-Inserir produto no carrinho                 |")
                print("| 17-Confirmar a compra                          |")
                print("| 99-Logout                                      |")
                print("|------------------------------------------------|")
                print("|                                                |")
                print("|------------------------------------------------|")

            try:
                op = int(input("Selecione uma opção: "))
            except ValueError:
                print("Por favor, insira um número válido.")
                continue

            #ADMIN
            if op == 1:
                nome = input("Nome da categoria: ")
                View.categoria_inserir(nome)
            elif op == 2:
                for cat in View.categoria_listar():
                    print(cat)
            elif op == 3:
                id = int(input("ID da categoria: "))
                nome = input("Novo nome da categoria: ")
                View.categoria_atualizar(nome, id)
            elif op == 4:
                id = int(input("ID da categoria: "))
                id = int(id)
                View.categoria_excluir(id)
            elif op == 5:
                descricao = input("Nome do produto: ")
                preco = float(input("Preço: "))
                estoque = int(input("Estoque: "))
                id_categoria = int(input("ID categoria: "))
                View.produto_inserir(descricao, preco, estoque, id_categoria)    
            elif op == 6:
                for prod in View.produto_listar():
                    print(prod)
            elif op == 7:
                descricao = input("Descricao: ")
                preco = float(input("Novo preço: "))
                estoque = int(input("Novo estoque: "))
                id_categoria = int(input("ID do produto: "))
                View.produto_atualizar(descricao, preco, estoque, id_categoria)
            elif op == 8:
                id = int(input("ID do produto: "))
                View.produto_excluir(id)

            elif op == 9:
                nome = input("Nome: ")
                email = input("Email: ")
                fone = input("Número para contato: ")
                senha = input("Senha: ")
                View.cliente_inserir(nome, email, fone, senha)

            elif op == 10:
                for cat in View.cliente_listar():
                    print(cat)

            elif op == 11:
                cliente_para_att = int(input("Informe o ID do cliente que deseja atualizar: "))
                nome = input("Novo nome: ")
                email= input("Novo email: ")
                fone = input("Novo numero para contato: ")
                senha = input("Nova senha: ")
                View.cliente_atualizar(nome, email, fone, senha, cliente_para_att)  
            elif op==12:
                id = int(input("ID do cliente: "))
                View.cliente_excluir(id)


            #CLIENTE
            elif op == 13:
                venda = Venda(0)
                Vendas.inserir(venda)
                UI.carrinho = venda.get_id()
                print(f"Carrinho iniciado com ID {UI.carrinho}")

            elif op == 14:
                for v in Vendas.listar():
                    print(v)
            elif op == 15:
                if UI.carrinho is None:
                    print("Nenhum carrinho iniciado. Inicie um antes.")
                else:
                    for item in View.ver_carrinho(UI.carrinho):
                        print(item)
                total = View.total_carrinho(UI.carrinho)
                print("Total do carrinho",total)
                if total >= 60:
                    desconto_info = View.verificar_desconto_carrinho(UI.carrinho)
                    for chave, valor in desconto_info.items():
                        print(f"{chave}: {valor}")

                

            elif op == 16:
                if UI.carrinho is None:
                    print("Nenhum carrinho iniciado. Inicie um antes.")
                else:
                    id_produto = int(input("ID do produto: "))
                    qtd = int(input("Quantidade: "))
                    View.inserir_produto_no_carrinho(UI.carrinho, id_produto, qtd)
            elif op == 17:
                if UI.carrinho is None:
                    print("Nenhum carrinho iniciado. Inicie um antes.")
                else:
                    View.finalizar_venda(UI.carrinho)
                    View.limpar_carrinho(UI.carrinho)
                    print("Compra finalizada!")
                    UI.carrinho = None 

            elif op == 99:
                UI.usuario_logado = None
                UI.menu()
            else:
                print("Opção inválida.")
    
    @staticmethod
    def iniciar():
        View.cadastrar_admin()
        UI.menu()
    
if __name__ == "__main__":
    UI.iniciar()