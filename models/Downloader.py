import yt_dlp
import os
from datetime import datetime

class Downloader:
	def __init__(self, channel, title, register):
		self.register = register
		self.title = title
		self.root = os.path.join("audios", channel, title)
		self.downloader = yt_dlp.YoutubeDL({'outtmpl': self.root + '.%(ext)s'})

	def downloadVideo(self, videoUrl):
		try:
			info = self.downloader.extract_info(videoUrl)
			self.downloader.download([videoUrl])
			videoExtension = info['ext']
			downloadedFile = self.root + f".{videoExtension}"

			uploadDate = info.get('upload_date', 'Unknown')
			try:
				uploadDateStr = datetime.strptime(uploadDate, '%Y%m%d').strftime('%Y-%m-%d')
			except:
				uploadDateStr = "Unknown"
			currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			with open(self.register, 'a') as registerFile:
				registerFile.write(f"Video: {self.title} - Fecha de publicación: {uploadDateStr} - Fecha y hora de descarga: {currentDateTime}\n")

			print("Descarga completada con éxito.")
			
			return downloadedFile
		except Exception as e:
			print(f"Ocurrió un error durante la descarga: {str(e)}")
