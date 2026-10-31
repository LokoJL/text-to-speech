import tkinter as tk
from tkinter import *
from gtts import gTTS
import os

window=Tk()
window.geometry('800x800')

label=tk.Label(text="Text to speech", fg='purple', bg='beige', font=("Times New Roman", 56))
label.pack()

entry=tk.Entry(bg='beige')
entry.place(x=300,y=300)

def play_audio():
    language="es"
    speech=gTTS(text=entry.get(),lang=language,slow=False)
    speech.save("convert.wav")

button=tk.Button(text="Convert", font=("Georgia",30),command=play_audio)
button.pack()

window.mainloop()



