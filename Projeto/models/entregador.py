import json


class Entregador:
    def __init__(self, nome, email, fone, senha, id=0):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    # getters
    def get_id(self):
        return self.__id


    def get_nome(self):
        return self.__nome


    def get_email(self):
        return self.__email


    def get_fone(self):
        return self.__fone
        
    def get_senha(self):
        return self.__senha


    # setters
    def set_id(self, v):
        v = int(v)  # conversão segura para inteiro
        if v < 0:
            raise ValueError("ID não pode ser negativo")
        else:
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

    def set_senha(self, v):
        if v== "":
            raise ValueError("Senha não pode estar em branco")
        else:
            self.__senha = v


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
            "fone": self.__fone,
             "senha": self.__senha 
        }
class Entregadores:
    objetos = []  
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:    
            with open("entregadores.json", mode="r") as arquivo:
                s = json.load(arquivo)
                for dic in s:
                    entregador = Entregador(
                        id=dic["id"],
                        nome=dic["nome"],
                        email=dic["email"],
                        fone=dic["fone"],
                        senha=dic["senha"]
                )
                    cls.objetos.append(entregador)
        except FileNotFoundError:
            pass    

    @classmethod
    def salvar(cls):
        cls.objetos.sort(key=lambda entregador: entregador.get_id())
        with open("entregadores.json", mode="w") as arquivo:
            lista_dicts = [entregador.to_dict() for entregador in cls.objetos]
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
        return [str(entregador) for entregador in cls.objetos]

    @classmethod
    def listar_objetos(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id: return obj
        return None               
    
    @classmethod
    def atualizar(cls, obj_atualizado):
        cls.abrir()
        
        for i, obj in enumerate(cls.objetos):
            if obj.get_id() == obj_atualizado.get_id():
                try:
                    # Atualiza TODOS os campos do objeto existente
                    obj.set_nome(obj_atualizado.get_nome())
                    obj.set_email(obj_atualizado.get_email())
                    obj.set_fone(obj_atualizado.get_fone())
                    obj.set_senha(obj_atualizado.get_senha())
                    cls.salvar()  # Salva as alterações
                    return True
                except ValueError as e:
                    raise ValueError(f"Dados inválidos: {e}")
    
    @classmethod
    def excluir(cls, obj):
        x = cls.listar_id(obj.get_id())
        if x != None: 
            cls.objetos.remove(x)
            cls.salvar()







