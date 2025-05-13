class Conta:
    def __init__(self, id_conta, nome_cliente, email, telefone, endereco, tipo_usuario):
        self.id_conta = id_conta  # Público
        self.nome_cliente = nome_cliente  # Público
        self.email = email  # Público
        self.telefone = telefone  # Público
        self._endereco = endereco  # Protegido
        self.__senha = None  # Privado  
        self.tipo_usuario = tipo_usuario
        self.usuario = None
        
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
        
        
        
        
class Autenticador:
    def __init__(self):
        self.__contas = []

    def cadastrar_conta(self, conta: Conta):
        self.__contas.append(conta)

    def autenticar(self, email: str, senha: str):
        for conta in self.__contas:
            if conta.autenticar(email, senha):
                print(f"Autenticação bem-sucedida para: {conta.nome_cliente}")
                return conta
        print("Falha na autenticação.")
        return None

    def validar_senha(self, senha: str):
        return len(senha) >= 8

    def enviar_email_recuperacao(self):
        print("E-mail de recuperação enviado.") 

    def enviar_codigo_verificacao(self):
        print("Código de verificação enviado.")  