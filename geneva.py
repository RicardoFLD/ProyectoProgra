from ast import Lambda
from email import header
from msilib.schema import Control
import pickle
from datetime import date
from tkinter import *
import tkinter
from turtle import bgcolor, width
from tkcalendar import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar, DateEntry
from datetime import date

#from timer import count
#from to_do_list import newTask

def genevaControl():
    control=Tk()

    control.geometry("820x720")
    control.title("Geneva")
    control.resizable(width=False, height=False)

    #HABIT TRACKER

    habits={}

    def new_habit():
        global newhabit
        newhabit=Toplevel(control)
        newhabit.geometry("500x500")
        global entry_habit
        Label(newhabit, text="Ingrese un hábito", font="Arial 10").place(x="145", y="30")
        entry_habit=Entry(newhabit, width=20)
        entry_habit.place(x="145",y="75")
        Label(newhabit, text="Selecciona la fecha de inicio", font="Arial 10").place(x="145", y="128")
        global startdate
        startdate=DateEntry(newhabit, width=15)
        startdate.place(x="145", y="173")
        Label(newhabit, text="Selecciona la fecha final", font="Arial 10").place(x="145", y="226")
        global finaldate
        finaldate=DateEntry(newhabit, width=15)
        finaldate.place(x="145", y="271")
        button_add_habit=Button(newhabit, text="Añadir hábito", width=20, command=add_habit)
        button_add_habit.place(x="145",y="340")

    def add_habit():
        habit=Checkbutton(listbox_habits, text=entry_habit.get())
        listbox_habits.insert(END, habit)
        if habit!= "":
            listbox_habits.delete(0, END)
            data=[]
            data.append(entry_habit.get())
            habits[startdate.get_date()]=data
            habits[finaldate.get_date()]=data
            newhabit.destroy()
        else:
            messagebox.showerror("Alerta","Debes ingresar un hábito")

    def delete_habit():
        try:
            habit_index = listbox_habits.curselection()[0]
            listbox_habits.delete(habit_index)
        except:
            messagebox.showwarning(title="¡Advertencia!", message="Debes seleccionar un hábito.")

    def save_habits():
        habits = listbox_habits.get(0, listbox_habits.size())
        pickle.dump(habits, open("habits.dat", "wb"))
        try:
            tasks = pickle.load(open("tasks.dat", "rb"))
            listbox_habits.delete(0, tkinter.END)
            for task in tasks:
                listbox_habits.insert(tkinter.END, task)
        except:
            messagebox.showwarning(title="¡Alerya!", message="No se ha encontrado el hábito")

    
    Label(control, text="Hábitos", font="Arial 10").place(x="187", y="319")

    frame_habits = tkinter.Frame(control)
    frame_habits.place(x="187", y="346")

    listbox_habits = tkinter.Listbox(frame_habits, height=10, width=35)
    listbox_habits.pack(side=tkinter.LEFT)

    scrollbar_habits = tkinter.Scrollbar(frame_habits)
    scrollbar_habits.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    listbox_habits.config(yscrollcommand=scrollbar_habits.set)
    scrollbar_habits.config(command=listbox_habits.yview)

    button_newhabit=tkinter.Button(control, text="+", font="Arial 12", fg="RoyalBlue2", command=new_habit, borderwidth=0)
    button_newhabit.place(x="450", y="312")

    button_delete_habit = tkinter.Button(control, text="Eliminar", width=10, command=delete_habit)
    button_delete_habit.place(x="330", y="600")

    button_save_habits = tkinter.Button(control, text="Realizado", width=10, command=save_habits)
    button_save_habits.place(x="220", y="600")

    #CALENDAR

    Label(control, text="Calendario", font="Arial 10").place(x="187",y="51")

    cal=Calendar(control, selectmode="day", width=35, height=10)
    cal.config(headersbackground='#b0b0b0', foreground='#000', background='#ededed', headersforeground ='#ededed')
    cal.place(x="187", y="78")

    #TO DO LIST
    
    Label(control, text="Lista de tareas", font="Arial 10").place(x="510", y="51")

    def newTask():
        task = my_entry.get()
        if task != "":
            lb.insert(END, task)
            my_entry.delete(0, "end")
        else:
            messagebox.showwarning("Error", "Escriba en el espacio")

    def deleteTask():
        lb.delete(ANCHOR)

    frame = Frame(control)
    frame.place(x="510", y="78")

    lb = Listbox(
    frame,
    width=19,
    height=14,
    font=("Arial 10"),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
    )
    lb.pack(side=LEFT, fill=BOTH)
    task_list = [
    'Tareas pedientes',
    ]

    for item in task_list:
        lb.insert(END, item)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    #my_entry = Entry(
        # Control,
        #font=("Arial 10")
        #)

    #my_entry.place(x="510", y="526")

    addTask_btn = Button(
        text='Añadir tarea',
        font=('Arial 10'),
        command=newTask
    )
    addTask_btn.place(x="535", y="600")

    delTask_btn = Button(
    text='Eliminar tarea',
    font=('Arial 10'),
    command=deleteTask
    )
    delTask_btn.place(x="648", y="600")

    control.mainloop()




genevaControl()