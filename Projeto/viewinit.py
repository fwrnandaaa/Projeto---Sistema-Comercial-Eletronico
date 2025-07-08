class View:
    # ... outros métodos ...
    
    @staticmethod
    def cliente_autenticar(email, senha):
        try:
            clientes = Clientes.listar_objetos()
            # ... resto do método ...
        except Exception as e:
            print(f"Erro ao autenticar: {str(e)}")
            return None