from abc import ABC, abstractmethod

class Modelo():
    objetos = []
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for x in cls.objetos:
            if x.get_id() > m:
                m = x.get_id()
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir
        for obj in cls.objetos():
            if obj.get_id() == id:
                return obj
        return None
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None:
            cls.objetos.remove(obj)
            cls.Objetos.append(x)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()

    @classmethod
    def abrir(cls):
        pass

    @classmethod
    def salvar(cls):
        pass