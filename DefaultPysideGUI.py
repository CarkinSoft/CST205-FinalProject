import sys
import numpy as np
# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QMainWindow, QStatusBar, QToolBar, QPushButton, QFileDialog
from PySide6.QtCore import Qt,Slot
from PySide6.QtGui import QPixmap
#from __feature__ import snake_case, true_property

# create a QApplication object
my_app = QApplication([])


#-----------------------------------------------------------------------------------------------------------------------
class EditorWindow(QWidget):
    def __init__(self):
        super().__init__()
        vboxEditor = QVBoxLayout()

        #labels
        self.label1 = QLabel("Audio Editor")
        self.label1.setAlignment(Qt.AlignCenter)

        self.label2 = QLabel("<h1>Select an audio file to edit<h1>")
        self.label2.setAlignment(Qt.AlignCenter)

        self.label3 = QLabel("PLACEHOLDER")
        self.label3.setAlignment(Qt.AlignCenter)


        #buttons
        selectFileButton = QPushButton("Open Audio File")
        selectFileButton.clicked.connect(self.openFileButton)

        #adding widgets to vboxEditor
        vboxEditor.addWidget(self.label1)
        vboxEditor.addWidget(self.label2)
        vboxEditor.addWidget(self.label3)
        vboxEditor.addWidget(selectFileButton)
        vboxEditor.addStretch()

        #setting layout
        self.setWindowTitle("Audio Editor")
        self.setLayout(vboxEditor)
        self.show()

    @Slot()
    def openFileButton(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav *.aac *.flac *.ogg)")

        if file:
            self.audioFilePath = file
        print(self.audioFilePath)

#-----------------------------------------------------------------------------------------------------------------------





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

      naviButtn2 = QPushButton("Tool1")
      naviButtn2.clicked.connect(self.naviButtn2_clicked)

      naviButtn3 = QPushButton("Tool2")
      naviButtn3.clicked.connect(self.naviButtn3_clicked)

      naviButtn4 = QPushButton("Tool3")
      naviButtn4.clicked.connect(self.naviButtn4_clicked)

      naviButtn5 = QPushButton("Tool4")
      naviButtn5.clicked.connect(self.naviButtn5_clicked)

      #Main Menu Widgets
      vbox.addWidget(self.label2)
      vbox.addWidget(self.label1)
      vbox.addWidget(naviButtn1)
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
      self.label1.setText("Tool1")

  @Slot()
  def naviButtn3_clicked(self):
      #Print statement for debugging
      print("Tool2 button clicked")
      self.label1.setText("Audio Editor Open")
      self.newWindow = EditorWindow()
      self.newWindow.show()


  @Slot()
  def naviButtn4_clicked(self):
      self.label1.setText("Tool3")

  @Slot()
  def naviButtn5_clicked(self):
      self.label1.setText("Tool4")
#-----------------------------------------------------------------------------------------------------------------------

def __main__():
    # create a MyWindow object
    my_win = MyWindow()
    my_win.show()

    # enter the Qt main loop and start to execute the Qt code
    sys.exit(my_app.exec())

if __name__ == "__main__":
    __main__()
