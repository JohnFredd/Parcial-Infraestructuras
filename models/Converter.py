import ffmpeg
import os

class Converter:
	def convert(self, root):
		print()
		print(root)
		output = os.path.splitext(root)[0] + '.mp3'

		print(output)
		print()

		try:
			stream = ffmpeg.input(root)
			print(stream)
			print()
			stream = ffmpeg.output(stream, output)
			ffmpeg.run(stream)
			os.remove(root)
		except FileNotFoundError:
			print(f"Error al convertir el video: {root}, no se encuentra el archivo, posiblemente contiene caracteres ilegibles en la ruta.")
			return
		except Exception as e:
			print(f"Error al convertir el video: {root}", e)
			return
