import sys

# import classes from PySide6.QtWidgets module
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
#from __feature__ import snake_case, true_property

# create a QApplication object
my_app = QApplication([])

class MyWindow(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()
      label1 = QLabel("Hello World")
      label2 = QLabel("<h1>Hello World<h1>")
      vbox.addWidget(label1)
      vbox.addWidget(label2)
      self.setLayout(vbox)
      self.show()

  def __str__(self):
      return "MyWindow"
  def __repr__(self):
      return "MyWindow"

# create a MyWindow object
my_win = MyWindow()

# enter the Qt main loop and start to execute the Qt code
sys.exit(my_app.exec())
