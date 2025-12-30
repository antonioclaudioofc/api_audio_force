import yt_dlp
from pathlib import Path


class YoutubeDownloader:

    MAX_ITEMS = 10

    def download(self, url: str, output_dir: Path):
        ydl_opts = {
            "outtmpl": str(output_dir / "%(playlist_index)s - %(title)s.%(ext)s"),
            "format": "bestaudio/best",
            "playlist_items": f"1-{self.MAX_ITEMS}",
            "noplaylist": False,
            "quiet": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
