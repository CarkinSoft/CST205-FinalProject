import sys

# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QCheckBox, QMainWindow, QStatusBar, QToolBar
from PySide6.QtCore import Qt,Slot
from PySide6.QtGui import QPixmap
#from __feature__ import snake_case, true_property

# create a QApplication object
my_app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

class MyWindow(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()

      #Labels
      self.label1 = QLabel("Main Menu")
      self.label1.setAlignment(Qt.AlignCenter)
      self.label1.setFixedHeight(100)
      self.label1.setFixedWidth(100)

      label2 = QLabel("<h1>Welcome to the Multimedia Tool Suite<h1>")
      label2.setAlignment(Qt.AlignCenter)
      label2.setFixedHeight(100)
      label2.setFixedWidth(100)

      #Buttons
      naviButtn1 = QPushButton("Home")
      naviButtn1.setFixedHeight(50)
      naviButtn1.setFixedWidth(100)
      naviButtn1.clicked.connect(self.naviButtn1_clicked)

      naviButtn2 = QPushButton("Tool1")
      naviButtn2.setFixedHeight(50)
      naviButtn2.setFixedWidth(100)
      #naviButtn2.clicked.connect(self.naviButtn2_clicked)

      naviButtn3 = QPushButton("Tool2")
      naviButtn3.setFixedHeight(50)
      naviButtn3.setFixedWidth(100)
      #naviButtn3.clicked.connect(self.naviButtn3_clicked)

      naviButtn4 = QPushButton("Tool3")
      naviButtn4.setFixedHeight(50)
      naviButtn4.setFixedWidth(100)
      #naviButtn4.clicked.connect(self.naviButtn4_clicked)

      naviButtn5 = QPushButton("Tool4")
      naviButtn5.setFixedHeight(50)
      naviButtn5.setFixedWidth(100)
      #naviButtn5.clicked.connect(self.naviButtn5_clicked)

      #Main Menu Widgets
      vbox.addWidget(label1)
      vbox.addWidget(label2)
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
      self.label1.setText("Tool2")

  @Slot()
  def naviButtn4_clicked(self):
      self.label1.setText("Tool3")

  @Slot()
  def naviButtn5_clicked(self):
      self.label1.setText("Tool4")


# create a MyWindow object
my_win = MyWindow()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec())
