***

# Ferramentas de Senha em Python

Este pequeno projeto em Python contém duas ferramentas úteis para a manipulação e verificação de senhas: um **Analisador de Senhas** e um **Gerador de Senhas Seguras**.

## Funcionalidades

O código é dividido em duas funções principais:

### 1. Analisador de Senhas (`analisando_senhas`)
Esta função pede para o usuário digitar uma senha e analisa caractere por caractere, classificando-os em quatro categorias:
* **Letras:** Caracteres alfabéticos (a-z, A-Z).
* **Números:** Dígitos numéricos (0-9).
* **Símbolos Permitidos:** Verifica se o caractere é um dos símbolos específicos aceitos (`@`, `#`, `*`).
* **Inválido:** Qualquer caractere que não se encaixe nas regras acima (ex: espaços, outros símbolos).

### 2. Gerador de Senhas Seguras (`criar_senha_nova`)
Esta função gera uma senha aleatória e segura utilizando a biblioteca `secrets` (recomendada para criptografia e segurança).
* **Tamanho padrão:** 12 caracteres (podendo ser customizado através do parâmetro `largura`).
* **Composição:** Utiliza uma mistura de letras (maiúsculas e minúsculas), números e os símbolos permitidos (`@#*`).

---

## Como usar

### Pré-requisitos
* Python 3.x instalado na sua máquina.

### Executando o código
Você pode colocar os dois trechos de código em um único arquivo chamado `senhas.py` e executá-lo no terminal:

```bash
python senhas.py
```

Ao rodar o script:
1. Ele primeiro pedirá que você digite uma senha para ser analisada e imprimirá o resultado na tela.
2. Em seguida, ele irá gerar e imprimir uma nova senha segura de 12 caracteres de forma automática.

---

## Tecnologias Utilizadas
* **Python 3**
* Biblioteca `secrets` (nativa do Python, usada para geração de números pseudoaleatórios criptograficamente fortes).
* Biblioteca `string` (nativa do Python, usada para puxar constantes de letras e números).

***