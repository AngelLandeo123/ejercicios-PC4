import requests
url = '	https://images.unsplash.com/photo-1583511655826-05…fDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1376&q=80'
respuesta = requests.get(url)
with open('imagentierna.jpg','wb') as f:
    f.write(respuesta.content)
    pass


