from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QSlider, QHBoxLayout
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog
from pydub import AudioSegment, effects
from PySide6.QtCore import Qt, Slot
import sys
import pydub
import ffmpeg
import os

class SoundWaveEditor(QWidget):
    def __init__(self):
        super().__init__()
        vboxMegaSoundwave = QVBoxLayout()
        self.resize(300, 200)

        #widgets
        self.label1 = QLabel("No file loaded")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.trimmer1 = QSlider()
        self.trimmer2 = QSlider()
        self.label2 = QLabel("0.00s - 0.00s")


        #pixmaps
        self.coolpixmap = QPixmap("Cool-Images/skizzer.png")
        self.coolpixmap1 = QPixmap("Cool-Images/snippy.jpg")
        self.coolpixmap2_TheSqueakuel = QPixmap("Cool-Images/soundwave.png")

        #Qlabels for pixmaps
        self.coolpicture = QLabel()
        self.coolpicture.setScaledContents(True)
        self.coolpicture.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coolpicture.setFixedSize(100,100)
        self.coolpicture1 = QLabel()
        self.coolpicture1.setScaledContents(True)
        self.coolpicture1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coolpicture1.setFixedSize(100,100)
        self.coolpicture2_ElectricBoogaloo = QLabel()
        self.coolpicture2_ElectricBoogaloo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coolpicture2_ElectricBoogaloo.setScaledContents(True)
        self.coolpicture2_ElectricBoogaloo.setFixedSize(100,100)
        self.coolpicture.setPixmap(self.coolpixmap)
        self.coolpicture1.setPixmap(self.coolpixmap1)
        self.coolpicture2_ElectricBoogaloo.setPixmap(self.coolpixmap2_TheSqueakuel)

        #sliders
        self.audio = None
        self.trimmer1.valueChanged.connect(self.updateTrimmers)
        self.trimmer2.valueChanged.connect(self.updateTrimmers)
        self.trimmer1.setValue(0)
        self.trimmer2.setValue(1000)

        #buttons
        selectFileButton = QPushButton("Open Audio File")
        selectFileButton.clicked.connect(self.openFileButton)

        trimButton = QPushButton("Slice and Save")
        trimButton.clicked.connect(self.trimAudio)

        #adding widgets to vboxEditor
        self.coolpicture2_ElectricBoogaloo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vboxMegaSoundwave.addWidget(self.coolpicture2_ElectricBoogaloo)
        vboxMegaSoundwave.addWidget(self.label1)
        vboxMegaSoundwave.addWidget(selectFileButton)
        vboxMegaSoundwave.addWidget(self.label2)
        vboxMegaSoundwave.addWidget(self.trimmer1)
        vboxMegaSoundwave.addWidget(self.trimmer2)
        vboxMegaSoundwave.addWidget(trimButton)

        #setting layout
        self.setWindowTitle("Mega-Soundwave Audio Slicer")
        self.setLayout(vboxMegaSoundwave)
        self.show()

    def updateTrimmers(self):
        self.trimmer1.setValue(self.trimmer1.value())
        self.trimmer2.setValue(self.trimmer2.value())
        if self.trimmer1.value() > self.trimmer2.value():
            self.trimmer1.setValue(self.trimmer2.value()-1)
        self.label2.setText(f"{self.trimmer1.value()/100:.2f}s - {self.trimmer2.value()/100:.2f}s")

    @Slot()
    def openFileButton(self):
        file = QFileDialog.getOpenFileName(self, "Open Audio File", "", "Audio Files (*.mp3 *.wav *.aac *.flac *.ogg)")
        if file[0]:  #only continue once a file is selected
            self.audioFilePath = file[0]  #get the file path
            self.audio = AudioSegment.from_file(self.audioFilePath, format="mp3")
            self.label1.setText(self.audioFilePath)

            self.trimmer1.setMinimum(0)
            self.trimmer1.setMaximum((self.audio.duration_seconds * 1000) - 1)
            self.trimmer2.setMinimum(self.trimmer1.value() + 1)
            self.trimmer2.setMaximum(self.audio.duration_seconds * 1000)
            self.trimmer1.setOrientation(Qt.Orientation.Horizontal)
            self.trimmer2.setOrientation(Qt.Orientation.Horizontal)

        print(self.audioFilePath)

    @Slot()
    def trimAudio(self):
        start = self.trimmer1.value()
        end = self.trimmer2.value()
        audio = AudioSegment.from_file(self.audioFilePath, format="mp3")
        trimmed_audio = audio[start * 1000:end * 1000]

        base_dir, original_name = os.path.split(self.audioFilePath)
        file_name, file_extension = os.path.splitext(original_name)
        newFileName = f"{file_name}_Trimmed{file_extension}"
        newFilePath = os.path.join(base_dir, newFileName)

        trimmed_audio.export(newFilePath, format="mp3")
        self.label1.setText(f"Trimmed audio file saved at: {newFilePath}")