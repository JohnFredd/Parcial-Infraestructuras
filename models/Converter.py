import ffmpeg
import os

class Converter:
	def convert(self, root):
		output = os.path.splitext(root)[0] + '.mp3'

		try:
			stream = ffmpeg.input(root)
			stream = ffmpeg.output(stream, output)
			ffmpeg.run(stream)
			os.remove(root)
		except Exception as e:
			print(f"Error al convertir el video: {root}", e)
			return
