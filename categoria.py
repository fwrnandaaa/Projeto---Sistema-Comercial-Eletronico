import json

class Categoria:
    def __init__(self, descricao, id=0):
        if id <0:
            raise ValueError("ID não pode ser negativo")
        else: self.__id = id      
        if descricao  == "":
            raise ValueError("Descrição não pode estar vazia")
        else:self.__descricao = descricao
    def __str__(self):
        return f"ID: {self.__id} - Descrição: {self.__descricao}"
    
    def to_dict(self): #essa função vai me ajudar a modificar o json agora que está tudo encapsulado
        return {
            "id": self.__id,
            "descricao": self.__descricao,
        }
    #getters
    def get_id(self):
        return self.__id
    def get_descricao(self):
        return self.__descricao
    
    #setters
    def set_descricao(self, v):
        if v == "":
            raise ValueError("Descrição não pode estar vazia")
        else: self.__descricao = v

    def set_id(self, v):
        if v < 0:
            raise ValueError("ID não pode ser negativo")
        else: self.__id = v

class Categorias:
    objetos = []
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:    
            with open("categoria.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    categoria = Categoria(
                        id=dic["id"],
                        descricao=dic["descricao"],
                )
                   
                    cls.objetos.append(categoria)
        except FileNotFoundError:
            pass    

    @classmethod
    def salvar(cls):
        cls.objetos.sort(key=lambda cliente: cliente.get_id())
        with open("categoria.json", mode="w") as arquivo:
            lista_dicts = [cat.to_dict() for cat in cls.objetos]
            json.dump(lista_dicts, arquivo, indent=4)
    
    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        if len(cls.objetos) > 0:
            m = max(cls.objetos, key=lambda c: c.get_id()).get_id()
        obj.set_id(m + 1)
        cls.objetos.append(obj)
        cls.salvar() 

    @classmethod
    def listar(cls):
        cls.abrir()
        return [str(cat) for cat in cls.objetos]
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id: 
                return obj
        return None    
    @classmethod
    def atualizar(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.objetos.append(obj)
            cls.salvar()
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()
