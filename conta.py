class Conta: #Representa uma conta de usuário no sistema
    def __init__(self, id_conta, nome_cliente, email, telefone, endereco, tipo_usuario): #Inicializa a conta com as informações fornecidas
        self.id_conta = id_conta  # Público
        self.nome_cliente = nome_cliente  # Público
        self.email = email  # Público
        self.telefone = telefone  # Público
        self._endereco = endereco  # Protegido
        self.__senha = None  # Privado  
        self.tipo_usuario = tipo_usuario
        self.usuario = None
        
    @property
    def senha(self): #Retorna a senha da conta
        return self.__senha    
    
    @senha.setter #Define uma nova senha se tiver pelo menos 8 caracteres
    def senha(self, nova_senha):
        if len(nova_senha) >= 8:
            self.__senha = nova_senha
        else:
            raise ValueError("A senha deve ter pelo menos 8 caracteres.")


    def autenticar(self,email,senha): #Verifica se o email e senha correspondem à conta
        return self.email == email and self.__senha == senha

    def alterar_senha(self, nova_senha): #Altera a senha da conta.
        self.senha = nova_senha

    def alterar_endereco(self, novo_endereco): #Atualiza o endereço da conta
        self._endereco = novo_endereco
        
        
        
        
class Autenticador: #Gerencia o cadastro e autenticação de contas no sistema.
    def __init__(self):
        self.__contas = []

    def cadastrar_conta(self, conta: Conta): #Adiciona uma nova conta à lista de contas
        self.__contas.append(conta)

    def autenticar(self, email: str, senha: str): #Autentica um usuário com base em email e senha
        for conta in self.__contas:
            if conta.autenticar(email, senha):
                print(f"Autenticação bem-sucedida para: {conta.nome_cliente}")
                return conta
        print("Falha na autenticação.")
        return None

    def validar_senha(self, senha: str): #Verifica se a senha atende aos requisitos mínimos
        return len(senha) >= 8

    def enviar_email_recuperacao(self):
        print("E-mail de recuperação enviado.") 

    def enviar_codigo_verificacao(self):
        print("Código de verificação enviado.")  