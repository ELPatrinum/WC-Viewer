# WC-Viewer
# WhatsApp Chat Viewer

## Overview

WhatsApp Chat Viewer is a Python-based desktop application built with PySide6, designed to provide an easy-to-use graphical interface for viewing WhatsApp chat exports. It supports displaying text messages, images, videos, and audio files directly within the chat interface.

---

## Features

* **Intuitive UI**: Clean and user-friendly interface optimized for readability.
* **Media Display**: Supports inline viewing of images and video thumbnails.
* **Audio Playback**: Quick access to audio playback through default system applications.
* **Full Message Parsing**: Handles multiline messages and correctly groups them.
* **Precise Scroll Position**: Maintains your reading position even as older messages are loaded and pruned.
* **Batch Loading**: Efficiently loads chat history in batches for better performance.
* **Fullscreen Mode**: Toggle fullscreen for distraction-free reading.

---

## Installation

### Prerequisites

Ensure you have Python 3.7+ installed.

### Install Dependencies

```bash
pip install PySide6 pandas moviepy
```

---

## Usage

```bash
python chat_viewer.py /path/to/chat/folder --me "Your Name"
```

* `/path/to/chat/folder`: Directory containing your exported WhatsApp `.txt` chat file and associated media.
* `--me`: (Optional) Specify your name to differentiate your messages (aligned to the right).

### Controls

* **F11**: Toggle fullscreen mode.
* **ESC**: Exit fullscreen mode.
* **Load More Button**: Load older messages manually.

---

## Supported Media Formats

* **Images**: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`
* **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`
* **Audio**: `.opus`, `.mp3`, `.wav`

---

## Contributions

Feel free to fork, improve, and submit pull requests.

---

## License

This project is licensed under the MIT License.
