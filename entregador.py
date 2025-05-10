from typing import List
from datetime import date
from pedido import Pedido



class Entregador:
    
    def __init__(self, nome: str, transporte_tipo: str, capacidade_carga: float, media_avaliacoes: float = 0.0):
        self.__nome = nome  # privado
        self.__transporte_tipo = transporte_tipo   # privado
        self.__capacidade_carga = capacidade_carga # privado
        self.__media_avaliacoes = media_avaliacoes # privado
        self.__entregas_finalizadas = [] # privado

   
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

   
    @property
    def transporte_tipo(self):
        return self.__transporte_tipo

    @transporte_tipo.setter
    def transporte_tipo(self, valor):
        self.__transporte_tipo = valor


    @property
    def capacidade_carga(self):
        return self.__capacidade_carga

    @capacidade_carga.setter
    def capacidade_carga(self, valor):
        self.__capacidade_carga = valor

    @property
    def media_avaliacoes(self):
        return self.__media_avaliacoes

    @media_avaliacoes.setter
    def media_avaliacoes(self, valor):
        self.__media_avaliacoes = valor

def aceitar_entrega(self, pedido):
        pedido.atribuir_entregador(self)
        pedido.status = "Em andamento"
        print(f"Entrega {pedido.id_pedido} aceita por {self.__nome}")
        
        
def finalizar_entrega(self, pedido):
        pedido.status = "Entregue"
        self.__entregas_finalizadas.append(pedido)
        print(f"Entrega {pedido.id_pedido} finalizada.")
 
def listar_entregas_finalizadas(self) -> List:
        return self.__entregas_finalizadas