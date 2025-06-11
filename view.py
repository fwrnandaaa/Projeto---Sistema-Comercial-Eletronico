from cliente import Cliente, Clientes
from categoria import Categoria, Categorias
from produto import Produto, Produtos
from venda import Venda, Vendas
from vendaitem import VendaItem, VendasItens

class View:
    verificador_desconto = False

    # ADMIN
    @staticmethod
    def cadastrar_admin():
        for cliente in Clientes.listar_objetos():
            if cliente.get_email() == "admin":
                return
        View.cliente_inserir("admin", "admin", "1234")  

    # CLIENTE
    @staticmethod
    def cliente_inserir(nome, email, fone):
        c = Cliente(nome, email, fone, 0)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar():
        return Clientes.listar_objetos()
    
    @staticmethod
    def cliente_atualizar(nome, email, fone, id):
        c = Cliente(nome, email, fone, id)
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)

    # CARRINHO
    @staticmethod
    def inserir_produto_no_carrinho(id_carrinho, id_produto, qtd):
        produto = Produtos.listar_id(id_produto)
        if produto is None:
            raise ValueError("Produto não encontrado")
        
        preco = produto.get_preco()
        vi = VendaItem(0, qtd, preco)
        vi.set_id_venda(id_carrinho)
        vi.set_id_produto(id_produto)
        VendasItens.inserir(vi)  # Faltava inserir o item no carrinho

        carrinho = Vendas.listar_id(id_carrinho)
        if carrinho is None:
            raise ValueError("Carrinho não encontrado")
    
        novo_total = carrinho.get_total() + (qtd * preco)
        carrinho.set_total(novo_total)
        Vendas.atualizar(carrinho)

    @staticmethod
    def verificar_desconto_carrinho(id_carrinho):
        total_bruto = 0
        for item in VendasItens.listar():
            if item.get_id_venda() == id_carrinho:
                total_bruto += item.get_qtd() * item.get_preco()

        if total_bruto > 150:
            desconto = 10
        elif total_bruto > 60:
            desconto = 5
        else:
            desconto = 0

        if desconto > 0:
            total_com_desconto = total_bruto * (1 - desconto / 100)
            return {
                "Total sem desconto": round(total_bruto, 2),
                "Percentual do desconto": desconto,
                "Total após desconto": round(total_com_desconto, 2),
            }
        else: 
            return {
                "Total do carrinho": round(total_bruto, 2)
            }

    # CATEGORIA
    @staticmethod
    def categoria_inserir(nome):
        cat = Categoria(nome, 0)
        Categorias.inserir(cat)

    @staticmethod
    def categoria_listar():
        return Categorias.listar()
    
    @staticmethod
    def categoria_atualizar(id, nome):
        cat = Categoria(id, nome)
        Categorias.atualizar(cat)

    @staticmethod
    def categoria_excluir(id):
        cat = Categorias.listar_id(int(id))
        if cat is not None:
            Categorias.excluir(cat)
        else:
            raise ValueError("Categoria não encontrada para exclusão")

    
    # PRODUTO
    @staticmethod
    def produto_inserir(nome, preco, estoque, id_categoria):
        p = Produto(nome, preco, estoque, id_categoria)
        Produtos.inserir(p)    

    @staticmethod
    def produto_listar():
        return Produtos.listar()
    
    @staticmethod
    def produto_atualizar(descricao, preco, estoque, id):
        p = Produto(descricao, preco, estoque, id)
        Produtos.atualizar(p)

    @staticmethod
    def produto_excluir(id):
        p = Produto("", 0.0, 0, 0, id)
        Produtos.excluir(p)

    # FINALIZAR VENDA
    @staticmethod
    def finalizar_venda(id_carrinho):
        carrinho = Vendas.listar_id(id_carrinho)
        if carrinho is None:
            raise ValueError("Carrinho não encontrado")

        desconto_info = View.verificar_desconto_carrinho(id_carrinho)
        total_final = desconto_info.get("Total após desconto", carrinho.get_total())
        carrinho.set_total(total_final)
        Vendas.atualizar(carrinho)

        for item in VendasItens.listar():
            if item.get_id_venda() == id_carrinho:
                produto = Produtos.listar_id(item.get_id_produto())
                if produto:
                    novo_estoque = produto.get_estoque() - item.get_qtd()
                    produto.set_estoque(novo_estoque)
                    Produtos.atualizar(produto)

    # LIMPAR CARRINHO
    @staticmethod
    def limpar_carrinho(id_carrinho):
        for item in VendasItens.listar():
            if item.get_id_venda() == id_carrinho:
                VendasItens.excluir(item)

        carrinho = Vendas.listar_id(id_carrinho)
        if carrinho:
            carrinho.set_total(0)
            Vendas.atualizar(carrinho)

    # VER CARRINHO
    @staticmethod
    def ver_carrinho(id_carrinho):
        return [item for item in VendasItens.listar() if item.get_id_venda() == id_carrinho]
