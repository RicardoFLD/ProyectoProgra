import habittracker

from tkinter import *
import tkinter

ventana=Tk()

ventana.wm_title("Athena")

ventana.wm_geometry("1280x720")

titulo= tkinter.Label(ventana, text="Bienvenido a Athena", font="Arial 18")
titulo.pack()

#to-do

tracker=tkinter.Button(ventana, text="Registro de hábitos", font="Arial 14")
tracker.pack()

ventana.mainloop()