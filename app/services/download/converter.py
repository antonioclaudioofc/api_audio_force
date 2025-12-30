import subprocess
from pathlib import Path


class AudioConverter:

    def to_mp3(self, directory: Path):
        for file in directory.iterdir():
            if file.suffix in [".webm", ".m4a", ".m4p"]:
                output = file.with_suffix(".mp3")

                subprocess.run(
                    ["ffmpeg", "-y", "-i",
                        str(file), "-vn", "-ab", "192k", str(output)],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )

                file.unlink(missing_ok=True)
