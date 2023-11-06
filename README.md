# SoundCrypt
Hiding confidential messages within wave audio files.

## What is SoundCrypt?
SoundCrypt is a Python-based program designed for seamless audio steganography. With SoundCrypt, you have the power to securely hide your private text messages within wave audio files. These audio files can be played on any media player, enabling you to discreetly share your confidential messages with others.

## Key Features
- **Embedding Tool:** Use the "SoundCrypt.py" script to seamlessly hide text messages within wave audio files. This tool provides a user-friendly command-line interface for selecting the audio file, inputting your message, and specifying the output file.

- **Extraction Tool:** The "Extract.py" script simplifies the process of extracting hidden messages from audio files without altering the original audio content.

- **Wave Audio File Support:** SoundCrypt supports wave audio files, a widely used audio format.

- **Message Security:** Messages are securely concealed within the audio files, ensuring the utmost confidentiality.

- **Intuitive Command Line:** Both tools offer an intuitive command-line interface, making it easy for users to interact with the steganography process.

## Requirements
- Python 3 is required to use SoundCrypt.
  
## Getting Started
To embark on your journey with SoundCrypt, follow these steps:

## Installation
To get started with SoundCrypt, follow these steps:

```
git clone https://github.com/your-username/SoundCrypt.git
cd SoundCrypt
```

## Usage
SoundCrypt comprises two Python scripts:
- **SoundCrypt.py**: Use this script to embed secret information within audio files.
- **Extract.py**: Use this script to extract hidden information from wave audio files.

### Embed Secret Information in Audio Files

```bash
python3 SoundCrypt.py -f demo.wav -m "Your Secret Message" -o output.wav
```
#Extract Secret Information from Audio Files
```
python3 Extract.py -f output.wav
```
