import time

def ejecutaScript():
    #Aquí agregas en contenido de tu script o ejecutas el script dentro de un archivo .py.
    
    exec(open("data1.py").read()) 
    print('Ejecutando Script...')
    time.sleep(15)

while True:
    ejecutaScript()
