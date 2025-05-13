class Produto:
    def __init__(self, nome: str, preco: float):
        self._nome = nome  # Protegido
        self._preco = preco  # Protegido


    @property
    def nome(self):
        return self._nome

  
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str):
            self._nome = novo_nome
        else:
            raise ValueError("O nome deve ser uma string.")

   
    @property
    def preco(self):
        return self._preco

 
    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, (int, float)) and novo_preco >= 0:
            self._preco = novo_preco
        else:
            raise ValueError("O preço deve ser um número positivo.")


    def __str__(self):
        return f"{self._nome} - R${self._preco:.2f}"