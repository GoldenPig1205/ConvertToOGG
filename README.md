# ConvertToOGG

This is a simple script to **convert** audio files placed in the `input` folder to OGG.

- You only need to install Python and `pydub`.

- **FFmpeg** is required for the conversion.

- Just place the files in the `input` folder and run `start.bat`. That's it.

---

## Prerequisites

- Windows

- Python (Recommended: 3.9+)

- FFmpeg

- Python Library: `pydub`

---

## Installation

### 1) Verify Python Installation

```bash
python --version

```

### 2) Install PyDub

```bash
pip install pydub

```

### 3) Install FFmpeg and Add to PATH

After installing FFmpeg, add the folder containing `ffmpeg.exe` (usually `...\\ffmpeg\\bin`) to the **environment variable PATH**.

Installation Verification:

```bash
ffmpeg -version

```

---

## How to Use

1. Place the audio file to be converted into the `input` folder.

2. Run `start.bat`.

Once the conversion is complete, an OGG file will be generated.

---

## Troubleshooting

### It says `ffmpeg` cannot be found

- Check if FFmpeg is installed

- Check if `ffmpeg\\bin` is registered in the PATH

- Open a new terminal and run `ffmpeg -version` again

### `ModuleNotFoundError: No module named 'pydub'`

```bash
pip install pydub

```
