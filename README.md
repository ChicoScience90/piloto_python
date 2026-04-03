***

# Piloto Python — Coleção de Scripts Utilitários

Repositório de estudos e ferramentas úteis escritas em Python. Cada script resolve um problema do dia a dia de forma simples e direta.

---

## Scripts disponíveis

| Script | Descrição |
|---|---|
| `analisando_senhas.py` | Analisa uma senha caractere por caractere |
| `gerador_de_senhas_random.py` | Gera senhas aleatórias e seguras |
| `extracao.py` | Extrai áudio de arquivos de vídeo |
| `videos_extracao.py` | Faz download de vídeos do YouTube |
| `translate.py` | Traduz textos entre idiomas via terminal |

---

## Analisador de Senhas (`analisando_senhas.py`)

Pede para o usuário digitar uma senha e classifica cada caractere em:

- **Letras** — caracteres alfabéticos (a-z, A-Z)
- **Números** — dígitos numéricos (0-9)
- **Símbolos** — símbolos permitidos (`@`, `#`, `*`)
- **Inválido** — qualquer outro caractere

```bash
python analisando_senhas.py
```

---

## Gerador de Senhas Seguras (`gerador_de_senhas_random.py`)

Gera uma senha aleatória utilizando a biblioteca `secrets` (recomendada para criptografia).

- **Tamanho padrão:** 12 caracteres (configurável pelo parâmetro `largura`)
- **Composição:** letras maiúsculas e minúsculas, números e os símbolos `@#*`

```bash
python gerador_de_senhas_random.py
```

---

## Extrator de Áudio (`extracao.py`)

Extrai a faixa de áudio de um arquivo de vídeo local e salva como `.mp3`, utilizando a biblioteca `moviepy`.

```bash
python extracao.py
```

> **Nota:** edite os caminhos do vídeo de origem e do áudio de destino diretamente no script antes de executar.

---

## Download de Vídeos do YouTube (`videos_extracao.py`)

Faz o download de vídeos do YouTube na melhor qualidade disponível, utilizando a biblioteca `yt-dlp`.

```bash
python videos_extracao.py
```

> **Nota:** edite a variável `link_do_video` no script com a URL desejada antes de executar.

---

## Tradutor de Textos (`translate.py`)

Traduz textos do **Português** para o **Espanhol** diretamente pelo terminal, utilizando a biblioteca `deep-translator` com o Google Tradutor.

```bash
python translate.py "Texto que eu quero traduzir"
```

Os idiomas de origem e destino podem ser alterados editando as variáveis `IDIOMA_ORIGEM` e `IDIOMA_DESTINO` no início do script.

---

## Tecnologias e Dependências

| Dependência | Uso | Instalação |
|---|---|---|
| **Python 3** | Linguagem base | [python.org](https://www.python.org/) |
| `secrets` / `string` | Geração de senhas seguras | *(nativa do Python)* |
| `moviepy` | Extração de áudio de vídeos | `pip install moviepy` |
| `yt-dlp` | Download de vídeos do YouTube | `pip install yt-dlp` |
| `deep-translator` | Tradução de textos | `pip install deep-translator` |

---

## Como usar

### Pré-requisitos
- Python 3.x instalado na máquina

### Instalando as dependências externas

```bash
pip install moviepy yt-dlp deep-translator
```

### Executando qualquer script

```bash
python nome_do_script.py
```

***