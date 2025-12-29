import subprocess
from pathlib import Path

def convert_to_mp3(file: Path):
    output = file.with_suffix(".mp3")

    subprocess.run(
        ["ffmpeg", "-y", "-i", str(file), "-vn", "-ab", "192k", str(output)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    file.unlink(missing_ok=True)
