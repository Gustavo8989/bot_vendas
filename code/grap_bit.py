import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import requests 
import time

def price(api,price_applied:float,frame):
    # Bitcoin 
    price_bitcoin = requests.get(api)
    data = price_bitcoin.json() 
    price =float(data['price'])
    # Real and Dolar 
    dolar_em_real = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    brl_response = requests.get(dolar_em_real) 
    usd_to_brl = float(brl_response.json()['USDBRL']['bid'])
    # Conversão 
    bitcoin_to_real =  price * usd_to_brl 
    my_money = price_applied 
    qtd_brl_bit = float(my_money / bitcoin_to_real)
    my_money_all = qtd_brl_bit * bitcoin_to_real
    print(price_bitcoin)




if __name__ == "__main__":
    while True:
        price("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",200,100)
        print('-'*40) 
        time.sleep(3600) 

