import requests


def get_price(symbol, to_symbol='USDT'):
    """ Obtener el precio de alguna criptomoneda """
    url = f'https://api2.binance.com/api/v3/ticker/24hr?symbol={symbol}{to_symbol}'
    response = requests.get(url)

    # devuelvo todos los datos
    data = response.json()
    return data
