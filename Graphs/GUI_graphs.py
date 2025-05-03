import sys
import os
# from Graphs import graphs 	# Use if this file is being run from DefaultPysideGUI.py
import graphs 			# Use if running this file directly
from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
							   QLineEdit, QComboBox, QPushButton, QFileDialog)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap
from PIL import Image, ImageQt
# from __feature__ import snake_case, true_property


class GraphWindow(QWidget):
	def __init__(self):
		super().__init__()

		# Main feature layout
		main_layout = QVBoxLayout()
		self.resize(500, 300)
		self.title = QLabel("Graph Audio")
		self.title.setAlignment(Qt.AlignCenter)
		self.title.setStyleSheet("font-size: 24px; font-weight: bold;")
		main_layout.addWidget(self.title)

		# File selection
		selectFileButton = QPushButton("Select Audio File")
		selectFileButton.clicked.connect(self.buttonClicked)
		# Empty label for selected file
		self.file_path = QLabel("")
		main_layout.addWidget(selectFileButton)
		main_layout.addWidget(self.file_path)

		# Graph selection
		self.cbox = QComboBox()
		self.desc_label = QLabel("Description: ")
		# Default prompt
		self.cbox.addItem("Pick a graph")
		self.cbox.setItemData(0, 0, role=Qt.UserRole - 1)
		# Graph descriptions
		self.graph_desc = {"MFCC" : "Mel-frequency cepstral coefficients, sometimes refered to as audio finger prints are used in music and speech recognition",
						"Spectrogram" : "Visualizes how the frequency of sound change over time.",
						"Waveform" : "A sound wave showing the amplitude (loudness) of the audio signal over time.",
						"Mel" : "A spectrogram scaled to better represent how humans percive sound amplitude",
						}
		self.cbox.addItems(self.graph_desc.keys())
		self.cbox.currentTextChanged.connect(self.update_desc)
		main_layout.addWidget(self.cbox)
		main_layout.addWidget(self.desc_label)

		# Create graph button
		btn = QPushButton("Make Graph!")
		# Function call on button click
		btn.clicked.connect(self.make_graph)
		main_layout.addWidget(btn)

		# Display graph
		self.graph_image = QLabel()
		main_layout.addWidget(self.graph_image)

		# Display window
		self.setLayout(main_layout)
		self.show()

  	# When a graph is selected from the combo box, give a description of the graph
	def update_desc(self, graph_type):
		if graph_type in self.graph_desc:
			graph_desc = self.graph_desc[graph_type]
			# self.desc_label.text = f"Description: {graph_desc}"
			self.desc_label.setText(f"Description: {graph_desc}")

		else:
			self.desc_label.setText(f"Description:")

	# Select a file from file manager and returns the path of that file
	@Slot()
	def buttonClicked(self):
		file, _ = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav *.aac *.flac *.ogg)")
		if file:
			self.file = file
		# Display selected file name
		file_name = os.path.basename(file)
		self.file_path.setText(f"Selected file: {file_name}")

	# Generate graph	
	def make_graph(self):
		file_path = self.file
		graph_type = self.cbox.currentText()
		
		# Generate graph using graphs.py
		try:
			# Call graphing function
			graphs.make_graph(file_path, graph_type)
			# Display graph image as pixmap
			graph_pixmap = QPixmap("OutputGraphs/graph.png")
			self.graph_image.setPixmap(graph_pixmap)

		except Exception as e:
			print("Exception while loading image:", e)
			self.desc_label.setText(f"Error generating graph")
    
if __name__ == "__main__":
	# Set up app, if run directly (not from DeafaultPysideGUI.py)
	my_app = QApplication([])
	my_win = GraphWindow()
	my_win.show()
	sys.exit(my_app.exec())
