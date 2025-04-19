import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from __feature__ import snake_case, true_property

my_app = QApplication([])

class MyWindow(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()
      label1 = QLabel('Shea')
      label2 = QLabel('<h1>Gallagher</h1>')
      vbox.add_widget(label1)
      vbox.add_widget(label2)
      self.set_layout(vbox)
      self.show()

my_win = MyWindow()

sys.exit(my_app.exec())