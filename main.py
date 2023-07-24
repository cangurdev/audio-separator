from spleeter.separator import Separator
import yt_dlp as youtube_dl
import os
import re

def download_mp3(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s'
    }

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_name = ydl.prepare_filename(info)
            return file_name
    except youtube_dl.DownloadError:
        print("Error: Unable to download the MP3.")
    except Exception as e:
        print(f"An error occurred: {e}")


def separate_instruments(file_name, output_dir='./output'):
    separator = Separator('spleeter:4stems')
    abs_file_path = os.path.abspath(file_name)

    if not os.path.exists(abs_file_path):
        print(f"Error: File '{abs_file_path}' does not exist.")
        return

    try:
        separator.separate_to_file(file_name, output_dir)
        print(f"Instruments separated successfully. Output files saved in '{output_dir}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = input('Enter the URL of the YouTube video: ')
    file_name = download_mp3(url)
    mp3Name = re.sub('.webm', '', file_name)

    title_without_spaces = re.sub(r'\s+', '-', file_name) + '.mp3'
    title_without_spaces = re.sub('.webm', '', title_without_spaces)

    os.rename(mp3Name + '.mp3', title_without_spaces)
    separate_instruments(title_without_spaces)


