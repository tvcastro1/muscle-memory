import requests


def main():
    r = requests.get("http://economia.awesomeapi.com.br/all/USD-BRL")
    if r.status_code == 200:
        valor_dolar = r.json()['USD']['low']
        return f'O valor do dólar hoje é R$ {valor_dolar}'
    else:
        return f'Ocorreu um erro ao acessar a API {r.status_code}'


if __name__ == '__main__':
    print(main())
