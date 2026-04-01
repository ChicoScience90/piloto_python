from moviepy import VideoFileClip


def extrair_audio(caminho_video, caminho_audio):
    # Carrega o arquivo de vídeo
    video = VideoFileClip(r"C:\Users\lukas\OneDrive\Área de Trabalho\ssstwitter.com_1774873552091.mp4")

    # Extrai o áudio e salva no formato desejado (mp3, wav, etc.)
    video.audio.write_audiofile(r"C:\Users\lukas\Downloads\hanzo.mp3")

    # Fecha o arquivo para liberar memória
    video.close()


# Exemplo de uso
extrair_audio("seu_video.mp4", "resultado_audio.mp3")