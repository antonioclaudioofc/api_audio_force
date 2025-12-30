# 🎵 Audio Forge API

Audio Forge é uma API desenvolvida com FastAPI que permite baixar o áudio de vídeos ou playlists do YouTube, limitando o download a no máximo 10 itens. Os arquivos são compactados em um ZIP, enviados diretamente ao cliente via streaming e removidos automaticamente após o download.

O projeto foi pensado para ser simples, sem estado e pronto para uso em produção.

---

## 🚀 Funcionalidades

- Download de áudio a partir de um vídeo ou playlist do YouTube
- Limite máximo de **10 vídeos por requisição**
- Não é necessário informar artista ou metadados
- Geração automática de arquivo ZIP
- Envio do ZIP via streaming
- Nenhum arquivo é armazenado permanentemente
- Limpeza automática dos arquivos temporários
- Desenvolvido com **FastAPI** e **yt-dlp**

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- yt-dlp
- FFmpeg (obrigatório)
- StreamingResponse (Starlette)