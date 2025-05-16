To modify the style of your README file, adding a light green color and a "keyboard input" style to the titles, you can't directly apply CSS styling in a standard Markdown file, but you can adapt the visual structure to make it look more like what you're envisioning.

Here's an updated version of your README content with the style applied in Markdown:

# WC-Viewer
# WhatsApp Chat Viewer
![ChatGPT Image May 12, 2025, 09_53_58 AM](https://github.com/user-attachments/assets/1796ce4c-237e-42c7-9da2-08efc8c4b8ce)

## Overview

WhatsApp Chat Viewer is a Python-based desktop application built with PySide6, designed to provide an easy-to-use graphical interface for viewing WhatsApp chat exports. It supports displaying text messages, images, videos, and audio files directly within the chat interface.

![May 12, 2025, 09_49_30 AM](https://github.com/user-attachments/assets/bf8e7c0a-c716-499f-b789-8b01a24aa554)

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
````

### Download the Script

```bash
git clone https://github.com/ELPatrinum/WC-Viewer.git
```

### Get into the Script directory

```bash
cd WC-Viewer
```

---

## Usage

![Screenshot 2025-05-12 094027](https://github.com/user-attachments/assets/4d462c68-638f-4290-8832-ff7607d03153)

```bash
python vchat.py /path/to/chat/folder --me "Your Name"
```

* `/path/to/chat/folder`: Directory containing your exported WhatsApp .txt chat file and associated media.
* `--me`: (Optional) Specify your name to differentiate your messages (aligned to the right).

### Controls

* **F11**: Toggle fullscreen mode.
* **ESC**: Exit fullscreen mode.
* **Load More Button**: Load older messages manually.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/7e46b9a1-b4e4-4c6a-a50e-68437f97211c" alt="Screenshot 2025-05-12 094258" />
</p>

---

## Supported Media Formats

* **Images**: .jpg, .jpeg, .png, .webp, .gif
* **Videos**: .mp4, .mov, .avi, .mkv
* **Audio**: .opus, .mp3, .wav

---

## Contributions

Feel free to fork, improve, and submit pull requests.

---

## License

This project is licensed under the MIT License.

---

<style>
  ## Overview, ## Features, ## Installation, ## Usage, ## Supported Media Formats, ## Contributions, ## License {
    color: lightgreen;
    font-family: "Courier New", Courier, monospace;
  }
</style>

