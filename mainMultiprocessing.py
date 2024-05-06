from models.Reader import Reader
from models.Downloader import Downloader
from models.Converter import Converter
import timeit
from datetime import datetime
import multiprocessing

startTime = timeit.default_timer()

reader = Reader()
converter = Converter()
channels = reader.readJson()

register = 'RegistroMultiprocessing.txt'
currentDateTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def work(channel, root, title, register, semaphore):
	with semaphore:
		downloader = Downloader(channel, title, register)
		converter.convert(downloader.downloadVideo(root))

if __name__ == "__main__":
	with open(register, 'a') as registerFile:
		registerFile.write(f"\nMultiprocessing - Fecha y hora de la ejecución: {currentDateTime}\n\n")
		
	processes = []
	maxProcesses = 8
	semaphore = multiprocessing.Semaphore(maxProcesses)

	for urls in channels:
		for url in channels[urls]:
			process = multiprocessing.Process(target=work, args=(urls, url[0], url[1], register, semaphore))
			processes.append(process)
			process.start()

	for process in processes:
		process.join()

	elapsedTime = timeit.default_timer() - startTime
	elapsedMinutes = int(elapsedTime // 60)
	elapsedSeconds = int(elapsedTime % 60)
	print("\n\n\nLa ejecución ha terminado.")
	print(f"Tiempo de ejecución: {elapsedMinutes} minutos y {elapsedSeconds} segundos")