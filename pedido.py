from datetime import date

class Pedido:
    def __init__(self, id_pedido, status, entrega_prevista, rota, transporte, valor_total, avaliacao_cliente, comentarios):
    
        self.id_pedido = id_pedido  # Público
        self.status = status  # Público
        self._entrega_prevista = entrega_prevista  # Protegido
        self._rota = rota  # Protegido
        self._transporte = transporte  # Protegido
        self._valor_total = valor_total  # Protegido
        self._avaliacao_cliente = avaliacao_cliente  # Protegido
        self._comentarios = comentarios  # Protegido
        
        

   
    @property
    def id_pedido(self):
        return self._id_pedido
    
    @id_pedido.setter
    def id_pedido(self, novo_id):
        self._id_pedido = novo_id

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        self._status = novo_status
    
    @property
    def entrega_prevista(self):
        return self._entrega_prevista

    @entrega_prevista.setter
    def entrega_prevista(self, nova_data):
        if isinstance(nova_data, date):
            self._entrega_prevista = nova_data
        else:
            raise ValueError("A data de entrega prevista deve ser um objeto do tipo date.")

    @property
    def valor_total(self):
        return self._valor_total

    @valor_total.setter
    def valor_total(self, valor):
        if valor >= 0:
            self._valor_total = valor
        else:
            raise ValueError("O valor total não pode ser negativo.")

    @property
    def avaliacao_cliente(self):
        return self._avaliacao_cliente

    @avaliacao_cliente.setter
    def avaliacao_cliente(self, nota):
        if 0 <= nota <= 5:
            self._avaliacao_cliente = nota
        else:
            raise ValueError("A nota deve estar entre 0 e 5 Estrelas.")

    @property
    def comentarios(self):
        return self._comentarios

    @comentarios.setter
    def comentarios(self, texto):
        self._comentarios = texto

    @property
    def transporte(self):
        return self._transporte

    @transporte.setter
    def transporte(self, transporte):
        self._transporte = transporte

    def calcular_valor_entrega(self) -> float:
        if self._rota:
            return len(self._rota) * 5
        return 0.0

    def gerar_rota(self, endereco_origem: str, endereco_destino: str):
        self._rota = [endereco_origem, endereco_destino]

    def atribuir_entregador(self, entregador):
        self.__entregador = entregador

    def atualizar_localizacao(self, coordenada):
        self.__coordenada = coordenada

    def calcular_preco_final(self) -> float:
        return self.valor_total + self.calcular_valor_entrega()

    def registrar_avaliacao(self, nota: int, comentario: str):
        self.avaliacao_cliente = nota
        self.comentarios = comentario
        
        
       
        
        



        
        
        
            
   

