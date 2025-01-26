import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3 
import os

#DESIGN
root = tk.Tk()
root.title("Hear Version")
root.geometry("900x450+200+200")
root.resizable(False,True)
root.configure(background="#827773")
image_icon=PhotoImage(file="icon.png")
root.iconphoto(False,image_icon)

#ENABLE COMMAND BUTTONS
engine=pyttsx3.init()

def speaknow():
    text=text_area.get(1.0, END)
    voice=voice_cmb.get()
    speed=speed_cmb.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (voice=='Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed =="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()

def download():
    text=text_area.get(1.0, END)
    voice=voice_cmb.get()
    speed=speed_cmb.get()
    voices=engine.getProperty('voices')

    def setvoice():
        if (voice=='Male'):
            engine.setProperty('voice',voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if(text):
        if(speed =="Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed=='Normal'):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


#Top Frame
Top_frame=Frame(root,bg="#8C8C8C",width=900,height=100)
Top_frame.place(x=0,y=0)

Label(Top_frame,text="TEXT:",font="Gabriola 60 bold",bg="#8C8C8C",fg="#48586e").place(x=155,y=-25)
Label(Top_frame,text="HEAR",font="Gabriola 60 bold",bg="#8C8C8C",fg="#ddbdbe").place(x=320,y=-25)
Label(Top_frame,text="VERSION+",font="Gabriola 60 bold",bg="#8C8C8C",fg="#ddbdbe").place(x=490,y=-25)
Label(root,text="VOICE",font="Courier 15 bold",bg="#827773",fg="white").place(x=600,y=170)
Label(root,text="SPEED",font="Courier 15 bold",bg="#827773",fg="white").place(x=757,y=170)

#INPUT TEXT
text_area=Text(root,font="Candara 15",bg="#8C8C8C",relief=GROOVE,wrap=WORD)
text_area.place(x=30,y=130,width=500,height=280)

#CHOOSE VOICE
voice_cmb=Combobox(root,values=['Female','Male'],font="Courier 12",state='r',width=12)
voice_cmb.place(x=560,y=200)
voice_cmb.set('Female')

#CHOOSE SPEED
speed_cmb=Combobox(root,values=['Slow','Normal','Fast'],font="Courier 12",state='r',width=12)
speed_cmb.place(x=720,y=200)
speed_cmb.set('Normal')

#BUTTONS
btn_speak=Button(root,text="   SPEAK 🗣️",width=25,height=1,bg="#ddbdbe",font="Courier 14 bold",command=speaknow)
btn_speak.place(x=571,y=280)

btn_save=Button(root,text=" SAVE ⬇️",width=11,height=1,bg="#8e9fb6",font="Courier 14 bold",command=download)
btn_save.place(x=728,y=330)

btn_upload=Button(root,text="UPLOAD➕",width=11,height=1,bg="#8e9fb6",font="Courier 14 bold",command=download,)
btn_upload.place(x=568,y=330)

root.mainloop()