import uuid
from pathlib import Path
from services.zip_service import ZipService
from services.download.downloader import YoutubeDownloader
from services.download.converter import AudioConverter


class DownloadService:

    def __init__(self):
        self.downloader = YoutubeDownloader()
        self.converter = AudioConverter()
        self.zipper = ZipService()

    def download_and_zip(self, url: str) -> Path:
        temp_dir = Path("/tmp") / f"download_{uuid.uuid4().hex}"
        temp_dir.mkdir(parents=True)

        self.downloader.download(url, temp_dir)
        self.converter.to_mp3(temp_dir)

        zip_path = self.zipper.create_zip(temp_dir)

        return zip_path
