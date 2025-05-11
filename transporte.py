class Coordenada:
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


class Transporte:
    def __init__(self, tipo_veiculo: str, taxa_km: float, tempo_estimado: float, distancia: float):
        self.__tipo_veiculo = tipo_veiculo  # Privado
        self.__taxa_km = taxa_km  # Privado
        self.__tempo_estimado = tempo_estimado  # Privado
        self.__distancia = distancia  # Privado
        self.__atualizar_localizacao = None  # Privado (Coordenada)

    @property
    def tipo_veiculo(self):
        return self.__tipo_veiculo

    @tipo_veiculo.setter
    def tipo_veiculo(self, valor):
        self.__tipo_veiculo = valor

    @property
    def taxa_km(self):
        return self.__taxa_km

    @taxa_km.setter
    def taxa_km(self, valor):
        if valor >= 0:
            self.__taxa_km = valor
        else:
            raise ValueError("A taxa por km não pode ser negativa.")

    @property
    def tempo_estimado(self):
        return self.__tempo_estimado

    @tempo_estimado.setter
    def tempo_estimado(self, valor):
        if valor > 0:
            self.__tempo_estimado = valor
        else:
            raise ValueError("O tempo estimado deve ser positivo.")

    @property
    def distancia(self):
        return self.__distancia

    @distancia.setter
    def distancia(self, valor):
        if valor > 0:
            self.__distancia = valor
        else:
            raise ValueError("A distância deve ser positiva.")

    def calcular_custo(self):
        return self.__taxa_km * self.__distancia

    def calcular_tempo(self):
        return self.__tempo_estimado

    def atualizar_localizacao(self, coord: Coordenada):
        self.__atualizar_localizacao = coord