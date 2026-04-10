# ConvertToOGG

`input` 폴더에 넣은 오디오 파일을 **OGG로 변환**하는 간단한 스크립트입니다.

- Python + `pydub`만 설치하면 됩니다.
- 변환에는 **FFmpeg**가 필요합니다.
- `input` 폴더에 파일 넣고 `start.bat` 실행하면 끝.

---

## 준비물

- Windows
- Python (권장: 3.9+)
- FFmpeg
- Python 라이브러리: `pydub`

---

## 설치

### 1) Python 설치 확인

```bash
python --version
```

### 2) pydub 설치

```bash
pip install pydub
```

### 3) FFmpeg 설치 및 PATH 등록

FFmpeg를 설치한 뒤, `ffmpeg.exe`가 들어있는 폴더(보통 `...\\ffmpeg\\bin`)를 **환경변수 PATH**에 추가하세요.

설치 확인:

```bash
ffmpeg -version
```

---

## 사용 방법

1. 변환할 오디오 파일을 `input` 폴더에 넣습니다.
2. `start.bat`를 실행합니다.

변환이 끝나면 OGG 파일이 생성됩니다.

---

## Troubleshooting

### `ffmpeg`를 찾을 수 없다고 나와요

- FFmpeg가 설치되어 있는지 확인
- PATH에 `ffmpeg\\bin`이 등록되어 있는지 확인
- 새 터미널을 열고 `ffmpeg -version` 다시 실행

### `ModuleNotFoundError: No module named 'pydub'`

```bash
pip install pydub
```
