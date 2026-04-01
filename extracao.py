from moviepy import VideoFileClip


def extrair_audio(caminho_video, caminho_audio):
    video = VideoFileClip(r"arquivo.mp4 que voce vai selecionar")

    video.audio.write_audiofile(r"destino do arquivo.mp3")

    video.close()


extrair_audio("seu_video.mp4", "resultado_audio.mp3")