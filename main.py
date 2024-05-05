from models.Reader import Reader
from models.Downloader import Downloader

downloader = Downloader()
video_url = "https://www.youtube.com/watch?v=u66g74GJ5Zc&t=1s"
downloader.downloadVideo(video_url)
