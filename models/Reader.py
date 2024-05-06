import json
import yt_dlp
import re

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
			'quiet': True,
			'extract_flat': True,
			'force_generic_extractor': True,
			'force_single_feed': True,
			'skip_download': True,
			'nocheckcertificate': True,
			'no_warnings': True,
			'ignoreerrors': True,
			'dump_single_json': True,
			'simulate': True,
			'youtube_include_dash_manifest': False,
			'youtube_include_hls_manifest': False,
			'extract_flat': True,
			'extractor_args': {'youtube': {'extract_flat': True}},
			'get_description': False,
			'get_thumbnail': False,
			'get_duration': False,
			'get_view_count': False,
			'get_like_count': False,
			'get_dislike_count': False,
			'get_average_rating': False,
			'get_categories': False,
			'get_tags': False,
			'playlist_items': '1-5'
		}
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			info = ydl.extract_info(channelUrl, download=False)
			channelName = info['uploader']
			recentVideos = []
			for entry in info['entries'][0]['entries']:
				recentVideos.append([entry['url'], self.cleanFilename(entry['title'])])
		return channelName, recentVideos
	
	def cleanFilename(self, filename):
		cleanedFilename = re.sub(r'[^\w\s-]', '', filename)

		return cleanedFilename