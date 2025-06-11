import json

from categoria import Categoria, Categorias

class Produto:
    def __init__(self, descricao, preco, estoque, id_categoria,id=0):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_preco(preco)
        self.set_estoque(estoque)
        self.set_id_categoria(id_categoria)
        
    def set_id(self, id):
        if id < 0:
            raise ValueError("ID não pode ser negativo!")
        else:
            self.__id = id

    def get_id(self):
        return self.__id
    
    def set_descricao(self, descricao):
        if descricao == " ":
            raise ValueError("Descrição não pode estar vazio!")
        else:
            self.__descricao = descricao

    def get_descricao(self):
        return self.__descricao
    
    def set_preco(self, preco):
        if preco < 0:
            raise ValueError("Preço não pode ser negativo!")
        else:
            self.__preco = preco

    def get_preco(self):
        return self.__preco
    
    def set_estoque(self, estoque):
        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo!")
        elif estoque == " ":
            raise ValueError("Estoque não pode estar vazio!")
        else:
            self.__estoque = estoque

    def get_estoque(self):
        return self.__estoque
    
    def get_id_categoria(self):
        return self.__id_categoria

    def set_id_categoria(self, v):
        self.__id_categoria = v

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__preco:.2f} - Estoque: {self.__estoque} - ID Categoria: {self.__id_categoria}"
    
    def to_dict(self):
        return {
            "id": self.get_id(),
            "descricao": self.get_descricao(),
            "preco": self.get_preco(),
            "estoque": self.get_estoque(),
            "id_categoria": self.get_id_categoria()
    }
    
class Produtos:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for x in cls.objetos:
            if x.get_id() > m:
                m = x.get_id()
        obj.set_id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.set_id)
        if x != None:
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.id)
        if x != None:
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("produtos.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    obj = Produto(dic["descricao"], dic["preco"], dic["estoque"], dic["id"])
                    obj.set_id_categoria = dic["id_categoria"]
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump([p.to_dict() for p in cls.objetos], arquivo, indent=4)
    




        