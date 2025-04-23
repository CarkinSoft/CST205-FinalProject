import sys
import shazam

# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from PySide6.QtCore import Slot
#from __feature__ import snake_case, true_property

# create a QApplication object
my_app = QApplication([])

class ShazamGUI(QWidget):
  def __init__(self):
      super().__init__()
      self.audioFilePath = None
      vbox = QVBoxLayout()
    #   label1 = QLabel(f"{shazam.shazam(audio_file)}")
      openFileButton = QPushButton("Open Audio File")
      openFileButton.clicked.connect(self.buttonClicked)
    #   vbox.addWidget(label1)
      vbox.addWidget(openFileButton)
      self.setLayout(vbox)
      self.show()


  @Slot()
  def buttonClicked(self):
    file, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav *.aac *.flac *.ogg)")

    if file:
          self.audioFilePath = file
          print(self.audioFilePath)

# create a MyWindow object
my_win = ShazamGUI()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec())