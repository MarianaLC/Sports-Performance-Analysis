
from Adafruit_IO import Client, Feed
from datetime import date
import getfit
import time

ADAFRUIT_IO_KEY = 'aio_GEWr22EO5KFqQFFUFqQecBH13wTH'
ADAFRUIT_IO_USERNAME = 'laravaz'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

def transfer():
    count = 0

    print('///////////////   A ENVIAR PARA ADAFRUIT...  ///////////////')
    for i,j in getfit.lista.items():
        count+=1
        ponto=str(str(i)+';'+ str(j))
        print(ponto)
        time.sleep(2)
        aio.send('lara-treinos', ponto)
        time.sleep(10)
    print('///////////////   FORAM RECEBIDOS ',count,' VALORES  ///////////////')
    return count

if __name__ == '__main__':
    transfer()