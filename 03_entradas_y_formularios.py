import tkinter as tk
from tkinter import messagebox

def registrar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    if nombre and edad:
        messagebox.showinfo("Registro", f"Registrado: {nombre}, {edad} años")
    else:
        messagebox.showwarning("Error", "Llena todos los campos")

ventana = tk.Tk()
ventana.title("Formulario de Registro")
ventana.geometry("400x250")

frame = tk.LabelFrame(ventana, text="Datos Personales", padx=20, pady=10)
frame.pack(padx=20, pady=20, fill="both")

tk.Label(frame, text="Nombre:").grid(row=0, column=0, sticky="w", pady=5)
entry_nombre = tk.Entry(frame, width=30)
entry_nombre.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Edad:").grid(row=1, column=0, sticky="w", pady=5)
entry_edad = tk.Entry(frame, width=30)
entry_edad.grid(row=1, column=1, pady=5)

tk.Button(frame, text="Registrar", command=registrar, bg="#2ecc71").grid(row=2, column=0, columnspan=2, pady=15)

ventana.mainloop()
