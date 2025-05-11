import requests 

def price(api,price_applied:float): 
    price_bitcoin = requests.get(api)
    data = price_bitcoin.json() 
    price =float(data['price'])

    dolar_em_real = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
    brl_response = requests.get(dolar_em_real) 
    usd_to_brl = float(brl_response.json()['USDBRL']['bid'])
    bitcoin_to_real =  price * usd_to_brl 
    my_money = price_applied 
    qtd_brl_bit = float(my_money / bitcoin_to_real)
    


price("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",200)
