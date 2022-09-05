import json
import requests
from datetime import datetime

api_url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"

access_token = "ya29.A0ARrdaM91BZXYN-_ctl5qnI4ELlOpqafpbhiDjAS5i20P4BUqszeqR9L_BAaqExQWBQwpUQ6VU19CEUVKrjeha-W9dj0nvYWVPERvFqhd6fu3vC5dSE-AXeBQo3iOIWeaTZ3pynSCO3H4ADXFPr7kJSeu33kN"
# Ver no google developers OAuth 2.0 Playground

headers = {
  "Authorization": "Bearer {}".format(access_token),
  "Content-Type": "application/json;encoding=utf-8"
  }

body = {
  "aggregateBy": [{
    "dataSourceId":
      "derived:com.google.heart_rate.bpm:com.google.android.gms:merge_heart_rate_bpm"
  }],
  "startTimeMillis": 1648378800000, # Mudar de Data/Hota para Milissegundos https://codechi.com/dev-tools/date-to-millisecond-calculators/
  "endTimeMillis": 1648386000000
}

response = requests.post(api_url, data=json.dumps(body), headers=headers)

print(response.text) #Para ver o conteudo do pedido

lista={}
resposta=response.json()

for i in resposta['bucket']:
  for x in i['dataset']:
    for dados in x['point']:
      start = dados['startTimeNanos']
      secs = int(start) / 1000000000
      dt = datetime.fromtimestamp(secs)
      print(dt.strftime('%Y-%m-%dT%H:%M:%S.%f'))
      value = dados['value']
      for o in dados['value']:
        fpVal=o['fpVal']
        lista.update({str(dt):fpVal})
print(lista)
print(len(lista.keys()))


