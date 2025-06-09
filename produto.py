import json

class Produto:
    def __init__(self, descricao, preco, estoque, id=0):
        if id < 0:
            raise ValueError("ID não pode ser negativo!")
        else:
            self.__id = 0

        if descricao == " ":
            raise ValueError("Descrição não pode estar vazio!")
        else:
            self.__descricao = descricao

        if preco < 0:
            raise ValueError("Preço não pode ser negativo!")
        elif preco == " ":
            raise ValueError("Preço não pode estar vazio!")
        else:
            self.__preco

        if estoque < 0:
            raise ValueError("Estoque não pode ser negativo!")
        elif preco == " ":
            raise ValueError("Estoque não pode estar vazio!")
        else:
            self.__estoque = estoque

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - R$ {self.__preco:.2f} - Estoque: {self.__estoque}"
    
class Produtos:
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for x in cls.objetos:
            if x.id > m:
                m = x.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.id == id:
                return obj
        return None
    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.id)
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
                    obj = Produto(dic["id"], dic["descricao"], dic["preco"], dic["estoque"])
                    obj.id_categoria = dic["id_categoria"]
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("produtos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)


    




        