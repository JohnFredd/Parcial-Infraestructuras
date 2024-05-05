import yt_dlp
import os

class Downloader:
    def __init__(self, channel):
        self.downloader = yt_dlp.YoutubeDL({'outtmpl': os.path.join("/videos/", channel, '%(title)s.%(ext)s')})

    def downloadVideo(self, video_url):
        try:
            self.downloader.extract_info(video_url)
            self.downloader.download([video_url])
            print("Descarga completada con éxito.")
        except Exception as e:
            print(f"Ocurrió un error durante la descarga: {str(e)}")
