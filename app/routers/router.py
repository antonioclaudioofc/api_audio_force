from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from domain.download.schemas import DownloadPayload
from services.download.download_service import DownloadService
from pathlib import Path
import shutil

router = APIRouter(
    prefix="/music",
    tags=["Download"]
)

service = DownloadService()


@router.post("/download")
def download_zip(payload: DownloadPayload):
    zip_path: Path = service.download_and_zip(payload.url)

    def file_stream():
        try:
            with open(zip_path, "rb") as f:
                while chunk := f.read(1024 * 1024):
                    yield chunk
        finally:
            shutil.rmtree(zip_path.parent, ignore_errors=True)

    return StreamingResponse(
        file_stream(),
        media_type="application/zip",
        headers={
            "Content-Disposition": "attachment; filename=music.zip"
        }
    )
