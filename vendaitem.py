import json

class VendaItem:
    def __init__(self, id, qtd=1, preco=1):
        self.__id_venda = 0
        self.__id_produto = 0
        if id < 0:
            raise ValueError("ID não pode ser negativo")
        else: self.__id = id
        if qtd <= 0:
            raise ValueError("Quantidade não pode ser menor que 1")
        else: self.__qtd = qtd
        if preco <0: 
            raise ValueError("Preço não pode ser negativo")
        else: self.__preco = preco
    def __str__(self):
        return f"{self.__id} - {self.__qtd} - R$ {self.__preco:.2f}"
    def get_id(self):
        return self.__id
    def get_qtd(self):
        return self.__qtd
    def get_preco(self):
        return self.__preco
    def get_id_venda(self):
        return self.__id_venda
    def get_id_produto(self):
        return self.__id_produto
    
    def set_id_venda(self, v):
        if v < 0: raise ValueError("ID da venda não pode ser negativo")
        else: self.__id_venda=v
    def set_id_produto(self, v):
        if v <0: raise ValueError("ID do produto não pode ser negativo")
        else: self.__id_produto=v
    def set_id(self, v):
        if v <=0: raise ValueError("ID não pode ser negativo")
        else: self.__id = v
    def set_preco(self, v):
        if v <= 0: raise ValueError("Preço não pode ser negativo ou estar zerado")
        else: self.__preco = v
    def set_qtd(self, v):
        if v <= 0: raise ValueError("Quantidade não pode estar zerada")
        else: self.__qtd = v
    def to_json(self):
        return {
            "id": self.__id,
            "qtd": self.__qtd,
            "preco": self.__preco,
            "id_venda": self.__id_venda,
            "id_produto": self.__id_produto
        }
class VendasItens:      # Persistência - Armazena os objetos em um arquivo/banco de dados
    objetos = []   # atributo de classe / estático - Não tem instância
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
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None                
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            for obj in cls.objetos:
                if x.get_id() == obj.get_id():
                    cls.objetos.remove(x)
                    cls.salvar()
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:     
            with open("vendasItens.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = VendaItem(dic["id"], dic["qtd"], dic["preco"])
                    obj.set_id_venda(dic["id_venda"])
                    obj.set_id_produto(dic["id_produto"])
                    cls.objetos.append(obj)
        except (FileNotFoundError, json.JSONDecodeError):
            pass            
    @classmethod
    def salvar(cls):
        with open("vendasItens.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = VendaItem.to_json)
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None               
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()