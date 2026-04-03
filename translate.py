import sys
from deep_translator import GoogleTranslator

IDIOMA_ORIGEM = 'pt'
IDIOMA_DESTINO = 'es'

def traduzir_texto(texto):
    try:
        tradutor = GoogleTranslator(source= IDIOMA_ORIGEM, target= IDIOMA_DESTINO)
        resultado = tradutor.translate(texto)
        return resultado
    except Exception as e:
        return f"Ocorreu um erro durante a tradução: {e}"
if __name__ == "__main__":
    if len(sys.argv) > 1:
        texto_para_traduzir = " ". join(sys.argv[1:])
        texto_traduzido = traduzir_texto(texto_para_traduzir)

        print("-" * 50)
        print(f"Idioma Original ({IDIOMA_ORIGEM}): {texto_para_traduzir}")
        print(f"Tradução ({IDIOMA_DESTINO}): {texto_traduzido}")
        print("_" * 50)
    else:
        print("Uso incorreto. Por favor, passe o texto junto com o comando.")
        #Como usar
        print('Exemplo: python translate.py "Texto que eu quero traduzir"')
