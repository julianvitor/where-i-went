# Where-I-Went Library

A Where-I-Went Library é uma biblioteca Python que permite extrair informações de geolocalização de imagens JPEG (ou JPG) e criar mapas interativos com base nesses dados. Esta biblioteca foi originalmente desenvolvida como parte do projeto Where-I-Went, mas agora está disponível como uma biblioteca independente que pode ser incorporada em outros projetos.

## Funções Disponíveis

A Where-I-Went Library fornece as seguintes funções:

### `extrair_informacoes_localizacao(caminho_arquivo)`
- Esta função extrai informações de geolocalização de uma imagem JPEG dada o caminho do arquivo.
- Retorna um dicionário com as informações de latitude e longitude, ou None se as informações não estiverem disponíveis na imagem.

### `ajustar_coordenadas(latitude, longitude, referencia_latitude, referencia_longitude)`
- Esta função ajusta as coordenadas de latitude e longitude com base nas referências (N, S, E, W) fornecidas.
- Retorna as coordenadas de latitude e longitude ajustadas.

### `criar_mapa(dados_localizacao, tipo_mapa)`
- Esta função cria mapas interativos com marcadores com base nos dados de geolocalização fornecidos.
- Os mapas podem ser criados nos estilos "satélite" ou "padrão".

## Como Instalar

Você pode instalar a Where-I-Went Library usando o `pip`, que é o gerenciador de pacotes Python padrão. Siga os passos abaixo para instalar a biblioteca:

1. Abra um terminal, clone o repositorio.

2. Execute o seguinte comando para instalar a biblioteca diretamente do repositório do PyPI (Python Package Index):

`pip install where-i-went`
Isso instalará a Where-I-Went Library no seu ambiente Python local.

Uso da Biblioteca
A aplicação original Where-I-Went está disponível no arquivo app.py. Você pode usá-lo como referência para aprender como usar a Where-I-Went Library em seus próprios projetos.

Certifique-se de ter uma pasta chamada "images" no mesmo diretório do seu projeto e adicione suas imagens JPEG nessa pasta. A partir daí, você pode importar as funções da biblioteca e usá-las para extrair informações de geolocalização e criar mapas interativos com base nas suas imagens.

Divirta-se explorando o mundo com a Where-I-Went Library!

[Where-I-Went](https://github.com/julianvitor/where-i-went)

***

# Where-I-Went Library

The Where-I-Went Library is a Python library that allows you to extract geolocation information from JPEG (or JPG) images and create interactive maps based on this data. This library was originally developed as part of the Where-I-Went project but is now available as an independent library that can be incorporated into other projects.

## Available Functions

The Where-I-Went Library provides the following functions:

### `extrair_informacoes_localizacao(caminho_arquivo)`
- This function extracts geolocation information from a JPEG image given the file path.
- It returns a dictionary with latitude and longitude information, or None if the information is not available in the image.

### `ajustar_coordenadas(latitude, longitude, referencia_latitude, referencia_longitude)`
- This function adjusts latitude and longitude coordinates based on the provided references (N, S, E, W).
- It returns the adjusted latitude and longitude coordinates.

### `criar_mapa(dados_localizacao, tipo_mapa)`
- This function creates interactive maps with markers based on geolocation data provided.
- Maps can be created in "satellite" or "standard" styles.

## How to Install

You can install the Where-I-Went Library using `pip`, which is the standard Python package manager. Follow the steps below to install the library:

1. Open a terminal, Clone the repo.

2. Execute the following command to install the library directly from the PyPI (Python Package Index) repository:

`pip install where-i-went`
This will install the Where-I-Went Library in your local Python environment.

Library Usage
The original Where-I-Went application is available in the app.py file. You can use it as a reference to learn how to use the Where-I-Went Library in your own projects.

Make sure you have a folder named "images" in the same directory as your project and add your JPEG images to that folder. From there, you can import the library's functions and use them to extract geolocation information and create interactive maps based on your images.

Enjoy exploring the world with the Where-I-Went Library!

[Where-I-Went](https://github.com/julianvitor/where-i-went)
