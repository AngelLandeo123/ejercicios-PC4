import requests
import locale
try:
    n = float(input("Ingrese la cantidad de bitcoins: "))
    locale.setlocale(locale.LC_ALL, '')
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    respuesta = requests.get(url)
    respuesta.json()
    data = respuesta.json()
    precio = float(data["bpi"]["USD"]["rate"].replace(",", ""))
    valor_total = n * precio
    formato_decimal = locale.format_string("%.4f", valor_total, grouping=True)
    print(f"El costo actual de {n} bitcoins en USD es {formato_decimal}")
except requests.RequestException:
    print("Valor invalido.")

#print(data)


