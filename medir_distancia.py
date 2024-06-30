
import requests

def obtener_distancia(ciudad_origen, ciudad_destino):
    
    api_url = f"https://api.distancia.com/{ciudad_origen}/{ciudad_destino}"
    respuesta = requests.get(api_url)
    datos = respuesta.json()
    return datos

while True:
    ciudad_origen = input("Ciudad de Origen: ")
    ciudad_destino = input("Ciudad de Destino: ")
    
    if ciudad_origen.lower() == 's' or ciudad_destino.lower() == 's':
        break
    
    distancia = obtener_distancia(ciudad_origen, ciudad_destino)
    
    print(f"Distancia en millas: {distancia['millas']}")
    print(f"Distancia en kilómetros: {distancia['kilometros']}")
    print(f"Duración del viaje: {distancia['duracion']}")
    print(f"Narrativa del viaje: {distancia['narrativa']}")
    
    medio_transporte = input("Elija el medio de transporte: ")

