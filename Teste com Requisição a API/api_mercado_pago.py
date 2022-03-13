import requests

token = 'APP_USR-39567916004755-030723-e85b528babb1ea693b2ebc1e16ad61c7-448944834'


def consulta_config():
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.get('https://api.mercadopago.com/v1/account/settlement_report/config', headers=headers)
    return r.json()

print(consulta_config())
def gera_relatorio():

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    data = '{ "begin_date": "2022-02-01T00:00:00Z", "end_date": "2022-02-28T00:00:00Z" }'

    r = requests.post('https://api.mercadopago.com/v1/account/settlement_report', headers=headers, data=data)
    return r


print(gera_relatorio())


headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {token} '
}

response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/list', headers=headers)
response_json = response.json()

print(response_json)


headers = {
    'Authorization': f'Bearer {token}'
}

response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/:file_name', headers=headers)

print(response)
