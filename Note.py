# pip install speechrecognition
# pip install pyaudio
# pip install pyttsx3

import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PySide6.QtCore import Qt, Slot
import speech_recognition as sr
import pyttsx3 
from PIL import Image

# This function takes input from your microphone and returns what it thinks you said.
# It gets an error a lot but it will keep calling the function until it works.
def get_text_from_speech():
    r = sr.Recognizer() 
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            audio = r.listen(source2)
            
            phrase = r.recognize_google(audio)
            phrase = phrase.lower()
            
            print(phrase)
            return phrase
            
    except sr.RequestError as e:
        print("Could not request results {0}".format(e))
    except sr.UnknownValueError:
        print("unknown error occurred")
        return get_text_from_speech()

def ransom_note(text):
    words = text.split()
    word_count = 0
    char_count = 0

    for w in words:
        word_count = word_count + 1
        curr_char_count = 0
        for c in w:
            curr_char_count = curr_char_count + 1
        if curr_char_count > char_count:
            char_count = curr_char_count

    my_note = Image.new('RGB', (600 * char_count, 600 * word_count), 'salmon')

    
    
    curr_y = 5
    curr_x = 5

    text_upper = text.upper()

    for char in text_upper:
        if not char.isalpha():
            curr_x = 5
            curr_y = curr_y + 550
            continue
        char_string = 'images/' + char + '.png'

        letter_img = Image.open(char_string)
        letter_img = letter_img.resize((512, 512))

        target_x = curr_x
        for source_x in range(letter_img.width):
            target_y = curr_y
            for source_y in range(letter_img.height):
                pixel = letter_img.getpixel((source_x, source_y))
                my_note.putpixel((target_x, target_y), pixel)
                target_y += 1
            target_x += 1
        curr_x = curr_x + 512

    
    my_note.show()




# get_text_from_speech()
# ransom_note('test')



#my_app = QApplication([])

class STTWindow(QWidget):
  def __init__(self):
      super().__init__()
      vbox = QVBoxLayout()
      label1 = QLabel("Press the button and say something to generate a \"ransom note\"\n(You may need to say it a couple of times)")
      label1.setAlignment(Qt.AlignmentFlag.AlignHCenter)
    #   label2 = QLabel("(You may need to say it a couple of times)")
      vbox.addWidget(label1)
    #   vbox.addWidget(label2)
      btn1 = QPushButton("Speak")
      btn1.clicked.connect(self.on_search)
      vbox.addWidget(btn1)
      self.setLayout(vbox)
      self.resize(700, 300)
      self.show()

  def __str__(self):
      return "STTWindow"
  def __repr__(self):
      return "STTWindow"
  @Slot()
  def on_search(self):
    temp = get_text_from_speech()
    ransom_note(temp)

#my_win = STTWindow()
#sys.exit(my_app.exec())

