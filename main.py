from models.Reader import Reader
from models.Downloader import Downloader
from models.Converter import Converter
import timeit
from datetime import datetime

startTime = timeit.default_timer()

reader = Reader()
converter = Converter()
channels = reader.readJson()

register = 'RegistroSecuencial.txt'
currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open(register, 'a') as registerFile:
	registerFile.write(f"\nSecuencial - Fecha y hora de la ejecución: {currentDateTime}\n\n")

for urls in channels:
	for url in channels[urls]:
		downloader = Downloader(urls, url[1], register)
		converter.convert(downloader.downloadVideo(url[0]))

elapsedTime = timeit.default_timer() - startTime
elapsedMinutes = int(elapsedTime // 60)
elapsedSeconds = int(elapsedTime % 60)
print("\n\n\nLa ejecución ha terminado.")
print(f"Tiempo de ejecución: {elapsedMinutes} minutos y {elapsedSeconds} segundos")