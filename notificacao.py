from datetime import datetime

class Notificacao:
    def __init__(self, id_notificacao: str, mensagem: str, data_hora: datetime, tipo_usuario: str):
        
        self.__id_notificacao = id_notificacao #privado
        self.__mensagem = mensagem #privado
        self.__data_hora = data_hora #privado
        self.__tipo_usuario = tipo_usuario #privado

    @property
    def id_notificacao(self):
        return self.__id_notificacao

    @id_notificacao.setter
    def id_notificacao(self, valor):
        self.__id_notificacao = valor


    @property
    def mensagem(self):
        return self.__mensagem

    @mensagem.setter
    def mensagem(self, valor):
        self.__mensagem = valor


    @property
    def data_hora(self):
        return self.__data_hora

    @data_hora.setter
    def data_hora(self, valor):
        if isinstance(valor, datetime):
            self.__data_hora = valor
        else:
            raise ValueError("data_hora deve ser um objeto datetime")

    @property
    def tipo_usuario(self):
        return self.__tipo_usuario

    @tipo_usuario.setter
    def tipo_usuario(self, valor):
        self.__tipo_usuario = valor
        
        
    
