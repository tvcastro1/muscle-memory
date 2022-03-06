import requests

r = requests.get("http://economia.awesomeapi.com.br/all/USD-BRL")
cotacao = r.json()

print(cotacao)

print('#### Cotação do Dolar ####')
print(cotacao['USD']['low'])

# def main():
#     r = requests.get("http://economia.awesomeapi.com.br/all/USD-BRL")
#     if r.status_code == 200:
#         valor_dolar = r.json()['USD']['low']
#         print(f'O valor do dólar hoje é R$ {valor_dolar}')
#     else:
#         print(f'Ocorreu um erro ao acessar a API {r.status_code}')
#
#     if __name__ == '__main__':
#         main()


