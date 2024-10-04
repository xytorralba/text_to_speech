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

root.mainloop()