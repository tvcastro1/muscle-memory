import requests
import json
token = 'APP_USR-39567916004755-030723-e85b528babb1ea693b2ebc1e16ad61c7-448944834'


def consulta_config():
    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    r = requests.get('https://api.mercadopago.com/v1/account/settlement_report/config', headers=headers)
    return r.json()


def gera_relatorio():

    headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    data = '{ "begin_date": "2022-02-01T00:00:00Z", "end_date": "2022-02-28T00:00:00Z" }'

    r = requests.post('https://api.mercadopago.com/v1/account/settlement_report', headers=headers, data=data)
    return r





headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {token} '
}

response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/list', headers=headers)
response_json = response.json()
dict_response = {(key, value) for x in response_json for key ,value in x.items()}
print(response_json)
print(dict_response)
# for x in response_json:
#     for key, value in x.items():
#         print(key)
#         print(value)







def download_relatorio():

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/settlement-report-448944834-2022-03-13-151126.csv', headers=headers)

    return response.text
