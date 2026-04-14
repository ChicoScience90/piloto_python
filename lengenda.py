"""
Script para legendar filmes/vídeos automaticamente com tradução.
Usa o modelo Whisper (OpenAI) localmente para transcrever o áudio
(em inglês ou outro idioma) e o deep-translator para converter a 
legenda para o português antes de gerar o arquivo .srt.

Dependências:
    pip install openai-whisper moviepy deep-translator

O Whisper também precisa do ffmpeg instalado no sistema.
"""

import os
import whisper
from moviepy import VideoFileClip
from deep_translator import GoogleTranslator


def extrair_audio(caminho_video):
    """Extrai o áudio do vídeo e salva como .wav temporário."""
    caminho_audio = caminho_video.rsplit(".", 1)[0] + "_temp_audio.wav"
    print(f"[1/3] Extraindo áudio de: {caminho_video}")

    video = VideoFileClip(caminho_video)
    video.audio.write_audiofile(caminho_audio, logger=None)
    video.close()

    print(f"      Áudio extraído: {caminho_audio}")
    return caminho_audio


def transcrever_audio(caminho_audio, modelo="base", idioma=None):
    """
    Transcreve o áudio usando o Whisper.
    """
    print(f"[2/3] Carregando modelo Whisper '{modelo}'...")
    model = whisper.load_model(modelo)

    print(f"      Transcrevendo áudio (isso pode levar alguns minutos)...")
    opcoes = {}
    if idioma:
        opcoes["language"] = idioma

    resultado = model.transcribe(caminho_audio, **opcoes)

    idioma_detectado = resultado.get("language", "desconhecido")
    print(f"      Idioma detectado pelo Whisper: {idioma_detectado}")
    print(f"      Total de segmentos: {len(resultado['segments'])}")

    return resultado


def formatar_tempo_srt(segundos):
    """Converte segundos (float) para o formato SRT: HH:MM:SS,mmm"""
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segs = int(segundos % 60)
    milissegundos = int((segundos % 1) * 1000)
    return f"{horas:02d}:{minutos:02d}:{segs:02d},{milissegundos:03d}"


def gerar_srt(resultado, caminho_srt, traduzir_para=None):
    """Gera o arquivo .srt e traduz o texto se solicitado."""
    print(f"[3/3] Gerando arquivo de legendas: {caminho_srt}")

    tradutor = None
    if traduzir_para:
        print(f"      Traduzindo as legendas para: '{traduzir_para}'...")
        tradutor = GoogleTranslator(source='auto', target=traduzir_para)

    with open(caminho_srt, "w", encoding="utf-8") as f:
        for i, segmento in enumerate(resultado["segments"], start=1):
            inicio = formatar_tempo_srt(segmento["start"])
            fim = formatar_tempo_srt(segmento["end"])
            texto = segmento["text"].strip()

            # Traduz a linha se necessário
            if tradutor:
                try:
                    texto = tradutor.translate(texto)
                except Exception as e:
                    print(f"      Erro ao traduzir o trecho {i}: {e}")

            f.write(f"{i}\n")
            f.write(f"{inicio} --> {fim}\n")
            f.write(f"{texto}\n\n")

    print(f"      Legendas salvas com sucesso!")


def legendar_video(caminho_video, modelo="base", idioma_do_audio=None, traduzir_para=None):
    """
    Função principal: recebe o caminho de um vídeo e gera o .srt correspondente.
    """
    if not os.path.exists(caminho_video):
        print(f"Erro: Arquivo '{caminho_video}' não encontrado!")
        return

    caminho_srt = caminho_video.rsplit(".", 1)[0] + ".srt"

    # 1. Extrair áudio
    caminho_audio = extrair_audio(caminho_video)

    try:
        # 2. Transcrever
        resultado = transcrever_audio(caminho_audio, modelo=modelo, idioma=idioma_do_audio)

        # 3. Gerar .srt (com tradução)
        gerar_srt(resultado, caminho_srt, traduzir_para=traduzir_para)

    finally:
        # Limpar arquivo de áudio temporário
        if os.path.exists(caminho_audio):
            os.remove(caminho_audio)
            print(f"\n      Arquivo temporário de áudio removido.")

    print(f"\nConcluído! Legenda gerada em: {caminho_srt}")


# =====================================================================
# CONFIGURAÇÃO - Altere aqui conforme sua necessidade
# =====================================================================

# Caminho do vídeo
VIDEO = r"C:\Users\lukas\Downloads\Video by taldediguinho.mp4"

# Idioma original do AUDIO (ex: 'en' para Inglês). Isso ajuda o Whisper a não se perder nas palavras em inglês.
IDIOMA_DO_AUDIO = "en"

# Para qual idioma você quer TRANSLATED a legenda pronta? (ex: 'pt' para Português, ou deixe None se não quiser traduzir)
TRADUZIR_PARA = "pt"

MODELO = "base"

if __name__ == "__main__":
    legendar_video(VIDEO, modelo=MODELO, idioma_do_audio=IDIOMA_DO_AUDIO, traduzir_para=TRADUZIR_PARA)
