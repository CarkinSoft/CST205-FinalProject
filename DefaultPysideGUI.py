import sys
import shazam

# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot, Qt
import requests
#from __feature__ import snake_case, true_property

# create a QApplication object
my_app = QApplication([])
#  background-color: #1a1a1a;
class ShazamGUI(QWidget):
  def __init__(self):
      super().__init__()
      self.setWindowTitle("Kaboom Song Lookup")
      self.setStyleSheet("""
        QWidget{
            background-color: #1a1a1a;
        }
        QPushButton {
         background-color: #696969;
         border-style: outset;
         border-width: 2px;
         border-radius: 10px;
         border-color: beige;
         font-family: 'Roboto', 'Helvetica Neue', sans-serif;
         font: bold 10px;
         min-width: 10em;
         padding: 6px;
        }
        QPushButton:hover {
          background-color: #333333;
        }
        QLabel {
            color: white;
        }
    """)

      vbox = QVBoxLayout()
      self.welcome = QLabel("Welcome to Kaboom! (A better Shazam!)")
      self.welcome.setAlignment(Qt.AlignCenter)
      self.info = QLabel("Please select an audio file of the song you want to look up:")
      self.album_cover = QLabel()
      self.album_cover.setAlignment(Qt.AlignCenter)
      self.results = QLabel("")
      openFileButton = QPushButton("Open Audio File")
      openFileButton.clicked.connect(self.buttonClicked)
      vbox.addWidget(self.welcome)
      vbox.addWidget(self.album_cover)
      vbox.addWidget(self.results)
      vbox.addWidget(self.info)
      vbox.addWidget(openFileButton)
      self.setLayout(vbox)
      self.show()


  @Slot()
  def buttonClicked(self):
    file, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav *.aac *.flac *.ogg)")

    if file:
        #   self.audioFilePath = file
        #   print(self.audioFilePath)
          song = shazam.shazam(file)
          print(song)
          if "error" in song:
            self.results.setText(song["error"])
          else:
            self.albumCoverImage(song.get("cover_art"))
            self.results.setText(
                f"Song: {song['title']}\n"
                f"By {song['artist']}\n"
                f"Album: {song['album']}\n"
                f"Song Information: {song['song_link']}"
            )

  def albumCoverImage(self, url):
    if not url or url == "No picture available":
        pix = QPixmap("static_images/404.jpeg")
        pix = pix.scaled(300, 300,  Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.album_cover.setPixmap(pix)
        return
        
    downloadImage = requests.get(url)
    if downloadImage.ok:
        pix = QPixmap()
        pix.loadFromData(downloadImage.content)
        pix = pix.scaled(300, 300,  Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.album_cover.setPixmap(pix)

    else:
        self.album_cover.setText("Error loading image...")

# create a MyWindow object
my_win = ShazamGUI()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec())