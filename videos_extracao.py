import yt_dlp


def extrair_video(url):
    opcoes = {
        'paths': {'home': r'C:\Users\lukas\Downloads'},

        'outtmpl': '%(title)s.%(ext)s',

        # Baixa a melhor qualidade de vídeo e áudio separadamente e junta (se tiver ffmpeg)
        # Tenta forçar mp4/m4a para melhor compatibilidade. Fallback para 'best' (720p).
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        'merge_output_format': 'mp4',
        
        # Aponta pro ffmpeg que instalamos agora, pois o terminal não atualizou as variáveis
        'ffmpeg_location': r'C:\Users\lukas\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin',

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


link_do_video = "https://www.youtube.com/watch?v=eAiVwsXgPDM"

extrair_video(link_do_video)