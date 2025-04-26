import sys
import shazam

# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QSizePolicy
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
      self.setWindowTitle("Kaboom Song Lookup") # window title

      # this is what determines the color, size and look of the window
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
         font-family: 'Avenir', sans-serif;
         font: 14px;
         padding: 6px;
        }
        QPushButton:hover {
          background-color: #333333;
        }
        QLabel {
            color: white;
            font: 14px;
            font-family: 'Avenir, sans-serif;
        }
    """)

      vbox = QVBoxLayout()

      # setting margins for space but it seems to not work
      vbox.setSpacing(5)
      vbox.setContentsMargins(0, 0, 0, 0)


      self.welcome = QLabel("Welcome to Kaboom! (A better Shazam!)")
      self.welcome.setAlignment(Qt.AlignCenter) # centering text
      self.info = QLabel("Please select an audio file of the song you want to look up:")
      self.info.setContentsMargins(0, 0, 0, 0) # more margins
      self.info.setAlignment(Qt.AlignCenter) # centering text
      self.album_cover = QLabel()
      self.album_cover.setAlignment(Qt.AlignCenter) # centering text

      # putting a default image in place of the album cover
      pix = QPixmap("static_images/kaboom.jpg")
      pix = pix.scaled(300, 300,  Qt.KeepAspectRatio, Qt.SmoothTransformation)
      self.album_cover.setPixmap(pix)

      # empty label which updates when song is searched for
      self.results = QLabel("")
      self.results.setAlignment(Qt.AlignCenter)

      # button creation and customization (size specifically)
      openFileButton = QPushButton("Open Audio File")
      openFileButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
      openFileButton.setMinimumSize(350, 30)
      openFileButton.clicked.connect(self.buttonClicked) # connects the button

      # adding everthing into layout
      vbox.addWidget(self.welcome)
      vbox.addWidget(self.album_cover)
      vbox.addWidget(self.results)
      vbox.addWidget(self.info)
      vbox.addWidget(openFileButton, alignment=Qt.AlignCenter)
      self.setLayout(vbox)
      self.show()


  @Slot()
  def buttonClicked(self):
    # allows you to open your file manager and returns the path of that file (I formatted it only for audio files)
    file, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav *.aac *.flac *.ogg)")

    if file:
        #   self.audioFilePath = file
        #   print(self.audioFilePath)
          song = shazam.shazam(file) # runs the shazam api code

          if "error" in song:
            self.results.setText(song["error"])
          else:
            self.albumCoverImage(song.get("cover_art"))
            self.results.setTextFormat(Qt.RichText) # allows for html
            self.results.setText(
                f"Song: {song['title']}<br>"
                f"By {song['artist']}<br>"
                f"Album: {song['album']}<br>"
                f"Song Link: <a href='{song['song_link']}'>Click here</a>"
            )
            self.results.setOpenExternalLinks(True) # allows for links to be clickable

  def albumCoverImage(self, url):
    if not url or url == "No picture available":
        pix = QPixmap("static_images/404.jpeg")
        pix = pix.scaled(300, 300,  Qt.KeepAspectRatio, Qt.SmoothTransformation) # keeps aspect ration no matter the size change and ensures quality
        self.album_cover.setPixmap(pix)
        return
        
    downloadImage = requests.get(url) # downloads image url
    
    # adds that image into the existing album cover label
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