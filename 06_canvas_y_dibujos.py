import tkinter as tk

def dibujar(event):
    x, y = event.x, event.y
    canvas.create_oval(x-3, y-3, x+3, y+3, fill="blue", outline="")

ventana = tk.Tk()
ventana.title("Canvas y Dibujo")

canvas = tk.Canvas(ventana, width=500, height=400, bg="white")
canvas.pack()

# Dibujos predefinidos
canvas.create_rectangle(50, 50, 150, 100, fill="red")
canvas.create_text(300, 50, text="Dibuja con el mouse", font=("Arial", 12))

canvas.bind("<B1-Motion>", dibujar) # Dibuja arrastrando click izquierdo

tk.Button(ventana, text="Limpiar", command=lambda: canvas.delete("all")).pack(pady=5)

ventana.mainloop()
