import tkinter as tk
from tkinter import messagebox

def agregar():
    if entry.get():
        lista.insert(tk.END, entry.get())
        entry.delete(0, tk.END)

def eliminar():
    try:
        lista.delete(lista.curselection())
    except:
        messagebox.showwarning("Aviso", "Selecciona un elemento")

ventana = tk.Tk()
ventana.title("Lista y Menú")
ventana.geometry("400x350")

# Menú superior
menubar = tk.Menu(ventana)
ventana.config(menu=menubar)
menubar.add_command(label="Acerca de", command=lambda: messagebox.showinfo("Info", "Práctica Tkinter Unidad 2"))

entry = tk.Entry(ventana, width=30)
entry.pack(pady=10)

tk.Button(ventana, text="Agregar", command=agregar).pack()
tk.Button(ventana, text="Eliminar Seleccionado", command=eliminar, bg="#f39c12").pack(pady=5)

lista = tk.Listbox(ventana, width=40, height=10)
lista.pack(pady=10)

ventana.mainloop()
