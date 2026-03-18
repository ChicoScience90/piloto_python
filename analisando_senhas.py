import string

def analisando_senhas():
    senha_digi = str(input('Digite sua senha: '))
    simbolos_permitidos = '@#*'

    print('\nResultados da Análise')
    for car in senha_digi:
        if car.isalpha():
            tipo = 'letras'
        elif car.isdigit():
            tipo = 'Números'
        elif car in simbolos_permitidos:
            tipo  = "Símbolos"
        else:
            tipo = 'Inválido'

        print(f'O caractere {car} é: {tipo}')

analisando_senhas()