from models.Reader import Reader
from models.Downloader import Downloader

reader = Reader()
channels = reader.readJson()

for urls in channels:
	downloader = Downloader(urls)
	for url in channels[urls]:
		downloader.downloadVideo(url)
