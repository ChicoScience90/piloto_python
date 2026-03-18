import secrets
import string

def criar_senha_nova(largura=12):
    caracteres = string.ascii_letters + string.digits
    meus_simbolos = '@#*'
    senha = ''.join(secrets.choice(caracteres + meus_simbolos) for i in range(largura))
    return senha
print(criar_senha_nova())