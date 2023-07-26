import requests

informacoesEndereco = {}
caractereCep = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.', '-']

print("Informe seu cep em um dos seguintes formatos: '00000-000', '00000.000', '00.000-000'")
cep = input()

for caractere in cep:
    if caractere not in caractereCep:
        print('cep informado no formato invalido, Tente novamente.')
        break

cepSemSeparadores = cep.replace('-', '')
cepSemSeparadores = cepSemSeparadores.replace('.', '')

url = f'https://viacep.com.br/ws/{cepSemSeparadores}/json/'
requisicao = requests.get(url)

informacoesEndereco = requisicao.json()

for informacao in informacoesEndereco:
    print(f'{informacao} : {informacoesEndereco.get(informacao)}')
