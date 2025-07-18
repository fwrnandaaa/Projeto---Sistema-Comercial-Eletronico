
from models.cliente import Cliente, Clientes
from models.categoria import Categoria, Categorias
from models.produto import Produto, Produtos
from models.venda import Venda, Vendas
from models.vendaitem import VendaItem, VendaItens
from models.entregador import Entregador, Entregadores

class View:
    # Entregador
    def entregador_inserir(nome, email, fone, senha):
        e = Entregador(nome, email, fone, senha, 0)
        Entregadores.inserir(e)
    
    def entregador_autenticar(email, senha):
        try:
            entregador = Entregadores.listar_objetos()
            for e in entregador:
                if e.get_email() == email and e.get_senha() == senha:
                    return {
                        "id": e.get_id(),
                        "nome": e.get_nome(),
                       "admin": (e.get_email() == "admin")

                    }
            return None
            
        except Exception as e:
            print(f"Erro ao autenticar: {str(e)}")
            return None
    
    @staticmethod
    def entregadores_listar():
         Entregadores.abrir()  
         return Entregadores.objetos

    verificador_desconto = False
    
    # ADMIN
    @staticmethod
    def cadastrar_admin():
        for cliente in Clientes.listar_objetos():
            if cliente.get_email() == "admin" and cliente.get_senha() == "admin":
                return
        View.cliente_inserir("admin", "admin", "1234", "admin")
    @staticmethod
    def get_nome_entregador(id_entregador):
        entregador = Entregadores.listar_id(id_entregador)
        if entregador:
            return entregador.get_nome()
        else:
            return "Desconhecido"

    # CLIENTE
    @staticmethod
    def listar_compras_cliente(id_cliente):
        Vendas.abrir()
        return [v for v in Vendas.objetos if v.get_id_cliente() == id_cliente]

    @staticmethod
    def listar_itens_venda(id_venda):
        VendaItens.abrir()
        return [i for i in VendaItens.objetos if i.get_id_venda() == id_venda]

    @staticmethod
    def cliente_autenticar(email, senha):
        try:
            clientes = Clientes.listar_objetos()
            for cliente in clientes:
                if cliente.get_email() == email and cliente.get_senha() == senha:
                    return {
                        "id": cliente.get_id(),
                        "nome": cliente.get_nome(),
                       "admin": (cliente.get_email() == "admin")

                    }
            return None
            
        except Exception as e:
            print(f"Erro ao autenticar: {str(e)}")
            return None
    
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        c = Cliente(nome, email, fone, senha, 0)
        Clientes.inserir(c)

    @staticmethod
    def cliente_listar():
         Clientes.abrir()  
         return Clientes.objetos

    @staticmethod
    def listar_id(id):
        return Clientes.listar_id(id)
    
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        c = Cliente(nome, email, fone, senha, id)  # Note a ordem dos parâmetros
        Clientes.atualizar(c)

    @staticmethod
    def cliente_excluir(id):
        c = Cliente("teste", "teste", "teste", "teste", id)
        Clientes.excluir(c)

    # CARRINHO
    @staticmethod
    def inicializar_carrinho(id_cliente):
        carrinho = Venda(0)  
        carrinho.set_id_cliente(id_cliente)
        Vendas.inserir(carrinho)
        return carrinho.get_id()  

    @staticmethod
    def inserir_produto_no_carrinho(id_carrinho, id_produto, qtd):
        produto = Produtos.listar_id(id_produto)
        if produto is None:
            raise ValueError("Produto não encontrado")
        
        if produto.get_estoque() < qtd:
            raise ValueError("Estoque insuficiente")

        preco = produto.get_preco()
        vi = VendaItem(0, qtd, preco)
        vi.set_id_venda(id_carrinho)
        vi.set_id_produto(id_produto)
        VendaItens.inserir(vi)  # Faltava inserir o item no carrinho

        carrinho = Vendas.listar_id(id_carrinho)
        if carrinho is None:
            raise ValueError("Carrinho não encontrado")
    
        novo_total = carrinho.get_total() + (qtd * preco)
        carrinho.set_total(novo_total)
        Vendas.atualizar(carrinho)

    @staticmethod
    def verificar_desconto_carrinho(id_carrinho):
        total_bruto = 0
        for item in VendaItens.listar():
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
    
    #ENTREGADORES
    @staticmethod
    def entregadores_listar():
         Entregadores.abrir()  
         return Entregadores.objetos
    
    @staticmethod
    def entregador_atualizar(id, nome, email, fone, senha):
        entregador = Entregador(nome, email, fone, senha, id)  # ← Usa Entregador!
        Entregadores.atualizar(entregador)

    @staticmethod
    def entregador_excluir(id):
        c = Entregador("teste", "teste", "teste", "teste", id)
        Entregadores.excluir(c)
    
    @staticmethod
    def entregas_por_entregador(id_entregador):
        return Vendas.listar_por_entregador(id_entregador)

    @staticmethod
    def entrega_marcar_entregue(id_venda):
        Vendas.marcar_entregue(id_venda)

    # CATEGORIA
    @staticmethod
    def categoria_inserir(nome):
        novo_id = max(cat.get_id() for cat in Categorias.objetos) + 1
        cat = Categoria(novo_id, nome)  # ⬅️ Aqui você sempre cria com ID = 0
        Categorias.inserir(cat)

    @staticmethod
    def categoria_atualizar(id, nome):
        cat = Categoria(id, nome)
        Categorias.atualizar(cat)

    @staticmethod
    def categoria_listar():
         Categorias.abrir()  
         return Categorias.objetos
    
    @staticmethod
    def categoria_atualizar(id, nome):
        cat = Categoria(id, nome)
        Categorias.atualizar(cat)

    @staticmethod
    def categoria_excluir(id):
        c = Categoria(id, "teste")
        Categorias.excluir(c)
    
    # PRODUTO
    @staticmethod
    def produto_inserir(nome, preco, estoque, id_categoria):
        p = Produto(nome, preco, estoque, id_categoria)
        p.set_id_categoria(id_categoria)
        Produtos.inserir(p)    

    @staticmethod
    def produto_listar():
        return Produtos.listar()
    
    @staticmethod
    def produto_atualizar(id, descricao, preco, estoque, idcat):
        p = Produto(descricao, preco, estoque, idcat, id)
        Produtos.atualizar(p)

    @staticmethod
    def produto_excluir(id):
        p = Produto("", 0.0, 0, id)
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

        for item in VendaItens.listar():
            if item.get_id_venda() == id_carrinho:
                produto = Produtos.listar_id(item.get_id_produto())
                if produto:
                    novo_estoque = produto.get_estoque() - item.get_qtd()
                    produto.set_estoque(novo_estoque)
                    Produtos.atualizar(produto)
    
    @staticmethod
    def vendas_listar():
         Vendas.abrir()  
         return Vendas.objetos

    @staticmethod
    def comprar_novamente(id_venda_original):
        try:
            venda_original = Vendas.listar_id(id_venda_original)
            if venda_original is None:
                raise ValueError("Nenhuma compra encontrada")

            id_cliente = venda_original.get_id_cliente()
            novo_carrinho_id = View.inicializar_carrinho(id_cliente)

            encontrou_item = False

            for item in VendaItens.listar():
                if item.get_id_venda() == id_venda_original:
                    produto = Produtos.listar_id(item.get_id_produto())
                    if produto and produto.get_estoque() >= item.get_qtd():
                        View.inserir_produto_no_carrinho(novo_carrinho_id, produto.get_id(), item.get_qtd())
                        encontrou_item = True

            if encontrou_item:
                return novo_carrinho_id  # ← Retorna o ID do novo carrinho com os itens inseridos
            else:
                return None
        except Exception as e:
            print(f"Erro ao repetir compra: {str(e)}")
            return None



    # LIMPAR CARRINHO
    @staticmethod
    def listar_carrinho(id_carrinho):
        itens = []
        for item in VendaItens.listar():
            if item.get_id_venda() == id_carrinho:
                produto = Produtos.listar_id(item.get_id_produto())
                if produto:
                    itens.append({
                        "Produto": produto.get_descricao(),
                        "Qtd": item.get_qtd(),
                        "Preço unitário": item.get_preco(),
                        "Subtotal": round(item.get_qtd() * item.get_preco(), 2)
                    })
        return itens

    @staticmethod
    def limpar_carrinho(id_carrinho):
        for item in VendaItens.listar():
            if item.get_id_venda() == id_carrinho:
                VendaItens.excluir(item)

        carrinho = Vendas.listar_id(id_carrinho)
        if carrinho:
            carrinho.set_total(0)
            Vendas.atualizar(carrinho)
    
    @staticmethod
    def total_carrinho(id_carrinho):
        total = 0
        for item in VendaItens.listar():
            if item.get_id_venda() == id_carrinho:  # Aqui está a correção
                total += item.get_qtd() * item.get_preco()
        return total
    
    # VER CARRINHO
    @staticmethod
    def ver_carrinho(id_carrinho):
        return [item for item in VendaItens.listar() if item.get_id_venda() == id_carrinho]
