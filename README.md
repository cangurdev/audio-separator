# Audio Separator

Audio Separator is a Python project that allows you to download MP3 audio from a given YouTube URL using the [yt_dlp](https://github.com/yt-dlp/yt-dlp) library and then separates the audio tracks using the [spleeter](https://github.com/deezer/spleeter) library.

It separates the audio track into 4 parts in output directory
-   Drums
-   Bass
-   Vocals
-   Other

## Requirements

- python 3.x
- yt_dlp library
- spleeter library

## Installation

1. Clone the repository:


```bash
git clone https://github.com/cvngur/audio-separator.git
cd audio-separator
```

2. Install the required libraries:

```bash
pip install yt-dlp spleeter
```

## Usage

Run the Python script

```bash
python3 main.py
```

## Contributing

Contributions are welcome! If you find any bugs or want to add new features, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.