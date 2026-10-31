import tkinter as tk
from tkinter import *
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

window=Tk()
window.geometry('800x800')

label=tk.Label(text="Text to speech", fg='purple', bg='beige', font=("Times New Roman", 56))
label.pack()

entry=tk.Entry(bg='beige')
entry.place(x=300,y=300)

def play_audio():
    text=entry.get()
    spanish_text=GoogleTranslator(source="en",target="es").translate(text)
    speech=gTTS(text=spanish_text,lang="es", slow=False)
    speech.save("spanish.mp3")

button=tk.Button(text="Convert", font=("Georgia",30),command=play_audio)
button.pack()

window.mainloop()