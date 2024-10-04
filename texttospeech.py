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

#Top Frame
Top_frame=Frame(root,bg="#8C8C8C",width=900,height=100)
Top_frame.place(x=0,y=0)

Label(Top_frame,text="TEXT:",font="Gabriola 60 bold",bg="#8C8C8C",fg="#48586e").place(x=163,y=-25)
Label(Top_frame,text="HEAR",font="Gabriola 60 bold",bg="#8C8C8C",fg="#ddbdbe").place(x=328,y=-25)
Label(Top_frame,text="VERSION",font="Gabriola 60 bold",bg="#8C8C8C",fg="#ddbdbe").place(x=498,y=-25)
Label(root,text="VOICE",font="Courier 15 bold",bg="#827773",fg="white").place(x=601,y=170)
Label(root,text="SPEED",font="Courier 15 bold",bg="#827773",fg="white").place(x=757,y=170)

#INPUT TEXT
text_area=Text(root,font="Candara 15",bg="#8C8C8C",relief=GROOVE,wrap=WORD)
text_area.place(x=30,y=130,width=500,height=280)

#CHOOSE VOICE
voice_cmb=Combobox(root,values=['Female','Male'],font="Courier 12",state='r',width=12)
voice_cmb.place(x=560,y=210)
voice_cmb.set('Female')

#CHOOSE SPEED
speed_cmb=Combobox(root,values=['Slow','Normal','Fast'],font="Courier 12",state='r',width=12)
speed_cmb.place(x=720,y=210)
speed_cmb.set('Normal')

#BUTTONS
btn_speak=Button(root,text="   SPEAK 🗣️",width=10,height=2,bg="#ddbdbe",font="Courier 14 bold",command=speaknow)
btn_speak.place(x=732,y=280)

btn_save=Button(root,text=" SAVE ⬇️",width=10,height=2,bg="#8e9fb6",font="Courier 14 bold",command=download)
btn_save.place(x=573,y=280)

root.mainloop()