import exifread
import folium
import json
import os
import webbrowser
from tqdm import tqdm

def extract_location_info(file_path):
    # Abre o arquivo da imagem em modo de leitura binária
    with open(file_path, 'rb') as image_file:
        # Lê os metadados EXIF da imagem
        tags = exifread.process_file(image_file)
    
    # Verifica se as informações de localização estão presentes nos metadados
    if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
        latitude = tags['GPS GPSLatitude'].values
        longitude = tags['GPS GPSLongitude'].values
        latitude_ref = tags['GPS GPSLatitudeRef'].values
        longitude_ref = tags['GPS GPSLongitudeRef'].values

        # Converte as coordenadas de graus, minutos e segundos para decimal
        latitude = float(latitude[0].num) / float(latitude[0].den) + \
                   float(latitude[1].num) / (float(latitude[1].den) * 60) + \
                   float(latitude[2].num) / (float(latitude[2].den) * 3600)
        longitude = float(longitude[0].num) / float(longitude[0].den) + \
                    float(longitude[1].num) / (float(longitude[1].den) * 60) + \
                    float(longitude[2].num) / (float(longitude[2].den) * 3600)

        # Converte a latitude e longitude para valores negativos, se necessário
        if latitude_ref == 'S':
            latitude = -latitude
        if longitude_ref == 'W':
            longitude = -longitude

        return latitude, longitude
    else:
        return None

def main():
    # Pasta contendo as imagens
    image_folder = 'images'

    # Lista para armazenar os caminhos das imagens
    image_paths = []

    # Itera sobre os arquivos na pasta e adiciona os caminhos das imagens à lista
    for filename in os.listdir(image_folder):
        if filename.endswith(('.jpg', '.jpeg')):
            image_paths.append(os.path.join(image_folder, filename))

    # Dicionário para armazenar os dados de localização
    location_data = {}

    # Use tqdm para criar uma barra de progresso durante a extração de dados
    for image_path in tqdm(image_paths, desc='Extraindo dados de localização'):
        location_info = extract_location_info(image_path)
        if location_info:
            latitude, longitude = location_info
            location_data[image_path] = {'latitude': latitude, 'longitude': longitude}

    # Salva os dados em um arquivo JSON
    with open('location_data.json', 'w') as json_file:
        json.dump(location_data, json_file, indent=4)

    # Cria um mapa
    map_satellite = folium.Map(location=[0, 0], zoom_start=2, tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', attr='Esri')

    map_standard = folium.Map(location=[0, 0], zoom_start=2)

    # Use tqdm para criar uma barra de progresso durante a criação de marcadores no mapa
    for image_path, location_info in tqdm(location_data.items(), desc='Adicionando marcadores ao mapa'):
        latitude = location_info['latitude']
        longitude = location_info['longitude']
        folium.Marker([latitude, longitude], popup=image_path).add_to(map_standard)

    for image_path, location_info in tqdm(location_data.items(), desc='Adicionando marcadores ao mapa de satélite'):
        latitude = location_info['latitude']
        longitude = location_info['longitude']
        folium.Marker([latitude, longitude], popup=image_path).add_to(map_satellite)

    # Salva os mapas em arquivos HTML
    map_standard.save('map.html')
    map_satellite.save('map_satellite.html')

    # Tenta abrir o mapa no navegador
    try:
        webbrowser.open('map.html')
    except Exception as e:
        error_message = f'Erro ao abrir o navegador: {e}'
        print(error_message)
        print('Por favor, abra o arquivo "map.html" em seu navegador manualmente.')

if __name__ == "__main__":
    main()
