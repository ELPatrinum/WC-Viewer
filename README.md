
# WC-Viewer
[![ChatGPT Image May 12, 2025, 09_53_58 AM](https://github.com/user-attachments/assets/1796ce4c-237e-42c7-9da2-08efc8c4b8ce)](https://github.com/ELPatrinum/WC-Viewer)

---

<div align="center">
  <a href="https://discord.gg/AYbJ9MJez7">
    <img alt="WC-Viewer Discord Badge" src="https://img.shields.io/badge/Discord-WC%20Viewer-blue?style=for-the-badge&logo=discord&logoColor=white">
  </a>
</div>

---

# WhatsApp Chat Viewer
![WhatsApp Chat Viewer](https://github.com/user-attachments/assets/bf8e7c0a-c716-499f-b789-8b01a24aa554)

## Overview

WhatsApp Chat Viewer is a Python-based desktop application built with PySide6, designed to provide an easy-to-use graphical interface for viewing WhatsApp chat exports. It supports displaying text messages, images, videos, and audio files directly within the chat interface.

---

<div align="center">
  <a href="#installation"><kbd> Installation </kbd></a>&ensp;&ensp;
  <a href="#usage"><kbd> Usage </kbd></a>&ensp;&ensp;
  <a href="#format"><kbd> Supported Media Formats </kbd></a>
</div>

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

### Prerequisites

Ensure you have Python 3.7+ installed.

### Install Dependencies

```bash
pip install PySide6 pandas moviepy
```

### Download the Script

```bash
git clone https://github.com/ELPatrinum/WC-Viewer.git
```

### Navigate to the Script Directory

```bash
cd WC-Viewer
```

---

### Usage

```bash
python vchat.py /path/to/chat/folder --me "Your Name"
```

* `/path/to/chat/folder`: Directory containing your exported WhatsApp `.txt` chat file and associated media.
* `--me`: (Optional) Specify your name to differentiate your messages (aligned to the right).

### Controls

* **F11**: Toggle fullscreen mode.
* **ESC**: Exit fullscreen mode.
* **Load More Button**: Load older messages manually.

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/4d462c68-638f-4290-8832-ff7607d03153" alt="WC-Viewer Screenshot"/>
</p>

---

## Supported Media Formats

* **Images**: `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif`
* **Videos**: `.mp4`, `.mov`, `.avi`, `.mkv`
* **Audio**: `.opus`, `.mp3`, `.wav`

---

<div align="center">
  <a href="#contributing"><kbd>Contributing</kbd></a>&ensp;&ensp;
  <a href="#license"><kbd>License</kbd></a>
</div>

---

## Contributions

We welcome contributions from the community! To get started:

* Check our [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
* Read about team roles in [TEAM\_ROLES.md](TEAM_ROLES.md).
* Review our release process in [RELEASE\_POLICY.md](RELEASE_POLICY.md).
* Add yourself to [CONTRIBUTORS.md](CONTRIBUTORS.md) when making your first PR.

---

## License

This project is licensed under the MIT License.

---

<div align="right">
  <sub>Last edited on: 16/05/2025</sub>
</div>

<a id="star_history"></a> <img src="https://readme-typing-svg.herokuapp.com?font=Lexend+Giga&size=25&pause=1000&color=CCA9DD&vCenter=true&width=435&height=25&lines=STARS" width="450"/>

---

<a href="https://star-history.com/#ELPatrinum/WC-Viewer">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ELPatrinum/WC-Viewer&type=Timeline&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ELPatrinum/WC-Viewer&type=Timeline" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ELPatrinum/WC-Viewer&type=Timeline" />
 </picture>
</a>

