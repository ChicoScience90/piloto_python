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

        print("\n✅ Download concluído com sucesso!")

    except Exception as e:
        print(f"\n❌ Ocorreu um erro ao tentar baixar o vídeo: {e}")


link_do_video = "https://x.com/RaphaelMemes/status/2039380770905575629"

extrair_video(link_do_video)