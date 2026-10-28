import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ventana Básica - Tkinter")
ventana.geometry("400x300")
ventana.configure(bg="#2c3e50")

# Etiqueta centrada
label = tk.Label(ventana, text="¡Mi primera ventana con Tkinter!", 
                 font=("Arial", 14), bg="#2c3e50", fg="white")
label.pack(pady=100)

ventana.mainloop()
