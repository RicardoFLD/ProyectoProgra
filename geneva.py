from ast import Lambda
from datetime import date
from tkinter import *
from tkcalendar import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar, DateEntry

def genevaControl():
    control=Tk()

    control.geometry("720x720")
    control.title("Geneva")

    Label(control, text="Geneva", font="Arial 20").place(x="31", y="21")

    habits=[]
    dates={}

    def newHabit():
        newhabit=Toplevel(control)
        newhabit.geometry("500x500")
        Label(newhabit, text="Nombra tu hábito", font="12").place(x="196", y="57")
        global eTxt
        eTxt=StringVar
        txt=Entry(newhabit)
        txt.place(x="159", y="106")
        Label(newhabit, text="Selecciona la fecha de inicio", font="10").place(x="131", y="161")
        global startdate
        startdate=DateEntry(newhabit)
        startdate.place(x="116", y="207")
        Label(newhabit, text="Selecciona la fecha final").place(x="290", y="161")
        global finaldate
        finaldate=DateEntry(newhabit)
        finaldate.place(x="275", y="207")
        Button(newhabit, text="Añadir", font="10", command=savehabit).place(x="195", y="319")
        found=False
        for  habit in habits[::]:
            if eTxt in habits:
                found=True
                break
            else:
                found=False
        if found:
            messagebox.showinfo("","Usuario encontrado")
            newhabit.destroy()
        else:
            messagebox.showinfo("","Usuario incorrecto")
            newhabit.destroy()
    
    done=IntVar()
    done.set(True)
    
    def savehabit():
        habits.append(eTxt)
        data=[startdate.get_date()]
        dates[finaldate.get_date()]=data
        messagebox.showinfo("","¡Hábito creado!")

    for i in habits:
        global nH
        nH=Checkbutton(control, text=habits[::-1], variable=done, value=1)
        nH.pack(pady=20)

    count=[]

    def donehab(doneH):
        if done == True:
            messagebox.showinfo("Hábito realizado", "¡Continúa así!")
            count.append(nH)
        elif done== False:
            messagebox.showwarning("Hábito no relizado","Por favor intenta mantener tu disciplina")

    createHabit=Button(control, text="Añadir hábito", font="10",command=newHabit)
    createHabit.place(x="31", y="78")

    if habits != []:
        doneHabit=Button(control, text="Hecho", font="12", command=donehab(done.get()))
        doneHabit.place(x="180",y="622")

    cal=Calendar(control, selectmode="day")
    cal.place(x="180", y="78")

    control.mainloop()

genevaControl()