import zipfile
from pathlib import Path


class ZipService:

    def create_zip(self, directory: Path) -> Path:
        zip_path = directory / "result.zip"

        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            for file in directory.glob("*.mp3"):
                zipf.write(file, arcname=file.name)

        return zip_path
