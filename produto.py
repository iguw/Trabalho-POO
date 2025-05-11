class Pedido:
    def __init__(self,status, data_criacao, entrega_prevista, rota, transporte, avaliacao_cliente, comentarios):
        self._status = status #Protegido
        self._data_criacao = data_criacao  #Protegido
        self._entrega_prevista = entrega_prevista #Protegido
        self._rota = rota #Protegido
        self._transporte = transporte  #Protegido
        self._avaliacao_cliente = avaliacao_cliente  #Protegido
        self._comentarios = comentarios #Protegido
        self.__entregador = None #Privado
        self.__coordenada = None #Privado

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    @property
    def data_criacao(self):
        return self._data_criacao

    @property
    def entrega_prevista(self):
        return self._entrega_prevista

    @entrega_prevista.setter
    def entrega_prevista(self, nova_data):
        self._entrega_prevista = nova_data

    @property
    def rota(self):
        return self._rota

    @rota.setter
    def rota(self, nova_rota):
        self._rota = nova_rota

    @property
    def transporte(self):
        return self._transporte

    @transporte.setter
    def transporte(self, novo_transporte):
        self._transporte = novo_transporte

    @property
    def avaliacao_cliente(self):
        return self._avaliacao_cliente

    @avaliacao_cliente.setter
    def avaliacao_cliente(self, nota):
        self._avaliacao_cliente = nota

    @property
    def comentarios(self):
        return self._comentarios

    @comentarios.setter
    def comentarios(self, texto):
        self._comentarios = texto
        
        
    def registrar_avaliacao(self, nota, comentario):  
        self._avaliacao_cliente = nota
        self._comentarios = comentario
        
        
    def atribuir_entregador(self, entregador):  
        self.__entregador = entregador
        
        
    def atualizar_localizacao(self, coordenada):  
        self.__coordenada = coordenada