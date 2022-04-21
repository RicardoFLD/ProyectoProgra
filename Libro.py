from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

def copiar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())

def pegar():
    editor.insert(INSERT, editor.clipboard_get())

def cortar():
    editor.clipboard_clear()
    editor.clipboard_append(editor.selection_get())
    editor.delete("sel.first", "sel.last")

def deshacer():
    editor.edit_undo()

def rehacer():
    editor.edit_redo()

def nuevo():
    editor.delete(1.0,END)

def abrir():
    documento = askopenfile(filetypes=[("Archivo de texto","*.txt")])
    if documento != None:
        editor.insert(1.0, documento.read())

def guardar():
    documento = asksaveasfile(filetypes=[("Archivo de texto","*.txt")])
    print(documento.write(editor.get(1.0, END)))

def acerca():
    messagebox.showinfo(
        "Bloc de geneva"
    )
    


if __name__ == "__main__":
    ventana = Tk()
    menubar = Menu(ventana)
    archivo = Menu(menubar, tearoff=0)
    archivo.add_command(label="Nuevo", command=nuevo)
    archivo.add_command(label="Abrir", command=abrir)
    archivo.add_command(label="Guardar", command=guardar)
    archivo.add_command(label="Salir", command=ventana.quit)
    menubar.add_cascade(label="Archivo", menu=archivo)



    editar = Menu(menubar, tearoff=0)
    editar.add_command(label="Deshacer", command=deshacer)
    editar.add_command(label="Rehacer", command=rehacer)
    editar.add_separator()
    editar.add_command(label="Copiar", command=copiar)
    editar.add_command(label="Pegar", command=pegar)
    editar.add_command(label="Cortar", command=cortar)
    menubar.add_cascade(label="Edición", menu=editar)


    ayuda = Menu(menubar, tearoff=0)
    ayuda.add_command(label="Informacion", command=acerca)
    
    menubar.add_cascade(label="Ayuda", menu=ayuda)


    editor = Text(ventana, undo="true")
    editor.pack(side=TOP, fill=BOTH, expand=1)


    ventana.title("Bloc de notas")
    ventana.geometry("700x450")
    ventana.config(menu=menubar)
    
    
ventana.mainloop()