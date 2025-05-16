# <kbd><span style="color: #90EE90;">WC-Viewer</span></kbd>
# <kbd><span style="color: #90EE90;">WhatsApp Chat Viewer</span></kbd>
![ChatGPT Image May 12, 2025, 09_53_58 AM](https://github.com/user-attachments/assets/1796ce4c-237e-42c7-9da2-08efc8c4b8ce)

## <kbd><span style="color: #90EE90;">Overview</span></kbd>

WhatsApp Chat Viewer is a Python-based desktop application built with PySide6, designed to provide an easy-to-use graphical interface for viewing WhatsApp chat exports. It supports displaying text messages, images, videos, and audio files directly within the chat interface.

![May 12, 2025, 09_49_30 AM](https://github.com/user-attachments/assets/bf8e7c0a-c716-499f-b789-8b01a24aa554)

---

## <kbd><span style="color: #90EE90;">Features</span></kbd>

* **Intuitive UI**: Clean and user-friendly interface optimized for readability.
* **Media Display**: Supports inline viewing of images and video thumbnails.
* **Audio Playback**: Quick access to audio playback through default system applications.
* **Full Message Parsing**: Handles multiline messages and correctly groups them.
* **Precise Scroll Position**: Maintains your reading position even as older messages are loaded and pruned.
* **Batch Loading**: Efficiently loads chat history in batches for better performance.
* **Fullscreen Mode**: Toggle fullscreen for distraction-free reading.

---

## <kbd><span style="color: #90EE90;">Installation</span></kbd>

### <kbd><span style="color: #90EE90;">Prerequisites</span></kbd>

Ensure you have Python 3.7+ installed.

### <kbd><span style="color: #90EE90;">Install Dependencies</span></kbd>

```bash
pip install PySide6 pandas moviepy
````

### \<kbd\>\<span style="color: \#90EE90;"\>Download the Script\</span\>\</kbd\>

```bash
git clone [https://github.com/ELPatrinum/WC-Viewer.git](https://github.com/ELPatrinum/WC-Viewer.git)
```

### \<kbd\>\<span style="color: \#90EE90;"\>Get into the Script directory\</span\>\</kbd\>

```bash
cd WC-Viewer
```

-----

## \<kbd\>\<span style="color: \#90EE90;"\>Usage\</span\>\</kbd\>

```bash
python vchat.py /path/to/chat/folder --me "Your Name"
```

  * `/path/to/chat/folder`: Directory containing your exported WhatsApp .txt chat file and associated media.
  * `--me`: (Optional) Specify your name to differentiate your messages (aligned to the right).

### \<kbd\>\<span style="color: \#90EE90;"\>Controls\</span\>\</kbd\>

  * **F11**: Toggle fullscreen mode.
  * **ESC**: Exit fullscreen mode.
  * **Load More Button**: Load older messages manually.

-----

\<p align="center"\>
\<img src="https://github.com/user-attachments/assets/7e46b9a1-b4e4-4c6a-a50e-68437f97211c" alt="Screenshot 2025-05-12 094258" /\>
\</p\>

-----

## \<kbd\>\<span style="color: \#90EE90;"\>Supported Media Formats\</span\>\</kbd\>

  * **Images**: .jpg, .jpeg, .png, .webp, .gif
  * **Videos**: .mp4, .mov, .avi, .mkv
  * **Audio**: .opus, .mp3, .wav

-----

## \<kbd\>\<span style="color: \#90EE90;"\>Contributions\</span\>\</kbd\>

Feel free to fork, improve, and submit pull requests.

-----

## \<kbd\>\<span style="color: \#90EE90;"\>License\</span\>\</kbd\>

This project is licensed under the MIT License.
