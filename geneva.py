from email import header
from msilib.schema import Control
import pickle
from datetime import date
from threading import Timer
from tkinter import *
import tkinter
from turtle import bgcolor, width
from tkcalendar import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar, DateEntry
from datetime import date
from Libro import libro
import time
import threading

def genevaControl():
    control=Tk()

    control.geometry("820x720")
    control.title("Geneva")
    control.resizable(width=False, height=False)

    #HABIT TRACKER

    habits={}

    def add_habit():
        habit=entry_habit.get()
        if habit!= "":
            listbox_habits.insert(END, habit)
            listbox_habits.delete(0, END)
            data=[]
            data.append(entry_habit.get())
            habits[startdate.get_date()]=data
            habits[finaldate.get_date()]=data
        else:
            messagebox.showerror("Alerta","Debes ingresar un hábito")

    Label(control, text="Añadir un hábito", font="Arial 10").place(x="31", y="241")
    entry_habit=Entry(control, width=13)
    entry_habit.place(x="31",y="270")
    Label(control, text="Selecciona la \nfecha de inicio", font="Arial 10").place(x="31", y="309")

    startdate=DateEntry(control, width=11)
    startdate.place(x="31", y="353")
    Label(control, text="Selecciona la \nfecha final", font="Arial 10").place(x="31", y="389")

    finaldate=DateEntry(control, width=11)
    finaldate.place(x="31", y="433")
    button_add_habit=Button(control, text="Añadir hábito", width=13, command=add_habit)
    button_add_habit.place(x="31",y="469")


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
            tasks = pickle.load(open("habits.dat", "rb"))
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

    button_delete_habit = tkinter.Button(control, text="Eliminar", font="Arial 10", width=10, command=delete_habit)
    button_delete_habit.place(x="330", y="600")

    button_save_habits = tkinter.Button(control, text="Realizado", font="Arial 10", width=10, command=save_habits)
    button_save_habits.place(x="220", y="600")

    #CALENDAR

    Label(control, text="Calendario", font="Arial 10").place(x="187",y="51")

    cal=Calendar(control, selectmode="day", width=35, height=10)
    cal.config(headersbackground='#b0b0b0', foreground='#000', background='#ededed', headersforeground ='#ededed')
    cal.place(x="187", y="78")

    #POMODORO TIMER

    class pomodoroTimer:
        def __init__(self):
            self.root=Tk()
            self.root.geometry("600x300")
            self.root.title("Temporizador de Pomodoro")
        
            self.s=ttk.Style()
            self.s.configure("TNotebook.tab", font=("Arial", 16))
            self.s.configure("TButton.tab", font=("Arial", 16))
        
            self.tabs=ttk.Notebook(self.root)
            self.tabs.pack(fill="both", pady=10, expand=True)
        
            self.tab1=ttk.Frame(self.tabs, width=600, height=100)
            self.tab2=ttk.Frame(self.tabs, width=600, height=100)
            self.tab3=ttk.Frame(self.tabs, width=600, height=100)
        
            self.pomodoro_timer_label=ttk.Label(self.tab1, text="25:00", font=("Arial", 43))
            self.pomodoro_timer_label.pack(pady=20)
        
            self.short_break_timer_label=ttk.Label(self.tab2, text="05:00", font=("Arial", 43))
            self.short_break_timer_label.pack(pady=20)
        
            self.long_break_timer_label=ttk.Label(self.tab3, text="15:00", font=("Arial", 43))
            self.long_break_timer_label.pack(pady=20)
        
            self.tabs.add(self.tab1, text="Pomodoro")
            self.tabs.add(self.tab2, text="Receso corto")
            self.tabs.add(self.tab3, text="Receso largo")
        
            self.grid_layout=ttk.Frame(self.root)
            self.grid_layout.pack(pady=18)
        
            self.start_button=ttk.Button(self.grid_layout, text="Iniciar", command=self.start_timer_thread())
            self.start_button.grid(row=0, column=0)
        
            self.skip_button=ttk.Button(self.grid_layout, text="Saltar", command=self.skip_clock())
            self.skip_button.grid(row=0, column=2)
        
            self.reset_button=ttk.Button(self.grid_layout, text="Reiniciar", command=self.reset_clock())
            self.reset_button.grid(row=0, column=3)
        
            self.pomodoro_counter_label=ttk.Label(self.grid_layout, text="Pomodoros: 0", font=("Arial", 16))
            self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)
        
            self.pomodoros=0
            self.skipped=False
            self.stopped=False
            self.running=False
        
            self.root.mainloop()
        
        def start_timer_thread(self):
            if not self.running:
                t=threading.thread(target=self.start_timer)
                t.start()
                self.running=True
            
        def start_timer(self):
            self.stopped=False
            self.skipped=False
            timer_id=self.tabs.index(self.tabs.select())+1
            
            if timer_id==1:
                full_seconds=60*25
                while full_seconds>0 and not self.stopped:
                    minutes, seconds=divmod(full_seconds,60)
                    self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                    self.root.update()
                    time.sleep(1)
                    full_seconds-=1
                if not self.stopped or self.skipped:
                    self.pomodoros+=1
                    self.pomodoro_counter_label.config(text=f"Pomodoros:{self.pomodoros}")
                    if self.pomodoros % 4==0:
                        self.tabs.select(2)
                        self.start_timer()
                    else:
                        self.tabs.select(1)
                        self.start_timer()
            elif timer_id ==2:
                full_seconds=60*5
                while full_seconds>0 and not self.stopped:
                    minutes, seconds=divmod(full_seconds,60)
                    self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                    self.root.update()
                    time.sleep(1)
                    full_seconds-=1
                if not self.stopped or self.skipped:
                    self.tabs.select(0)
                    self.start_timer()
            elif timer_id==3:
                full_seconds=60*15
                while full_seconds>0 and not self.stopped:
                    minutes, seconds=divmod(full_seconds,60)
                    self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                    self.root.update()
                    time.sleep(1)
                    full_seconds-=1
                if not self.stopped or self.skipped:
                    self.tabs.select(0)
                    self.start_timer()
                    
        def reset_clock(self):
            self.stopped=True
            self.skipped=False
            self.pomodoros=0
            self.pomodoro_timer_label.config(text="25:00")
            self.short_break_timer_label.config(text="05:00")
            self.long_break_timer_label.config(text="15:00")
            self.pomodoro_counter_label.config(text="Pomodoros: 0")
            self.running=False
            
        def skip_clock(self):
            current_tab=self.tabs.index(self.tabs.select())
            if current_tab==0:
                self.pomodoro_timer_label.config(text="25:00")
            elif current_tab==1:
                self.short_break_timer_label.config(text="05:00")
            elif current_tab==2:
                self.long_break_timer_label.config(text="15:00")
                self.stopped=True
                self.skipped=True
            
    Button(control, text="Pomodoro", font="Arial 10", width=10, command=pomodoroTimer()).place(x="31", y="123")

    #Button(control, text="Temporizador", font= "Arial 10", width=11, command=count()).place(x="31", y="142")

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
        text='Añadir tarea',
        font="Arial 10", width=10,
        command=newTask
    )
    addTask_btn.place(x="525", y="600")

    delTask_btn = Button(
    text='Eliminar tarea',
    font="Arial 10",width=10,
    command=deleteTask
    )
    delTask_btn.place(x="638", y="600")

    #JOURNAL

    Button(control, text="Notas", font="Arial 10", width=11, command=libro()).place(x="31", y="78")

    control.mainloop()




genevaControl()