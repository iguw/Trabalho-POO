class Coordenada: #Representa uma coordenada geográfica com latitude e longitude
    def __init__(self, latitude: float, longitude: float):
        self.latitude = latitude
        self.longitude = longitude


class Transporte: #Representa um meio de transporte utilizado para entrega, com cálculo de custo e tempo
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

    @tempo_estimado.setter  #Define a taxa por quilômetro, raises ValueError: Se o valor for negativo
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

    def calcular_custo(self): #Calcula o custo total da entrega com base na distância e taxa por km, igual o tempo estimado usei um valor fixo
        return self.__taxa_km * self.__distancia

    def calcular_tempo(self): #Retorna o tempo estimado de entrega
        return self.__tempo_estimado

    def atualizar_localizacao(self, coord: Coordenada): #Atualiza a última localização conhecida do transporte
        self.__atualizar_localizacao = coord