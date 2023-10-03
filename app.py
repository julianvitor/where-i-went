import exifread,folium,json,os,time,coord_converter
from tqdm import tqdm
from functools import cache

# Função para extrair informações de localização de uma imagem
@cache
def extract_location_info(file_path):
    with open(file_path, 'rb') as image_file:
        tags = exifread.process_file(image_file)

    if 'GPS GPSLatitude' in tags and 'GPS GPSLongitude' in tags:
        latitude_values = tags['GPS GPSLatitude'].values
        longitude_values = tags['GPS GPSLongitude'].values

        # Converta latitude e longitude usando o módulo em C
        latitude = coord_converter.convert_coordinates(tuple(float(val) for val in latitude_values))
        longitude = coord_converter.convert_coordinates(tuple(float(val) for val in longitude_values))

        latitude_ref = tags['GPS GPSLatitudeRef'].values
        longitude_ref = tags['GPS GPSLongitudeRef'].values

        latitude, longitude = adjust_coordinates(latitude, longitude, latitude_ref, longitude_ref)

        return latitude, longitude
    else:
        return None

# Função para ajustar as coordenadas para valores negativos, se necessário
def adjust_coordinates(latitude, longitude, latitude_ref, longitude_ref):
    # Verifique se latitude e longitude precisam ser negadas com base nos valores de referência
    if latitude_ref == 'S':
        latitude = -latitude
    if longitude_ref == 'W':
        longitude = -longitude

    return latitude, longitude

# Função para criar um mapa com marcadores
def create_map(location_data, map_type):
    if map_type == "satellite":
        m = folium.Map(location=[0, 0], zoom_start=2,tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', attr='Esri')
        for image_path, location_info in location_data.items():
            latitude = location_info['latitude']
            longitude = location_info['longitude']
            folium.Marker((latitude, longitude), popup=image_path).add_to(m)
        m.save(f'map_{map_type}.html')#save map
    elif map_type == "standard":
        m = folium.Map(location=[0, 0], zoom_start=2)
        for image_path, location_info in location_data.items():
            latitude = location_info['latitude']
            longitude = location_info['longitude']
            folium.Marker((latitude, longitude), popup=image_path).add_to(m)
        m.save(f'map_{map_type}.html')
    

# Função principal
def main():
    start_time = time.time()

    # Pasta contendo as imagens
    image_folder = 'images'

    # Lista para armazenar os caminhos das imagens
    image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith(('.jpg', '.jpeg'))]

    # Dicionário para armazenar os dados de localização
    location_data = {}

    # Use tqdm para criar uma barra de progresso durante a extração de dados
    for image_path in tqdm(image_paths, desc='Extraindo dados de localização'):
        location_info = extract_location_info(image_path)
        if location_info:
            latitude, longitude = location_info
            location_data[image_path] = {'latitude': latitude, 'longitude': longitude}

    # Salve os dados em um arquivo JSON
    with open('location_data.json', 'w') as json_file:
        json.dump(location_data, json_file, indent=4)

    # Crie mapas
    create_map(location_data, "standard")
    create_map(location_data, "satellite")

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Tempo de execução: {execution_time:.2f} segundos")

if __name__ == "__main__":
    main()