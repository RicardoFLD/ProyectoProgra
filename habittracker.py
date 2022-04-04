from tkinter import *
from tkcalendar import *
import nonrealizedaction
from tkinter import messagebox, ttk

root = Tk()

root.geometry("1280x720")
root.title("Habit tracker")

Label(root, text="Geneva", font=("MS Reference Sans Serif Normal", "20")).place(x=60, y=30)

#####################################################Journal#################################################################

journal=Button(root, text="Journal", font=("MS Reference Sans Serif Normal", "14"))
journal.place(x=70, y=120)

#####################################################Hábitos#################################################################

habits=["Seleccionar hábito"]

def newHabit():
    txt=Entry(root)
    txt.place(x=70,y=300)
    txt1=txt.get()
    def plusOne():
        habits.append(txt1)
    add=Button(root, text="Añadir", font=("MS Reference Sans Serif Normal", "12"), command=plusOne)#
    add.place(x=70, y=325)

addHabit=Button(root, text="Hábito nuevo", font=("MS Reference Sans Serif Normal", "14"), command=newHabit)
addHabit.place(x=70, y=210)

habit=ttk.Combobox(root, state="reandonly", values=habits)
habit.place(x=375, y=375)

def getSelection():
    selection=habit.get()

def grab_date():
    seleccion.config(text=cal.get_date())

Button(root, text="Selecionar", command=getSelection).place(x=375, y=400)

Label(root, text="Traqueador de hábitos", font=("MS Reference Sans Serif Normal", "14")).place(x=375, y=30)

cal=Calendar(root, selectmode="day", year=2022, month=4, day=4)
cal.place(x=344, y=120)





seleccion=Label(root,text="")





root.mainloop()