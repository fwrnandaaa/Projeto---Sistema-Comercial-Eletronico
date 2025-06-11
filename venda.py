import json
from datetime import datetime

class Venda:
    def __init__(self, id):
        self.set_id(id)
        self.set_data(datetime.now())
        self.set_total(0)
        self.set_carrinho(True)
        self.set_id_cliente(0)

    def set_id(self, v):
        if v < 0:
            raise ValueError("ID não pode ser negativo")
        else: self.__id = v
    def set_carrinho(self, v):
        self.__carrinho = v
    def set_total(self, v):
        if v <0:
            raise ValueError("Valor não pode ser menor que 0")
        else: self.__total=v
    def set_id_cliente(self, v):
        self.__id_cliente = v
    def set_data(self, v):
        self.__data = v

    def get_id(self):
        return self.__id
    def get_data(self):
        return self.__data.strftime("%d/%m/%Y %H:%M")
    def get_carrinho(self):
        return self.__carrinho
    def get_total(self):
        return self.__total
  
    def get_id_cliente(self):
        return self.__id_cliente
    
    def __str__(self):
           return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - R$ {self.__total:.2f}"
    
    def to_json(self):
        dic = {}
        dic["id"] = self.__id       
        dic["data"] = self.__data.strftime("%d/%m/%Y %H:%M")
        dic["carrinho"] = self.__carrinho
        dic["total"] = self.__total
        dic["id_cliente"] = self.__id_cliente
        return dic
    
class Vendas:      # Persistência - Armazena os objetos em um arquivo/banco de dados
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
            cls.objetos.remove(x)
            cls.salvar()
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:     
            with open("vendas.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s: 
                    obj = Venda(dic["id"])
                    obj.set_data(datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
                    obj.set_carrinho(dic["carrinho"])
                    obj.set_total(dic["total"]) 
                    obj.set_id_cliente(dic["id_cliente"])
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass            
    
    @classmethod
    def salvar(cls):
        with open("vendas.json", mode="w") as arquivo:
            json.dump([obj.to_json() for obj in cls.objetos], arquivo, indent=4)
    
    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
        
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None:
            index = cls.objetos.index(x)
            cls.objetos[index] = obj
            cls.salvar()

