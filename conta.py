class Conta:
    def __init__(self, id_conta, nome_cliente, email, telefone, endereco):
        self.id_conta = id_conta  # Público
        self.nome_cliente = nome_cliente  # Público
        self.email = email  # Público
        self.telefone = telefone  # Público
        self._endereco = endereco  # Protegido
        self.__senha = None  # Privado  
        
    @property
    def senha(self):
        return self.__senha    
    
    @senha.setter
    def senha(self, nova_senha):
        if len(nova_senha) >= 8:
            self.__senha = nova_senha
        else:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")


    def autenticar(self,email,senha):
        return self.email == email and self.__senha == senha

    def alterar_senha(self, nova_senha):
        self.senha = nova_senha

    def alterar_endereco(self, novo_endereco):
        self._endereco = novo_endereco