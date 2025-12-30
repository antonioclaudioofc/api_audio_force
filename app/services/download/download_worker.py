from app.repository.task_repository import TaskRepository
from app.domain.download.enums import TaskStatus
from app.services.download.downloader import YoutubeDownloader
from app.services.download.converter import AudioConverter


class DownloadWorker:

    def __init__(self):
        self.repo = TaskRepository()
        self.downloader = YoutubeDownloader()
        self.converter = AudioConverter()

    def execute(self, task_id: str, payload):
        try:
            self.repo.update_status(task_id, TaskStatus.PROCESSING)

            directory = self.downloader.download(payload.url)
            self.converter.to_mp3(directory)

            self.repo.update_status(task_id, TaskStatus.DONE)

        except Exception as e:
            self.repo.set_error(task_id, str(e))
