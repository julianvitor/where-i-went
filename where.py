import exifread, folium, os, sys
from . import coord_converter
from functools import cache

# Função para extrair informações de localização de uma imagem
@cache
def extrair_informacoes_localizacao(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as arquivo_imagem:
        # Redireciona a saída padrão (stdout) e a saída de erro (stderr) para um objeto de captura
        saida_padrao_original = sys.stdout
        saida_erro_original = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')
        try:
            tags = exifread.process_file(arquivo_imagem)
        finally:
            # Restaura a saída padrão e a saída de erro
            sys.stdout.close()
            sys.stderr.close()
            sys.stdout = saida_padrao_original
            sys.stderr = saida_erro_original

    if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
        valores_latitude = tags['GPS GPSLatitude'].values
        valores_longitude = tags['GPS GPSLongitude'].values

        # Converta latitude e longitude usando o módulo em C
        latitude = coord_converter.convert_coordinates(tuple(float(val) for val in valores_latitude))
        longitude = coord_converter.convert_coordinates(tuple(float(val) for val in valores_longitude))

        referencia_latitude = tags['GPS GPSLatitudeRef'].values
        referencia_longitude = tags['GPS GPSLongitudeRef'].values

        latitude, longitude = ajustar_coordenadas(latitude, longitude, referencia_latitude, referencia_longitude)

        return latitude, longitude
    else:
        return None

# Função para ajustar as coordenadas para valores negativos, se necessário
@cache
def ajustar_coordenadas(latitude, longitude, referencia_latitude, referencia_longitude):
    # Verifique se latitude e longitude precisam ser negadas com base nos valores de referência
    if referencia_latitude == 'S':
        latitude = -latitude
    if referencia_longitude == 'W':
        longitude = -longitude

    return latitude, longitude

# Função para criar um mapa com marcadores
def criar_mapa(dados_localizacao, tipo_mapa):
    if tipo_mapa == "satelite":
        m = folium.Map(location=[0, 0], zoom_start=2,tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', attr='Esri')
        for caminho_arquivo, informacao_localizacao in dados_localizacao.items():
            latitude = informacao_localizacao['latitude']
            longitude = informacao_localizacao['longitude']
            folium.Marker((latitude, longitude), popup=caminho_arquivo).add_to(m)
        m.save(f'mapa_{tipo_mapa}.html') # salvar mapa
    elif tipo_mapa == "padrao":
        m = folium.Map(location=[0, 0], zoom_start=2)
        for caminho_arquivo, informacao_localizacao in dados_localizacao.items():
            latitude = informacao_localizacao['latitude']
            longitude = informacao_localizacao['longitude']
            folium.Marker((latitude, longitude), popup=caminho_arquivo).add_to(m)
        m.save(f'mapa_{tipo_mapa}.html')
