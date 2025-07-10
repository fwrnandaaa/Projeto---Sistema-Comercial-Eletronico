import json
from models.modelo import Modelo

class Categoria:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_desc(descricao)

    def set_id(self, v):
        if v < 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = v

    def set_desc(self, v):
        if v == "":
            raise ValueError("Descrição não pode estar vazia")
        self.__descricao = v

    def get_id(self):
        return self.__id

    def get_desc(self):
        return self.__descricao
    
    def __str__(self):
        return self.get_desc() 

class Categorias(Modelo):
    objetos = []  # Se não existir, garanta isso aqui

    @classmethod
    def inserir(cls, obj):
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def abrir(cls):
        try:    
            with open("categorias.json", mode="r") as arquivo:
                cls.objetos = [] 
                s = json.load(arquivo)
                for dic in s:
                    obj = Categoria(dic["_Categoria__id"], dic["_Categoria__descricao"])
                    cls.objetos.append(obj)

        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        with open("categorias.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)

    @classmethod
    def atualizar(cls, obj_atualizado):
        cls.abrir()
        
        encontrou = False
        for i, obj in enumerate(cls.objetos):
            if obj.get_id() == obj_atualizado.get_id():
                try:
                    obj.set_desc(obj_atualizado.get_desc())
                    encontrou = True
                    break
                except ValueError as e:
                    raise ValueError(f"Dados inválidos: {e}")
        
        if not encontrou:
            raise ValueError("Categoria não encontrada para atualização")
        cls.salvar()