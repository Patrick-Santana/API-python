#  Python script.

import requests
def main():

    print('Consulte o Seu Cep')
    print('******************')

    cep_input = input('Digite o Seu Cep para consulta: ')

    if len(cep_input) != 8:
     print('Quantidade de Dígitos inválida!!')
     exit()

    request = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep_input))

    address_data = request.json()

    if 'erro' not in address_data:
        print('==>CEP ENCONTRADO<==')

        print('CEP:{}'.format(address_data['cep']))
        print('Logradouro:{}'.format(address_data['logradouro']))
        print('Complemento:{}'.format(address_data['complemento']))
        print('Bairro:{}'.format(address_data['bairro']))
        print('Localidade:{}'.format(address_data['localidade']))
        print('UF: {}'.format(address_data['uf']))
    else:
         print('{} CEP Inválido'.format(cep_input))

    print('--------------------------------')
    option = int(input('Deseja realizar uma nova consulta? ?\n1. Sim\n2. Sair\n '))

    if option == 1:
        main()
    else:
        print('Operação Finalizada Com Sucesso!')


if __name__ == '__main__':
    main()

