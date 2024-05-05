from models.Reader import Reader
from models.Downloader import Downloader
from models.Converter import Converter

reader = Reader()
converter = Converter()
channels = reader.readJson()

for urls in channels:
	downloader = Downloader(urls)
	for url in channels[urls]:
		converter.convert(downloader.downloadVideo(url))
