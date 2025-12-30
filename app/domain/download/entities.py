from dataclasses import dataclass
from domain.download.enums import TaskStatus


@dataclass
class DownloadTask:
    id: str
    status: TaskStatus
    error: str | None = None
