from fastapi import APIRouter, BackgroundTasks, HTTPException
from pathlib import Path
from core.store import TASKS
from schemas.download import DownloadRequest
from services.tasks import process_download, create_task

router = APIRouter(
    prefix="music",
)


@router.post("/downloads")
def create_download(data: DownloadRequest, bg: BackgroundTasks):
    task_id = create_task()
    bg.add_task(process_download, task_id, data.model_dump())
    return {"task_id": task_id, "status": "processing"}

@router.get("/downloads/{task_id}")
def get_status(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(404)
    return TASKS[task_id]

@router.get("/downloads/{task_id}/files")
def list_files(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(404)

    files = []
    base = Path("downloads")

    for artist in base.iterdir():
        if artist.is_dir():
            files.extend([f.name for f in artist.glob("*.mp3")])

    return {"files": files}

@router.delete("/downloads/{task_id}")
def delete_task(task_id: str):
    if task_id not in TASKS:
        raise HTTPException(404)

    del TASKS[task_id]
    return {"message": "Tarefa removida"}
