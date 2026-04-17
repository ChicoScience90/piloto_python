from moviepy import VideoFileClip


def extrair_audio(caminho_video, caminho_audio):
    video = VideoFileClip(r"C:\Users\lukas\Downloads\Video by arquivo_cosmico.mp4")

    video.audio.write_audiofile(r"C:\Users\lukas\Downloads\Video by arquivo_cosmico.mp3")

    video.close()


extrair_audio("seu_video.mp4", "resultado_audio.mp3")
