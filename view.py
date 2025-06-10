from cliente import Cliente, Clientes
from categoria import Categoria, Categorias
from produto import Produto, Produtos
from venda import Venda, Vendas
from vendaitem import VendaItem, VendasItens

class View:
    verificador_desconto = False
    def cadastrar_admin():
        for cliente in Clientes.listar_objetos():
            if cliente.get_email() == "admin" : pass
        else:
            View.cliente_inserir("admin", "admin", "1234")  

    def cliente_inserir(nome, email, fone):
        c = Cliente(0, nome, email, fone)
        Clientes.inserir(c)
    def cliente_listar():
       return Clientes.listar()
    def cliente_atualizar(id, nome, email, fone):
        c = Cliente(id, nome, email, fone)
        Clientes.atualizar(c)
    def cliente_excluir(id):
        c = Cliente(id, "", "", "")
        Clientes.excluir(c)

    def inserir_produto_no_carrinho(id_carrinho, id_produto, qtd):
        preco = Produtos.listar_id(id_produto).get_preco()
        vi = VendaItem(0, qtd, preco)
        vi.set_id_venda(id_carrinho)
        vi.set_id_produto(id_produto)
        carrinho = Vendas.listar_id(id_carrinho)
        if carrinho is None:
          raise ValueError("Carrinho não encontrado")
    
        novo_total = carrinho.get_total() + (vi.get_qtd() * vi.get_preco())
        carrinho.set_total(novo_total) 
        Vendas.atualizar(carrinho)

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

        total_com_desconto = total_bruto * (1 - desconto / 100)
        desconto_aplicado = desconto > 0
        if desconto > 0:
            return {
                "Total sem desconto": round(total_bruto, 2),
                "Percentual do desconto": desconto,
                "Total após desconto": round(total_com_desconto, 2),
            }
        else: 
                return {
                   " Total do carrinho": total_bruto
                }
