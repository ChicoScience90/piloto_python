import yt_dlp


def extrair_video(url):
    opcoes = {
        'paths': {'home': r'C:\Users\lukas\Downloads'},

        'outtmpl': '%(title)s.%(ext)s',

        'format': 'best',

        'quiet': False,
        'no_warnings': True
    }

    try:
        print(f"Tentando extrair o vídeo de: {url}")

        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url])

        print("\nDownload concluído com sucesso!")

    except Exception as e:
        print(f"\nOcorreu um erro ao tentar baixar o vídeo: {e}")


link_do_video = "https://www.youtube.com/watch?v=1ZGsugwZC2U"

extrair_video(link_do_video)