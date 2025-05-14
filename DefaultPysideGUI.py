import sys
import shazam
import numpy as np
# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QMainWindow, QStatusBar, QToolBar, QPushButton, QFileDialog
from PySide6.QtCore import Qt,Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QSizePolicy
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Slot, Qt
import requests
import MegaSoundwave
import Note

from Graphs.GUI_graphs import GraphWindow
from Note import STTWindow

#from __feature__ import snake_case, true_property

# create a QApplication object
my_app = QApplication([])

#-----------------------------------------------------------------------------------------------------------------------

class KaboomGUI(QWidget):
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
         border-radius: 8px;
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
        self.info = QLabel("  Please select an audio file of the song you want to look up:  ")
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
                text = (
                    f"Song: {song['title']}<br>"
                    f"By {song['artist']}<br>"
                    f"Album: {song['album']}<br>"
                )
                # makes sure there is a link to be clicked
                if song['song_link'] != 'No Spotify link available':
                    text += f"Song Link: <a href='{song['song_link']}'>Click here</a>"
                else:
                    text += "No Spotify link available."

                self.results.setText(text)
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

#-----------------------------------------------------------------------------------------------------------------------

class MyWindow(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()

      #Labels
      self.label1 = QLabel("Main Menu")
      self.label1.setAlignment(Qt.AlignCenter)

      self.label2 = QLabel("<h1>Welcome to the Multimedia Tool Suite<h1>")
      self.label2.setAlignment(Qt.AlignCenter)

      #Buttons
      naviButtn1 = QPushButton("Home")
      naviButtn1.clicked.connect(self.naviButtn1_clicked)

      naviButtn2 = QPushButton("Kaboom Song Lookup")
      naviButtn2.clicked.connect(self.naviButtn2_clicked)

      naviButtn3 = QPushButton("MegaSoundwave Audio Slicer")
      naviButtn3.clicked.connect(self.naviButtn3_clicked)

      naviButtn4 = QPushButton("Audio Grapher")
      naviButtn4.clicked.connect(self.naviButtn4_clicked)

      naviButtn5 = QPushButton("Ransom Note Generator")
      naviButtn5.clicked.connect(self.naviButtn5_clicked)

      #Main Menu Widgets
      vbox.addWidget(self.label2)
      vbox.addWidget(self.label1)
      #vbox.addWidget(naviButtn1)
      #UNUSED
      vbox.addWidget(naviButtn2)
      vbox.addWidget(naviButtn3)
      vbox.addWidget(naviButtn4)
      vbox.addWidget(naviButtn5)
      vbox.addStretch()
      self.setWindowTitle("Multimedia Tool Suite")
      self.setLayout(vbox)
      self.show()

  def __str__(self):
      return "MyWindow"

  def __repr__(self):
      return "MyWindow"

  @Slot()
  def naviButtn1_clicked(self):
      self.label1.setText("Home")
      print("Home button clicked")

  @Slot()
  def naviButtn2_clicked(self):
      self.label1.setText("Shazam")
      print("Shazam button clicked")
      self.newWindow = KaboomGUI()
      self.newWindow.show()

#WORKING TOOL SELECTION BUTTON
#COPY THIS FOR THE OTHER TOOLS:
  @Slot()
  def naviButtn3_clicked(self):
      #Print statement for debugging
      print("MegaSoundwave button clicked")
      self.label1.setText("Audio Editor Open")
      self.newWindow = MegaSoundwave.SoundWaveEditor()
      self.newWindow.show()


  @Slot()
  def naviButtn4_clicked(self):
      print("Graph Audio button clicked")
      self.label1.setText("Graph Audio Open")
      self.newWindow = GraphWindow()
      self.newWindow.show()

  @Slot()
  def naviButtn5_clicked(self):
      print("Tool4 button clicked")
      self.label1.setText("Tool4")
      self.newWindow = STTWindow()
      self.newWindow.show()

#-----------------------------------------------------------------------------------------------------------------------

def __main__():
    # create a MyWindow object
    my_win = MyWindow()
    my_win.show()

    # enter the Qt main loop and start to execute the Qt code
    sys.exit(my_app.exec())

if __name__ == "__main__":
    __main__()
