import json
from models.modelo import Modelo

class Categoria(self, id, decricao):
    set_id(self.__id)
    set_desc(self.__descricao)

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

class Categorias(Modelo):
    