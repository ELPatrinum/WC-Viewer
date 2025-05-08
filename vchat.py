#!/usr/bin/env python3
"""
WhatsApp Chat Viewer Using PySide6 - Improved UI, Full Messages, Precise Scroll Position (Pruning Aware), Smaller Media, Corrected Event Filter, Terminal Loading Bar with Clean Exit, and Video Thumbnails
"""
import os
import sys
import re
import argparse
import pandas as pd
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QScrollArea,
    QPushButton, QLabel, QFrame, QSizePolicy
)
from PySide6.QtGui import QPixmap, QDesktopServices, QPalette, QColor
from PySide6.QtCore import Qt, QUrl, QTimer, QEvent

# Constants
BATCH_SIZE = 50
MAX_VISIBLE = 200
VIDEO_EXT = {'.mp4', '.mov', '.avi', '.mkv'}
AUDIO_EXT = {'.opus', '.mp3', '.wav'}
IMAGE_EXT = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}


# --- Helper Functions ---
def parse_chat_gen(file_path):
    """Generator yielding parsed messages as dicts, handling long lines."""
    pattern = re.compile(
        r'^\[(\d{1,2}/\d{1,2}/\d{2,4}),\s*(\d{1,2}:\d{2}(?::\d{2})?\s*(?:AM|PM)?)\]\s*(.*?):\s?(.*)$',
        re.IGNORECASE
    )
    current = None
    with open(file_path, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if not line:
                continue
            line = line.replace('\u202f', ' ').replace('\xa0', ' ').replace('\u200e', '')

            m = pattern.match(line)
            if m:
                if current:
                    yield current
                date_str, time_str, sender, msg = m.groups()
                dt_str = f"{date_str} {time_str}"
                dt = pd.to_datetime(dt_str, dayfirst=True, errors='coerce')
                if pd.isna(dt):
                    current = None
                    continue
                current = {'datetime': dt, 'sender': sender, 'message': msg}
            elif current:
                current['message'] += '\n' + line
        if current:
            yield current


def open_media(path):
    """Open file with system default application."""
    QDesktopServices.openUrl(QUrl.fromLocalFile(path))


# --- Main Application Class ---
class ChatViewer(QMainWindow):
    def __init__(self, chat_file, me_name=None, initial_messages=None):
        super().__init__()
        self.chat_file = chat_file
        self.setWindowTitle('WhatsApp Chat Viewer')
        self.resize(600, 800)

        # Improved color scheme for better visibility
        palette = self.palette()
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))  # Black text
        self.setPalette(palette)

        if initial_messages is not None:
            self.messages = initial_messages
            self.total = len(self.messages)
        else:
            self.messages = list(parse_chat_gen(self.chat_file))
            self.total = len(self.messages)

        self.index = 0
        self.me_name = me_name
        self.last_date = None
        self._scroll_position_before_load = 0

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove default margins
        layout.setSpacing(0)  # No spacing between widgets

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn) # Ensure scrollbar is always visible
        layout.addWidget(self.scroll_area)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_layout.setContentsMargins(10, 10, 10, 10) # Add some padding inside the scroll area
        self.scroll_layout.setSpacing(8) # Add spacing between messages
        self.scroll_area.setWidget(self.scroll_content)

        self.load_button = QPushButton('Load more')
        self.load_button.clicked.connect(self._load_batch)
        layout.addWidget(self.load_button)

        self.fullscreen = False
        self.scroll_area.installEventFilter(self)

        # Initial load after show to keep UI responsive
        QTimer.singleShot(0, self._load_batch)

    def eventFilter(self, obj, event):
        from PySide6.QtCore import QEvent

        if event.type() == QEvent.KeyPress:
            key = event.key()
            if key == Qt.Key_F11:
                self.fullscreen = not self.fullscreen
                self.setWindowState(
                    Qt.WindowFullScreen if self.fullscreen else Qt.WindowNoState
                )
                return True
            elif key == Qt.Key_Escape and self.fullscreen:
                self.fullscreen = False
                self.setWindowState(Qt.WindowNoState)
                return True
        return super().eventFilter(obj, event)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._reflow_bubbles()

    def _reflow_bubbles(self):
        available_width = int(self.scroll_area.viewport().width() * 0.75)
        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            if item and item.widget():
                bubble = item.widget()
                for lbl in bubble.findChildren(QLabel):
                    if lbl.property('is_message'):
                        lbl.setMaximumWidth(available_width)
                        lbl.adjustSize()

    def _load_batch(self):
        if self.index >= self.total:
            self.load_button.setText('No more messages')
            self.load_button.setEnabled(False)
            return

        # Store the current scroll position before loading more messages
        scroll_bar = self.scroll_area.verticalScrollBar()
        self._scroll_position_before_load = scroll_bar.value()
        max_scroll_value_before_load = scroll_bar.maximum()
        removed_height = 0

        end = min(self.index + BATCH_SIZE, self.total)
        items_added = 0
        for msg in self.messages[self.index:end]:
            dt, sender, text = msg['datetime'], msg['sender'], msg['message']
            date = dt.date()
            if date != self.last_date:
                date_separator = QLabel(date.strftime('%A, %d %B %Y'))
                date_separator.setStyleSheet(
                    'background: #e0e0e0; font-weight: bold; padding: 6px; color: #333333; border-radius: 6px; margin-bottom: 6px;'
                )
                date_separator.setAlignment(Qt.AlignCenter)
                self.scroll_layout.addWidget(date_separator)
                self.last_date = date
                items_added += 1

            is_me = (self.me_name and sender == self.me_name)
            bubble_bg = '#dcf8c6' if is_me else '#ffffff'
            bubble = QFrame()
            bubble.setFrameShape(QFrame.StyledPanel)
            bubble.setStyleSheet(f"background: {bubble_bg}; padding: 8px; margin-bottom: 8px; border-radius: 10px; border: 1px solid #c0c0c0;")
            bubble_layout = QVBoxLayout(bubble)
            bubble_layout.setContentsMargins(8, 6, 8, 6)
            bubble_layout.setSizeConstraint(QVBoxLayout.SetDefaultConstraint) # Allow vertical expansion of content

            meta_label = QLabel(f"{sender} • {dt.strftime('%H:%M')}")
            meta_label.setStyleSheet('font-size: 9pt; font-style: italic; color: #666666;')
            bubble_layout.addWidget(meta_label)

            message_content = QLabel()
            message_content.setWordWrap(True)
            message_content.setTextInteractionFlags(Qt.TextSelectableByMouse)
            message_content.setStyleSheet('color: #000000;')
            message_content.setProperty('is_message', True) # Mark as message for reflow
            message_content.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)

            media_match = re.search(r'<attached: (.*?)>', text)
            if media_match:
                file_name = media_match.group(1)
                file_path = os.path.join(os.path.dirname(self.chat_file), file_name)
                file_ext = os.path.splitext(file_name)[1].lower()
                if file_ext in IMAGE_EXT and os.path.exists(file_path):
                    pixmap = QPixmap(file_path)
                    target_width = int(self.scroll_area.viewport().width() * 0.3) # Slightly smaller for regular images
                    if file_ext == '.webp':
                        target_width = int(self.scroll_area.viewport().width() * 0.1) # Smaller for stickers
                    scaled_pixmap = pixmap.scaledToWidth(
                        target_width, Qt.SmoothTransformation
                    )
                    image_label = QLabel()
                    image_label.setPixmap(scaled_pixmap)
                    image_label.mousePressEvent = lambda event, path=file_path: open_media(path)
                    image_label.setCursor(Qt.PointingHandCursor)
                    bubble_layout.addWidget(image_label)
                elif file_ext in VIDEO_EXT and os.path.exists(file_path):
                    try:
                        from moviepy.editor import VideoFileClip
                        import tempfile
                        thumbnail_path = os.path.join(tempfile.gettempdir(), f"thumb_{os.path.basename(file_path)}.jpg")
                        # Use a context manager to ensure the clip is closed
                        with VideoFileClip(file_path) as clip:
                            # Get a frame at 1 second
                            if clip.duration > 1:
                                frame_time = 1
                            else:
                                frame_time = clip.duration/2
                            frame_at_time = clip.to_ImageClip(frame_time)
                            frame_at_time.save_frame(thumbnail_path, overwrite=True)

                        if os.path.exists(thumbnail_path):
                            pixmap = QPixmap(thumbnail_path)
                            target_width = int(self.scroll_area.viewport().width() * 0.4)  # Adjust size as needed
                            scaled_pixmap = pixmap.scaledToWidth(target_width, Qt.SmoothTransformation)
                            thumbnail_label = QLabel()
                            thumbnail_label.setPixmap(scaled_pixmap)
                            thumbnail_label.mousePressEvent = lambda event, path=file_path: open_media(path)
                            thumbnail_label.setCursor(Qt.PointingHandCursor)
                            bubble_layout.addWidget(thumbnail_label)
                        else:
                            video_button = QPushButton('▶︎ Play Video')
                            video_button.setStyleSheet(
                                'padding: 6px; border-radius: 5px; background-color: #f0f0f0; color: #333333;')
                            video_button.clicked.connect(lambda _, path=file_path: open_media(path))
                            bubble_layout.addWidget(video_button)

                    except ImportError:
                        video_button = QPushButton('▶︎ Play Video')
                        video_button.setStyleSheet(
                            'padding: 6px; border-radius: 5px; background-color: #f0f0f0; color: #333333;')
                        video_button.clicked.connect(lambda _, path=file_path: open_media(path))
                        bubble_layout.addWidget(video_button)
                    except Exception as e:
                        print(f"Error generating thumbnail for {file_path}: {e}")
                        video_button = QPushButton('▶︎ Play Video')
                        video_button.setStyleSheet(
                            'padding: 6px; border-radius: 5px; background-color: #f0f0f0; color: #333333;')
                        video_button.clicked.connect(lambda _, path=file_path: open_media(path))
                        bubble_layout.addWidget(video_button)

                elif file_ext in AUDIO_EXT and os.path.exists(file_path):
                    audio_button = QPushButton('▶︎ Play Audio')
                    audio_button.setStyleSheet(
                        'padding: 6px; border-radius: 5px; background-color: #f0f0f0; color: #333333;')
                    audio_button.clicked.connect(lambda _, path=file_path: open_media(path))
                    bubble_layout.addWidget(audio_button)
                else:
                    message_content.setText(
                        text.replace('\u202f', ' ').replace('\xa0', ' ').replace('\u200e', ''))
                    bubble_layout.addWidget(message_content)
            else:
                message_content.setText(
                    text.replace('\u202f', ' ').replace('\xa0', ' ').replace('\u200e', ''))
                bubble_layout.addWidget(message_content)

            # Ensure the bubble's layout adjusts to the content
            bubble_layout.invalidate()
            bubble.adjustSize()
            bubble.setMinimumHeight(bubble.height())  # Set minimum height to current height

            alignment = Qt.AlignRight if is_me else Qt.AlignLeft
            self.scroll_layout.addWidget(bubble, alignment=alignment)
            items_added += 1

        self.index = end

        # Restore the scroll position to maintain the user's place
        QTimer.singleShot(0, lambda: self._restore_scroll_position(
            max_scroll_value_before_load, items_added))

        # Prune oldest widgets to keep UI responsive
        widgets_to_remove = self.scroll_layout.count() - MAX_VISIBLE
        for i in range(widgets_to_remove):
            item = self.scroll_layout.takeAt(0)
            if item and item.widget():
                widget = item.widget()
                removed_height += widget.height() + self.scroll_layout.spacing()  # Account for spacing
                widget.deleteLater()

        if removed_height > 0:
            QTimer.singleShot(0, lambda: self._adjust_scroll_after_prune(removed_height))

        if self.index >= self.total:
            self.load_button.setText('No more messages')
            self.load_button.setEnabled(False)

    def _adjust_scroll_after_prune(self, removed_height):
        scroll_bar = self.scroll_area.verticalScrollBar()
        scroll_bar.setValue(max(0, scroll_bar.value() - removed_height))

    def _restore_scroll_position(self, max_before, items_added):
        scroll_bar = self.scroll_area.verticalScrollBar()
        max_after = scroll_bar.maximum()
        current_value = scroll_bar.value()

        if max_after > max_before:
            # Calculate the relative scroll position (percentage)
            relative_position = 0.0
            if max_before > 0:
                relative_position = current_value / max_before

            # Calculate the new absolute scroll position
            new_scroll_value = int(relative_position * max_after)

            # Set the new scroll value
            scroll_bar.setValue(new_scroll_value)
        elif max_after > max_before and current_value == max_before and items_added > 0:
            # If we were at the bottom, stay at the bottom
            scroll_bar.setValue(max_after)



# --- Main Execution ---
def main():
    parser = argparse.ArgumentParser(description='WhatsApp Chat Viewer')
    parser.add_argument('folder', help='Path to extracted chat folder')
    parser.add_argument('--me', dest='me_name', help='Your name for right-aligned bubbles')
    args = parser.parse_args()

    txt_files = [f for f in os.listdir(args.folder) if f.lower().endswith('.txt')]
    if not txt_files:
        print('Error: No .txt chat file found.')
        sys.exit(1)
    chat_file = os.path.join(args.folder, txt_files[-1]) # Assuming the last .txt file is the main chat

    # --- Loading Indicator ---
    def show_loading_bar(progress, total):
        bar_length = 40
        filled_length = int(bar_length * progress // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        print(f'\rParsing chat: [{bar}] {progress}/{total}', end='\r')

    messages = []
    total_lines = 0
    with open(chat_file, 'r', encoding='utf-8') as f:
        for _ in f:
            total_lines += 1

    parsed_count = 0
    print("Parsing chat file...")
    for msg in parse_chat_gen(chat_file):
        messages.append(msg)
        parsed_count += 1
        show_loading_bar(parsed_count, total_lines)

    print("\nChat parsing complete. Opening UI...")
    # --- End Loading Indicator ---

    app = QApplication(sys.argv)

    def on_about_to_quit():
        print("\nClosing Chat UI...")

    app.aboutToQuit.connect(on_about_to_quit)

    viewer = ChatViewer(chat_file, args.me_name, initial_messages=messages) # Pass pre-parsed messages
    viewer.show()
    exit_code = app.exec() # Store the exit code
    return exit_code # Return the exit code


if __name__ == '__main__':
    sys.exit(main())

