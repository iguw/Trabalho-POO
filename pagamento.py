from pedido import Pedido


class Pagamento: #Gerencia os dados e ações relacionados ao pagamento de pedidos
    def __init__(self, id_pagamento, valor, status, forma_pagamento, transacao_id):
        self.id_pagamento = id_pagamento  # Público
        self.status = status  # Público
        self._valor = valor  # Protegido
        self._forma_pagamento = forma_pagamento  # Protegido
        self._pedido = None  # Protegido (associado posteriormente)
        self._reembolsado = False  # Protegido
        self._comprovante = None  # Protegido
        self.__transacao_id = transacao_id  # Privado

    @property
    def id_pagamento(self):
        return self._id_pagamento

    @id_pagamento.setter
    def id_pagamento(self, valor):
        self._id_pagamento = valor

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, novo_valor):
        if novo_valor >= 0:
            self._valor = novo_valor
        else:
            raise ValueError("O valor do pagamento não pode ser negativo.")

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, novo_status):
        self._status = novo_status

    @property
    def forma_pagamento(self):
        return self._forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, forma):
        self._forma_pagamento = forma

    @property
    def pedido(self):
        return self._pedido

    @property
    def transacao_id(self):
        return self.__transacao_id

    @property
    def reembolsado(self):
        return self._reembolsado

    @property
    def comprovante(self):
        return self._comprovante

    def processar_pagamento(self) -> bool: #Processa o pagamento, alterando seu status e gerando comprovante
        if self.validar_pagamento():
            self.status = "Processado"
            self.gerar_comprovante()
            return True
        return False

    def estornar_pagamento(self) -> bool: #Estorna o pagamento se for válido
        if self.status == "Processado" and not self.reembolsado:
            self.status = "Estornado"
            self._reembolsado = True
            return True
        return False

    def validar_pagamento(self) -> bool: #Estorna o pagamento se for válido
        return self.valor > 0 and self.forma_pagamento in ["Débito", "Crédito", "Pix", "Boleto"]

    def gerar_comprovante(self) -> str: #Gera o texto do comprovante de pagamento
        self._comprovante = f"Comprovante: Pagamento de R${self.valor:.2f} via {self.forma_pagamento}."
        return self._comprovante

    def associar_pedido(self, pedido): #Associa o pagamento a um pedido específico
        self._pedido = pedido
