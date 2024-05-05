import json
import yt_dlp

class Reader():
	def readJson(self, fileName = "static/channels.json"):
		try:
			with open(fileName, 'r') as file:
				data = json.load(file)
				channels = data.get("channels", [])
		except FileNotFoundError:
			print("Archivo no encontrado, introduzca el nombre del archivo correctamente o defina un archivo en la ruta: /static/channels.json")
			return
		except Exception as e:
			print("Error al cargar el archivo:", e)
			return

		
		videos = {}
		for channelUrl in channels:
			channelName, channelVideos = self.extractChannelInformation(channelUrl)
			if channelVideos:
				videos[channelName] = channelVideos

		return videos


	def extractChannelInformation(self, channelUrl):
		ydl_opts = {
			'extract_flat': True,
			'quiet': True,
			'skip_info': True,
		}
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			info = ydl.extract_info(channelUrl, download=False)
			channelName = info.get('uploader', '')
			recentVideos = self.extractRecentVideos(channelUrl)
		return channelName, recentVideos
	
	def extractRecentVideos(self, channelUrl):
		ydl_opts = {
			'extract_flat': True,
			'quiet': True,
			'max_entries': 5,
		}
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			info = ydl.extract_info(channelUrl, download=False)
			print(info)
			if 'entries' in info:
				recentVideos = [entry['url'] for entry in info['entries']]
				return recentVideos
			else:
				return None