import math

# Função para calcular a distância entre dois pontos


def calcular_distancia(lat_a, lon_a, lat_b, lon_b):
    # Raio médio da Terra em milhas
    raio_terra = 3958.8

    # Converter as coordenadas de graus para radianos
    lat_a_rad = math.radians(lat_a)
    lon_a_rad = math.radians(lon_a)
    lat_b_rad = math.radians(lat_b)
    lon_b_rad = math.radians(lon_b)

    # Calcular a diferença entre as coordenadas
    delta_lat = lat_b_rad - lat_a_rad
    delta_lon = lon_b_rad - lon_a_rad

    # Calcular a distância usando a fórmula de Haversine
    a = math.sin(delta_lat / 2) ** 2 + math.cos(lat_a_rad) * \
        math.cos(lat_b_rad) * math.sin(delta_lon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distancia = raio_terra * c

    return distancia


# Obter as coordenadas de A e B do usuário
lat_a = float(input("Digite a latitude de A: "))
lon_a = float(input("Digite a longitude de A: "))
lat_b = float(input("Digite a latitude de B: "))
lon_b = float(input("Digite a longitude de B: "))

# Calcular a distância entre A e B
distancia = calcular_distancia(lat_a, lon_a, lat_b, lon_b)

# Exibir o resultado
print(f"A distância entre A e B é de {distancia} milhas.")
