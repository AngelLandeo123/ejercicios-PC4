
import requests
url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
respuesta = requests.get(url)
respuesta.json()
data = respuesta.json()
       
colum = []
columnas = 'Fecha,Codigo,Moneda,Precio\n'
colum.append(columnas)


fecha = data['time']['updated']
codigo = data["bpi"]['USD']["code"]
moneda = data["bpi"]["USD"]["description"]
precio = data["bpi"]["USD"]["rate_float"]
   
texto_fila = f'{fecha},{codigo},{moneda},{precio}\n' 
colum.append(texto_fila)
        

with open('Precio_bitcoin.txt','w') as archico:
    archico.writelines(colum)

with open('Precio_bitcoin.csv','w') as archico:
    archico.writelines(colum)


