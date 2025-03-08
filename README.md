# Multi-Language Detector

## Overview

This Python script detects the language of text files in a specified folder using **MediaPipe's Language Detector**. It processes multiple `.txt` files and prints the detected language(s) along with their probabilities.

## Features

- Automatically detects text files in a folder.
- Uses **MediaPipe's Language Detector** to identify languages.
- Displays language names, ISO codes, and detection probabilities.
- Skips empty files and handles errors gracefully.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- MediaPipe
- `language_detector.tflite` model file

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Jhonelkour/multi-language-detector.git
   cd multi-language-detector
   ```
2. vInstall dependencies:
   ```bash
   pip install mediapipe
   ```
3. Place your text files in the same directory or update `FOLDER_PATH` in the script.
4. Ensure `language_detector.tflite` is in the project directory.

## Usage

Run the script:

```bash
python detect_language.py
```

## Expected Output

For a text file containing **French text**, the output might be:

```
📂 Processing: example.txt
📝 Detected Languages:
  - fr (French): (0.98)
✅ All files processed.
```

## Supported Languages

The script supports multiple languages, including:

- English (`en`)
- French (`fr`)
- Spanish (`es`)
- German (`de`)
- Italian (`it`)
- Arabic (`ar`)
- Chinese (`zh`)
- Japanese (`ja`)
- Many more...
