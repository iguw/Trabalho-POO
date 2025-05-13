from datetime import date
from pedido import Pedido


class Cliente:
    
    def __init__(self, nome: str, endereco: str, telefone: str, email: str, senha: str):
    
        self._nome = nome #privado
        self._endereco = endereco #privado
        self._telefone = telefone #privado
        self._email = email #privado
        self._senha = senha #privado
        self.historico_pedidos = []

    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        self._nome = nome

  
    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self._endereco = endereco

    @property
    def telefone(self):
        return self._telefone  
    
    @telefone.setter
    def telefone(self, telefone: str):
        self._telefone = telefone

   
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email: str):
        self._email = email

   
    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha: str):
        self._senha = senha
        
        
    def solicitar_pedido(self, id_pedido, entrega_prevista, transporte, valor_total, endereco_destino):
        pedido = Pedido(
            id_pedido,
            status="Criado",
            entrega_prevista=entrega_prevista,
            rota=[self.endereco, endereco_destino],
            transporte=transporte,
            valor_total=valor_total,
            avaliacao_cliente=None,
            comentarios=""
        )
        self.historico_pedidos.append(pedido)
        return pedido
     
    def visualizar_historico_pedidos(self):
        return self.historico_pedidos

    def atualizar_endereco(self, novo_endereco):
        self.endereco = novo_endereco

    def avaliar_entrega(self, pedido, nota, comentario):
        pedido.registrar_avaliacao(nota, comentario)
        
        
    def cancelar_pedido(self, pedido):
        pedido.status = "Cancelado"
        return True
    