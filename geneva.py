from email import header, message
import pickle
from datetime import date
from threading import Timer
from tkinter import *
import tkinter
from turtle import bgcolor, width
from tkcalendar import *
from tkinter.ttk import*
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from datetime import date
from Libro import libro
from time import strftime
import datetime as dt

def genevaControl():
    control=Tk()

    control.geometry("820x720")
    control.title("Geneva")
    control.resizable(width=False, height=False)

    #CLOCK
    def time():
        string = strftime('%H:%M:%S %p')
        clock.config(text = string)
        clock.after(1000, time)

    clock = Label(control, font = ("Arial", 13))
    clock.place(x="31", y="78")
    time()

    #JOURNAL
    Button(control, text="Notas", width=13, command=libro).place(x="31", y="186")

    #HABIT TRACKER

    habits={}

    date = dt.datetime.now()

    datelabel = Label(control, text=f"{date:%x}")
    datelabel.place(x="31", y="110")

    def done():
        for i,j in habits:
            if j == datelabel:
                habits.pop(i)

    def add_habits():
        habits = entry_habits.get()
        if habits != "":
            listbox_habits.insert(tkinter.END, habits)
            entry_habits.delete(0, tkinter.END)
            habits[entry_habits.get()]=finaldate
        else:
            messagebox.showwarning(title="¡Alerta!", message="Debes introducir un hábito")

    def delete_habits():
        try:
            habits_index = listbox_habits.curselection()[0]
            listbox_habits.delete(habits_index)
        except:
            messagebox.showwarning(title="¡Alerta!", message="Debes seleccionar un hábito")

    def load_habits():
        try:
            habits = pickle.load(open("habits.dat", "rb"))
            listbox_habits.delete(0, tkinter.END)
            for habits in habits:
                listbox_habits.insert(tkinter.END, habits)
        except:
            messagebox.showwarning(title="¡Alerta!", message="No se pudo encontrar el hábito")

    def save_habits():
        habits = listbox_habits.get(0, listbox_habits.size())
        pickle.dump(habits, open("habits.dat", "wb"))


    frame_habits = tkinter.Frame(control)
    frame_habits.place(x="187", y="346")

    listbox_habits = tkinter.Listbox(frame_habits, height=10, width=35)
    listbox_habits.pack(side=tkinter.LEFT)

    scrollbar_habits = tkinter.Scrollbar(frame_habits)
    scrollbar_habits.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    listbox_habits.config(yscrollcommand=scrollbar_habits.set)
    scrollbar_habits.config(command=listbox_habits.yview)

    Label(control, text="Añadir un hábito", font="Arial 10").place(x="31", y="241")

    entry_habits = tkinter.Entry(control, width=13)
    entry_habits.place(x="31", y="270")

    Label(control, text="Selecciona la \nfecha final", font="Arial 10").place(x="31", y="343")

    finaldate=DateEntry(control, width=11)
    finaldate.place(x="31", y="385")

    button_add_habits = tkinter.Button(control, text="Crear hábito", width=13, command=add_habits)
    button_add_habits.place(x="31", y="469")

    button_delete_habits = tkinter.Button(control, text="Eliminar", width=10, command=delete_habits)
    button_delete_habits.place(x="330", y="600")

    button_load_habits = tkinter.Button(control, text="Guardar", width=13, command=load_habits)
    button_load_habits.place(x="31", y="515")

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

    frame = Frame(control, width=19, height=14)
    frame.place(x="510", y="78")

    lb = Listbox(
    frame,
    width=30,
    height=24,
    font=("Arial 10"),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
    )
    lb.pack(side=LEFT, fill=BOTH)
    task_list = []

    for item in task_list:
        lb.insert(END, item)

    sb = Scrollbar(frame)
    sb.pack(side=RIGHT, fill=BOTH)

    lb.config(yscrollcommand=sb.set)
    sb.config(command=lb.yview)

    my_entry=Entry(control,font="Arial 10", width=30)
    my_entry.place(x="510", y="526")

    addTask_btn = Button(
        text='Añadir tarea', width=13,
        command=newTask
    )
    addTask_btn.place(x="525", y="600")

    delTask_btn = Button(
    text='Eliminar tarea',width=13,
    command=deleteTask
    )
    delTask_btn.place(x="638", y="600")



    control.mainloop()




genevaControl()