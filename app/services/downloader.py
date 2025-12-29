import yt_dlp
from pathlib import Path
from .converter import convert_to_mp3

def download_media(url: str, artist: str, channel_id: str | None = None):
    base = Path("downloads") / artist
    base.mkdir(parents=True, exist_ok=True)

    def filter_channel(info):
        if channel_id and info.get("channel_id") != channel_id:
            return "Ignorado: canal não oficial"
        return None

    ydl_opts = {
        "outtmpl": str(base / "%(title)s.%(ext)s"),
        "format": "bestaudio/best",
        "ignoreerrors": True,
        "match_filter": filter_channel,
        "noplaylist": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in base.iterdir():
        if file.suffix in [".webm", ".m4a", ".m4p"]:
            convert_to_mp3(file)
