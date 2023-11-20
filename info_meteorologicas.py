import requests ## fazer solicitacao na APT
from urllib.parse import quote #usar caracteris em uma string
import schedule #agendador de tarefas
import time #funcao para usar o sleep
import os #comunicar com o so

print("Teste 1")

API_KEY = '2836b58e0733aaaff8ef7dbb4ebb6727'
LATITUDE = -26.908278
LONGITUDE = -48.677511
API_URL = f'http://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}'

print("Teste 2")

def obter_dados_meteorologicos(): #faz solicitacao a api, deu certo volta os dados, deu errado retorna None
    resposta = requests.get(API_URL)

    if resposta.status_code == 200:
        dados = resposta.json()
        return dados
    else:
        print(f"Erro na solicitação: {resposta.status_code}")
        return None

print("Teste 3")

def enviar_sinal(dados): #manda uma mensagem com base nos dados e imprimi no terminal
    mensagem = f"Sinal enviado para ({LATITUDE}, {LONGITUDE}): {dados['weather'][0]['description']}"
    os.system(f"echo '{mensagem}' >> a.txt")
    print(mensagem)

print("Teste 4")

