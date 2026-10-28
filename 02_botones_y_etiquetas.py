import tkinter as tk

def cambiar_texto():
    etiqueta.config(text="¡Botón presionado!")
    etiqueta.config(fg="green")

def restaurar():
    etiqueta.config(text="Texto original", fg="black")

ventana = tk.Tk()
ventana.title("Botones y Etiquetas")
ventana.geometry("350x200")

etiqueta = tk.Label(ventana, text="Texto original", font=("Arial", 16))
etiqueta.pack(pady=20)

btn1 = tk.Button(ventana, text="Cambiar Texto", command=cambiar_texto, bg="#3498db", fg="white")
btn1.pack(pady=5)

btn2 = tk.Button(ventana, text="Restaurar", command=restaurar, bg="#e74c3c", fg="white")
btn2.pack(pady=5)

ventana.mainloop()
