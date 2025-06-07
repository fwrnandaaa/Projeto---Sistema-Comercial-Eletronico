import json


class Cliente:
    def __init__(self, nome, email, fone, id=0):
        if id < 0:
            raise ValueError("ID não pode ser negativo")
        else:
            self.__id = id


        if nome == "":
            raise ValueError("Nome não pode estar em branco")
        else:
            self.__nome = nome


        if email == "":
            raise ValueError("Email não pode estar em branco")
        else:
            self.__email = email


        if fone == "":
            raise ValueError("Telefone não pode estar em branco")
        else:
            self.__fone = fone


    # getters
    def get_id(self):
        return self.__id


    def get_nome(self):
        return self.__nome


    def get_email(self):
        return self.__email


    def get_fone(self):
        return self.__fone


    # setters
    def set_id(self, v):
        if v < 0:
            raise ValueError("ID não pode ser negativo")
        self.__id = v

    def set_nome(self, v):
        if v == "":
            raise ValueError("Nome não pode estar em branco")
        else:
            self.__nome = v


    def set_email(self, v):
        if v == "":
            raise ValueError("Email não pode estar em branco")
        else:
            self.__email = v


    def set_fone(self, v):
        if v == "":
            raise ValueError("Telefone não pode estar em branco")
        else:
            self.__fone = v
    def __str__(self):
        return f"ID: {self.__id}\nNome: {self.__nome}\nEmail: {self.__email}\nTelefone: {self.__fone}"


    def to_dict(self): #essa função vai me ajudar a modificar o json agora que está tudo encapsulado
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone
        }




class Clientes:
    objetos = []  
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:    
            with open("clientes.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    cliente = Cliente(
                        id=dic["id"],
                        nome=dic["nome"],
                        email=dic["email"],
                        fone=dic["fone"]
                )
                   
                    cls.objetos.append(cliente)
        except FileNotFoundError:
            pass    

    @classmethod
    def salvar(cls):
        cls.objetos.sort(key=lambda cliente: cliente.get_id())
        with open("clientes.json", mode="w") as arquivo:
            lista_dicts = [cliente.to_dict() for cliente in cls.objetos]
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
        return [str(cliente) for cliente in cls.objetos]
    
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
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()





