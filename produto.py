
#Representa um produto disponível para venda.
# Atributos:nome (str): Nome do produto., _preco (float)
        




class Produto:
    def __init__(self, nome: str, preco: float):   #Inicializa um novo produto com nome e preço     
        self._nome = nome  # Protegido
        self._preco = preco  # Protegido


    @property #Retorna o nome do produto
    def nome(self):
        return self._nome

  
    @nome.setter
    def nome(self, novo_nome): #Atualiza o nome do produto se for uma string válida
        if isinstance(novo_nome, str):
            self._nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string.")

   
    @property
    def preco(self): #Retorna o preço do produto
        return self._preco

 
    @preco.setter #Atualiza o preço do produto se for um número positivo
    def preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self._preco = novo_preco
        else:
            raise ValueError("O preço deve ser um número positivo.")

 
    def __str__(self): #Retorna uma representação formatada do produto
        return f"{self._nome} - R${self._preco:.2f}"