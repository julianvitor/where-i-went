import unittest, os
from app import extrair_informacoes_localizacao, ajustar_coordenadas, criar_mapa

class TestApp(unittest.TestCase):

    def test_extrair_informacoes_localizacao(self):
        caminho_arquivo_teste = 'test.jpg'
        
        # Chama a função para extrair informações de localização
        latitude, longitude = extrair_informacoes_localizacao(caminho_arquivo_teste)
        
        # Valores esperados das coordenadas
        valor_esperado_da_latitude = 43.46744833333334
        valor_esperado_da_longitude = 11.885126666663888
        
        # Verifica se as coordenadas extraídas estão corretas
        self.assertAlmostEqual(latitude, valor_esperado_da_latitude, places=6)
        self.assertAlmostEqual(longitude, valor_esperado_da_longitude, places=6)

    def test_ajustar_coordenadas(self):
        # Teste casos de referência 'S' e 'W'
        latitude1, longitude1 = ajustar_coordenadas(10.0, 20.0, 'S', 'W')
        self.assertEqual(latitude1, -10.0)
        self.assertEqual(longitude1, -20.0)

        # Teste casos de referência diferentes de 'S' e 'W'
        latitude2, longitude2 = ajustar_coordenadas(30.0, 40.0, 'N', 'E')
        self.assertEqual(latitude2, 30.0)
        self.assertEqual(longitude2, 40.0)
    
    def test_criar_mapa(self):
        # Dados de localização fictícios para o teste
        dados_localizacao = {
            'imagem1.jpg': {'latitude': 40.0, 'longitude': -70.0},
            'imagem2.jpg': {'latitude': 45.0, 'longitude': -75.0},
        }

        criar_mapa(dados_localizacao, "padrao")
        self.assertTrue(os.path.exists('mapa_padrao.html'))

        criar_mapa(dados_localizacao, "satelite")
        self.assertTrue(os.path.exists('mapa_satelite.html'))

        os.remove('mapa_padrao.html')
        os.remove('mapa_satelite.html') 

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(verbosity=2))
