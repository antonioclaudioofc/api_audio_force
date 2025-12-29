import uuid
from core.store import TASKS
from .downloader import download_media

def process_download(task_id: str, data: dict):
    try:
        TASKS[task_id]["status"] = "PROCESSING"

        download_media(
            url=data["url"],
            artist=data["artist"],
            channel_id=data.get("official_channel_id")
        )

        TASKS[task_id]["status"] = "DONE"
    except Exception as e:
        TASKS[task_id]["status"] = "ERROR"
        TASKS[task_id]["error"] = str(e)

def create_task():
    task_id = uuid.uuid4().hex[:10]
    TASKS[task_id] = {"status": "QUEUED"}
    return task_id
