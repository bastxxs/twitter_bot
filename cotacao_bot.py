import tweepy
import time
from datetime import datetime, timedelta
import requests


consumer_key = 'XXXXXXXXXX'
consumer_secret = 'XXXXXXXXXX'
access_token = 'XXXXXXXXXX'
access_token_secret = 'XXXXXXXXXX'


api_cotacao = "http://api.exchangeratesapi.io/v1/latest?access_key=86f3a9da78b0e2d98c519f582fdc835b"

# Autenticar com a API do Twitter

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Defina o horário em que deseja que o bot tweete (por exemplo, 13:00)
hora_do_tweet = datetime.now().replace(hour=13, minute=0, second=0, microsecond=0)




def retorna_dados():

    response = requests.get(api_cotacao)
    
    
    if response.status_code == 200:
      
      moeda_principal = 'BRL'
      moeda_origem = 'EUR'
      dados = response.json()
     
      if moeda_principal in dados['rates']:
          # nome_moeda = dados['rates']
           valor_moeda = dados['rates'][moeda_principal]
          
           valor_formatado = round(valor_moeda, 2)

           data = dados['date']
           data_formatada = datetime.strptime(data, '%Y-%m-%d')
           data_final = data_formatada.strftime('%d-%m-%Y')
        
           return f"{data_final}\n1 {moeda_origem} = {valor_formatado} {moeda_principal}"

retorna_dados()

def tweetar_mensagem(mensagem):

    try:
    
        api.update_status(mensagem)
        print(f"Tweet enviado: {mensagem}")
    
    except tweepy.HTTPException as e:

        print(f"Erro ao enviar tweet: {str(e)}")

while True:
    
    agora = datetime.now()
    
    if agora >= hora_do_tweet:
        
        tweetar_mensagem(retorna_dados())
        
        hora_do_tweet = hora_do_tweet + timedelta(days=1)
    
    time.sleep(120)
