import yt_dlp
import os

class Downloader:
	def __init__(self, channel):
		self.root = os.path.join("audios", channel)
		self.downloader = yt_dlp.YoutubeDL({'outtmpl': os.path.join(self.root, '%(title)s.%(ext)s')})

	def downloadVideo(self, videoUrl):
		try:
			info = self.downloader.extract_info(videoUrl)
			self.downloader.download([videoUrl])
			videoTitle = info['title']
			videoExtension = info['ext']
			downloadedFile = os.path.join(self.root, f"{videoTitle}.{videoExtension}")
			print("Descarga completada con éxito.")
			return downloadedFile
		except Exception as e:
			print(f"Ocurrió un error durante la descarga: {str(e)}")
