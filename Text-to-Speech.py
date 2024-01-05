from tkinter import *
from gtts import gTTS
#from playsound import playsound
import os

tk = Tk()
tk.geometry('640x480')
tk.resizable(0,0)
tk.config(bg = 'mediumslateblue')
tk.title('TextToSpeech Project')

Label(tk, text = 'TEXT TO SPEECH APPLICATION' , font='timesnewroman 31 bold italic',bg='indigo', fg='wheat').pack()
Label(tk, text ='Enter Text:', font ='timesnewroman 20 bold', bg ='lightsteelblue',fg='teal').place(x=20,y=60)

Txt = StringVar()
entry_field = Entry(tk,textvariable =Txt, width ='100')
entry_field.place(x=20 , y=100)

def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Speech.mp3')
    #playsound('Speech.mp3')
    os.system('Speech.mp3')
def Exit():
    tk.destroy()
def Reset():
    Txt.set("")
    
Button(tk, text = "Play from text" , font = 'timesnewroman 15 bold', command = Text_to_speech,bg='lightcyan').place(x=20, y=140)
Button(tk, text = 'Clear Text', font='arial 15 bold', command = Reset,bg='lavenderblush').place(x=20 , y =200)
Button(tk,text = 'Close Application',font = 'arial 15 bold' , command = Exit, bg = 'salmon').place(x=20,y=260)


tk.mainloop()
