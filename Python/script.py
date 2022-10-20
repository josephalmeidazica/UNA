import requests
url = 'https://api.hgbrasil.com/finance?'
key = 'key=95c18823'
format_json = 'format=json-cors&'


r = requests.get(url + key + format_json)
if (r.status_code == 200):
    data = r.json()
    for item in data['results']['currencies']:
        print()
        print(data['results']['currencies'][item])
        print()
else:
    print('Nao houve sucesso na requisicao.')