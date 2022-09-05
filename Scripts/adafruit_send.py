from Adafruit_IO import Client
import time
from datetime import datetime

ADAFRUIT_IO_KEY = 'aio_GEWr22EO5KFqQFFUFqQecBH13wTH'
ADAFRUIT_IO_USERNAME = 'laravaz' 
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

count = 0
normalizador = -1
lista=[]
feed = aio.data('mariana-treinos')
print('///////////////   A ENVIAR PARA GOOGLE SHEET...  ///////////////////')
for d in feed:
    
    dado = format(d.value)
    #print(dado)
    
    part = dado.split(';')
    data_freq = part[0]
    freq = part[1]
    
    
    data_conv = datetime.strptime(data_freq,'%Y-%m-%d %H:%M:%S')
    print(data_freq,' ',freq,'\n')
    
    
    # timeout so we dont flood adafruit-io with requests
    time.sleep(0.25)
    # Definir o intervalo de treino no dia correspondente. Ver no google sheet 'Treinos'
    if data_conv > (datetime.strptime('2022-03-27 13:19:00','%Y-%m-%d %H:%M:%S')):
        #Tempo final do treino + 4 minutos
        #print("Fora do intervalo")
        continue

    elif data_conv >= (datetime.strptime('2022-03-27 12:55:00','%Y-%m-%d %H:%M:%S')) and data_conv <= (datetime.strptime('2022-03-27 13:19:00','%Y-%m-%d %H:%M:%S')):
        #Tempo inicial do treino - 4 minutos e Tempo final do treino + 4 minutos
        #print("Passou")
        count += 1
        #normalizador += 1
        lista.append([data_freq,normalizador,freq])

    else:
        print("Parou")
        break
    
normalizador += count

for i in lista:
    i[1]=normalizador
    normalizador -=1
    
print('//////////////     TOTAL RECEBIDOS:  ', count, '        ////////////////////')
print(lista)
    

