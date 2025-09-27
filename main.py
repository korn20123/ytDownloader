from yt_dlp import YoutubeDL
import argparse
import os
import sys
def get_app_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(__file__))
def download(url, output='%(title)s.%(ext)s'):
    ffmpeg_path = os.path.join(get_app_dir(), "ffmpeg.exe")
    opts = {
        'format': 'bestaudio/best',
        'outtmpl': output,
        'ffmpeg_location': ffmpeg_path,
        'ignoreerrors': True,
        'noprogress': True,
        'quit': True,
        'noplaylist': True,
        'prefer_ffmpeg': True,             # zwingt yt-dlp, ffmpeg zu nutzen
        'force_generic_extractor': True,   # oft notwendig, um ffprobe zu umgehen
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            },
        ],
    }
    with YoutubeDL(opts) as yt:
        yt.download([url])
def main():
    parser = argparse.ArgumentParser(description='program zum runterladen von youtube audio')
    parser.add_argument('url', help='die url zum runterladen')
    args = parser.parse_args()
    download(url=args.url)
if __name__ == '__main__':
    main()