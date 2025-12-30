from pydantic import BaseModel


class DownloadPayload(BaseModel):
    url: str
