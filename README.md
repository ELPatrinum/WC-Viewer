<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    kbd {
      font-family: "Courier New", monospace;
      font-size: 16px;
      color: lightgreen;  /* Light green color */
      padding: 0.2em 0.5em;
      background-color: #2a2a2a;
      border-radius: 4px;
    }

    h1, h2, h3 {
      margin-bottom: 10px;
    }
  </style>
  <title>WC-Viewer Documentation</title>
</head>
<body>

  <h1><a href="#installation"><kbd>Installation</kbd></a></h1>
  <h2><a href="#updating"><kbd>Updating</kbd></a></h2>
  <h2><a href="#themes"><kbd>Themes</kbd></a></h2>
  <h2><a href="#styles"><kbd>Styles</kbd></a></h2>
  <h2><a href="CONTRIBUTING.md"><kbd>Contributing</kbd></a></h2>
  <h2><a href="KEYBINDINGS.md"><kbd>Keybindings</kbd></a></h2>
  <h2><a href="https://www.youtube.com/watch?v=2rWqdKU1vu8&list=PLt8rU_ebLsc5yEHUVsAQTqokIBMtx3RFY&index=1"><kbd>Youtube</kbd></a></h2>
  <h2><a href="https://hydeproject.pages.dev/"><kbd>Wiki</kbd></a></h2>
  <h2><a href="https://discord.gg/qWehcFJxPa"><kbd>Discord</kbd></a></h2>

  <h1>WC-Viewer</h1>
  <h2>WhatsApp Chat Viewer</h2>
  <img src="https://github.com/user-attachments/assets/1796ce4c-237e-42c7-9da2-08efc8c4b8ce" alt="ChatGPT Image May 12, 2025, 09_53_58 AM">

  <h2 id="overview">Overview</h2>
  <p>WhatsApp Chat Viewer is a Python-based desktop application built with PySide6...</p>
  <img src="https://github.com/user-attachments/assets/bf8e7c0a-c716-499f-b789-8b01a24aa554" alt="May 12, 2025, 09_49_30 AM">

  <h2 id="features">Features</h2>
  <ul>
    <li><kbd>Intuitive UI</kbd>: Clean and user-friendly interface optimized for readability.</li>
    <li><kbd>Media Display</kbd>: Supports inline viewing of images and video thumbnails.</li>
    <li><kbd>Audio Playback</kbd>: Quick access to audio playback through default system applications.</li>
    <li><kbd>Full Message Parsing</kbd>: Handles multiline messages and correctly groups them.</li>
    <li><kbd>Precise Scroll Position</kbd>: Maintains your reading position even as older messages are loaded and pruned.</li>
    <li><kbd>Batch Loading</kbd>: Efficiently loads chat history in batches for better performance.</li>
    <li><kbd>Fullscreen Mode</kbd>: Toggle fullscreen for distraction-free reading.</li>
  </ul>

  <h2 id="installation">Installation</h2>
  <h3>Prerequisites</h3>
  <p>Ensure you have Python 3.7+ installed.</p>

  <h3>Install Dependencies</h3>
  <pre><code>pip install PySide6 pandas moviepy</code></pre>
  
  <h3>Download the Script</h3>
  <pre><code>git clone https://github.com/ELPatrinum/WC-Viewer.git</code></pre>
  
  <h3>Get into the Script directory</h3>
  <pre><code>cd WC-Viewer</code></pre>

  <h2 id="usage">Usage</h2>
  <img src="https://github.com/user-attachments/assets/4d462c68-638f-4290-8832-ff7607d03153" alt="Screenshot 2025-05-12 094027">
  
  <pre><code>python vchat.py /path/to/chat/folder --me "Your Name"</code></pre>
  <p>* `/path/to/chat/folder`: Directory containing your exported WhatsApp `.txt` chat file and associated media.</p>
  <p>* `--me`: (Optional) Specify your name to differentiate your messages (aligned to the right).</p>

  <h3>Controls</h3>
  <ul>
    <li><kbd>F11</kbd>: Toggle fullscreen mode.</li>
    <li><kbd>ESC</kbd>: Exit fullscreen mode.</li>
    <li><kbd>Load More Button</kbd>: Load older messages manually.</li>
  </ul>

  <h2>Supported Media Formats</h2>
  <ul>
    <li><kbd>Images</kbd>: .jpg, .jpeg, .png, .webp, .gif</li>
    <li><kbd>Videos</kbd>: .mp4, .mov, .avi, .mkv</li>
    <li><kbd>Audio</kbd>: .opus, .mp3, .wav</li>
  </ul>

  <h2>Contributions</h2>
  <p>Feel free to fork, improve, and submit pull requests.</p>

  <h2>License</h2>
  <p>This project is licensed under the MIT License.</p>

</body>
</html>
