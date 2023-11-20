import requests ## fazer solicitacao na APT
from urllib.parse import quote #usar caracteris em uma string
import schedule #agendador de tarefas
import time #funcao para usar o sleep
import os #comunicar com o so

API_KEY = '2836b58e0733aaaff8ef7dbb4ebb6727'
CITY_NAME = 'itajai'
CITY_NAME_ENCODED = quote(CITY_NAME)
API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY_NAME_ENCODED}&appid={API_KEY}'

def obter_dados_meteorologicos(): #faz solicitacao a api, deu certo volta os dados, deu errado retorna None
	resposta = requests.get(API_URL)

	if resposta.status_code == 200: 
		dados = resposta.json()
		return dados	
		
	else: 
		print (f"Erro na solicitação: {resposta.status_code}")
		return None
