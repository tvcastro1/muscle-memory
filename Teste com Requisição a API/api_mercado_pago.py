import requests
import pandas as pd
import io
import json
token = 'APP_USR-39567916004755-030723-e85b528babb1ea693b2ebc1e16ad61c7-448944834'

headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
    'Authorization': f'Bearer {token}'
}

data = {
            "file_name_prefix": "settlement-report-USER_ID",
            "show_fee_prevision": False,
            "show_chargeback_cancel": True,
            "coupon_detailed": True,
            "include_withdraw": True,
            "shipping_detail": True,
            "refund_detailed": True,
            "display_timezone": "GMT-03",
            "report_translation": True,
            "columns": [
                {
                    "key": "TRANSACTION_DATE"
                },
                {
                    "key": "SOURCE_ID"
                },
                {
                    "key": "EXTERNAL_REFERENCE"
                }
            ]
        }

response = requests.put('https://api.mercadopago.com/v1/account/settlement_report/config', headers=headers, data=data)
print(response)

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





# headers = {
#     'accept': 'application/json',
#     'Authorization': f'Bearer {token} '
# }
#
# response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/list', headers=headers)
# response_json = response.json()
# json_data = json.loads(response.text)
# for i in range(len(json_data)):
#     print(json_data[i])
# dict_response = {(key, value) for x in response_json for key ,value in x.items()}
# print(response_json)
# print(dict_response)
# for x in response_json:
#     for key, value in x.items():
#         print(key)
#         print(value)



def download_relatorio():

    headers = {
        'Authorization': f'Bearer {token}'
    }

    response = requests.get('https://api.mercadopago.com/v1/account/settlement_report/settlement-report-448944834-2022-03-13-151126.csv', headers=headers)
    url_content = response.content
    df = pd.read_csv(io.StringIO(url_content.decode('utf-8')), header=None, sep='\n')
    df = df[0].str.split('\s\|\s', expand=True)
    # csv_file = open('downloaded1.csv', 'wb')
    # csv_file.write(url_content)
    # csv_file.close()
    # df = pd.read_csv('downloaded1.csv',delimiter=',', engine='python', quoting=3, header=None)
    # return df.to_string()

    # csv_file = open('downloaded.csv', 'wb')
    # csv_file.write(url_content)
    # csv_file.close()
    return df.to_string()

# print(download_relatorio())

print(consulta_config())