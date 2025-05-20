class vendedor: #Representa um vendedor com informações da empresa e produtos ofertados
    def __init__ (self,nome_empresa, endereco, telefone, cnpj, email):
        self.nome_empresa = nome_empresa # Público
        self.endereco = endereco # Público
        self.telefone = telefone # Público
        self.cnpj = cnpj # Público
        self.email = email # Público
        self._pedidos_recebidos = []
        self.produtos = []
        
        


    @property
    def nome_empresa(self):
        return self._nome_empresa
    
    @nome_empresa.setter
    def nome_empresa(self, nome_empresa):
        self._nome_empresa = nome_empresa

    @property
    def endereco(self):
        return self._endereco
    
    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def telefone(self):
        return self._telefone
    
    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def cnpj(self):
        return self._cnpj
    
    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj
    
    

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def pedidos_recebidos(self): 
        return self._pedidos_recebidos
    
    
    
    def adicionar_pedido(self, pedido): #Adiciona um pedido à lista de pedidos recebidos
        self._pedidos_recebidos.append(pedido)

    def visualizar_pedidos_recebidos(self): #Retorna a lista de pedidos recebido
        return self._pedidos_recebidos
    
    def excluir_pedido(self, id_pedido): #Exclui um pedido da lista de pedidos recebidos pelo ID
        self._pedidos_recebidos = [pedido for pedido in self._pedidos_recebidos if pedido.id != id_pedido]
    
    
    
        

  

