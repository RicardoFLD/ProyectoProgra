from tkinter import *
from tkinter import ttk, messagebox
from geneva import *

def inicio():
    global root
    root=Tk()
    root.geometry("500x500")
    root.title("Iniciar sesión")
    Label(root, text="Bienvenido", font=("20")).place(x="200", y="86")
    #LogIn
    Label(root, text="Inicio de sesión").place(x="202", y="133")
    Label(root, text="Usuario").place(x="200", y="172")
    global vUser
    vUser=StringVar
    logUser=Entry(root, textvariable=vUser)
    logUser.place(x="200", y="192")
    Label(root, text="Contraseña").place(x="200", y="244")
    global vPassword
    vPassword=StringVar
    logPassword=Entry(root, textvariable=vPassword, show="*")
    logPassword.place(x="200", y="264")
    Button(root, text="Iniciar sesión", command=verifyLogIn).place(x="200", y="327")
    Button(root, text="Registrarse", command=registry).place(x="200", y="416")
    root.mainloop()

def registry():
    root_registry=Toplevel(root)
    root_registry.title("Registar Usuario")
    root_registry.geometry("400x400")
    Label(root_registry, text="Integrate a la familia Geneva").place(x="120", y="79")
    global rUser
    global rPassword
    rUser=StringVar()
    rPassword=StringVar()
    Label (root_registry, text="Por favor digite usuario").place(x="120", y="140")
    entradausuarioregistro=Entry(root_registry, textvariable=rUser)
    entradausuarioregistro.place(x="120", y="165")
    Label(root_registry, text="Por favor digite clave").place(x="120", y="212")
    entradaclaveregistro=Entry(root_registry, textvariable=rPassword, show="*")
    entradaclaveregistro.place(x="120", y="237")
    Button(root_registry, text="Registrar", command=saveRegistry).place(x="120", y="323")

user={}
def saveRegistry():
    data=[]
    data.append(rPassword.get())
    user[rUser.get()]=data
    messagebox.showinfo("Alerta","Usuario guardado")
    print(user)

def verifyLogIn():
    found=False
    for  key,value in user.items():
        if vUser.get() in key and vPassword.get() in value:
            found=True
            break
        else:
            found=False
    
    if found:
        messagebox.showinfo("","Usuario encontrado")
        genevaControl()
        root.destroy()
    else:
        messagebox.showinfo("","Usuario incorrecto")

inicio()