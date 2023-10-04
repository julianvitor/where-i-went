import json, os, time
from tqdm import tqdm
from where import *
def main():
    tempo_inicio = time.time()
    pasta_imagens = 'images'
    dados_localizacao = {}
    extensoes_suportadas = ('.jpg', '.jpeg')
    # Lista para armazenar os caminhos das imagens, excluindo arquivos não suportados
    caminhos_imagens = [
        os.path.join(pasta_imagens, nome_arquivo)
        for nome_arquivo in os.listdir(pasta_imagens)
        if nome_arquivo.lower().endswith(extensoes_suportadas)
    ]
   
    # Use tqdm para criar uma única barra de progresso que abranja todo o processo
    with tqdm(total=len(caminhos_imagens), desc='Processando imagens') as barra_progresso:
        for caminho_arquivo in caminhos_imagens:
            informacao_localizacao = extrair_informacoes_localizacao(caminho_arquivo)
            if informacao_localizacao:
                latitude, longitude = informacao_localizacao
                dados_localizacao[caminho_arquivo] = {'latitude': latitude, 'longitude': longitude}
            barra_progresso.update(1)  # Atualize a barra de progresso a cada imagem processada
            
    # Salve os dados em um arquivo JSON
    with open('dados_localizacao.json', 'w') as arquivo_json:
        json.dump(dados_localizacao, arquivo_json, indent=4)

    # Crie mapas
    criar_mapa(dados_localizacao, "padrao")
    criar_mapa(dados_localizacao, "satelite")

    tempo_fim = time.time()
    tempo_execucao = tempo_fim - tempo_inicio
    print(f"Tempo de execução: {tempo_execucao:.2f} segundos")

if __name__ == "__main__":
    main()
