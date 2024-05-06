from models.Reader import Reader
from models.Downloader import Downloader
from models.Converter import Converter
import timeit
from datetime import datetime
import threading

startTime = timeit.default_timer()

reader = Reader()
converter = Converter()
channels = reader.readJson()

register = 'RegistroMultithreading.txt'
currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

with open(register, 'a') as registerFile:
	registerFile.write(f"\nMultithreading - Fecha y hora de la ejecución: {currentDateTime}\n\n")

threads = []
maxThreads = 4
semaphore = threading.Semaphore(maxThreads)

def work(channel, root, title, register):
	with semaphore:
		downloader = Downloader(channel, title, register)
		converter.convert(downloader.downloadVideo(root))

for urls in channels:
	for url in channels[urls]:
		thread = threading.Thread(target=work, args=(urls, url[0], url[1], register))
		threads.append(thread)
		thread.start()

for thread in threads:
	thread.join()

elapsedTime = timeit.default_timer() - startTime
elapsedMinutes = int(elapsedTime // 60)
elapsedSeconds = int(elapsedTime % 60)
print("\n\n\nLa ejecución ha terminado.")
print(f"Tiempo de ejecución: {elapsedMinutes} minutos y {elapsedSeconds} segundos")