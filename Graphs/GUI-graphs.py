import sys
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                                QLabel, QLineEdit, QComboBox,
                                 QPushButton)
from PySide6.QtCore import Qt
from __feature__ import snake_case, true_property

# Set up app
my_app = QApplication([])

class GraphWindow(QWidget):
  def __init__(self):
      super().__init__()

      # Main feature layout
      main_layout = QVBoxLayout()
      self.title = QLabel("Audio Graphs")

      # File input
      self.filename = QLineEdit("Enter file name with extension (.mp3, .wav)")
      main_layout.add_widget(self.filename)

      # Graph selection
      self.cbox = QComboBox()
      self.desc_label = QLabel("Description: ")
      # Default prompt
      self.cbox.add_item("Pick a graph")
      self.cbox.set_item_data(0, 0, role=Qt.UserRole - 1)
      # Graph descriptions
      self.graph_desc = {"MFCC" : "Mel-frequency cepstral coefficients, sometimes refered to as audio finger prints are used in music and speech recognition",
                    "Spectrogram" : "Visualizes how the frequency of sound change over time.",
                    "Beat Markers" : "Displays detected beat positions in the audio signal.",
                    "Waveform" : "A sound wave showing the amplitude (loudness) of the audio signal over time.",
                    "Mel" : "A spectrogram scaled to better represent how humans percive sound amplitude",
                    }
      self.cbox.add_items(self.graph_desc.keys())
      self.cbox.currentTextChanged.connect(self.update_desc)
      main_layout.add_widget(self.cbox)
      main_layout.add_widget(self.desc_label)

      # Create graph button
      btn = QPushButton("Make Graph!")
      # Function call on button click, not implemented yet
      # btn.clicked.connect(self.make_graph)
      main_layout.add_widget(btn)

      # Display graph
      self.graph_image = QLabel()
      main_layout.add_widget(self.graph_image)

      # Display window
      self.set_layout(main_layout)
      self.show()

  # when a graph is selected from the combo box, give a description of what its displaying
  def update_desc(self, graph_name):
    if graph_name in self.graph_desc:
      graph_desc = self.graph_desc[graph_name]
      self.desc_label.text = f"Description: {graph_desc}"
    else:
       self.desc_label.text = f"Description:"

  # def make_graph():
  #    return


my_win = GraphWindow()

sys.exit(my_app.exec())