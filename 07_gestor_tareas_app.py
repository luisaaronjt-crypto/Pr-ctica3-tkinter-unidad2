import tkinter as tk
from tkinter import ttk

def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea:
        tabla.insert("", tk.END, values=(tarea, "Pendiente"))
        entry_tarea.delete(0, tk.END)

def completar():
    item = tabla.selection()
    if item:
        tabla.item(item, values=(tabla.item(item)['values'][0], "Completada"))

ventana = tk.Tk()
ventana.title("Gestor de Tareas - App Completa")
ventana.geometry("500x400")

frame_top = tk.Frame(ventana)
frame_top.pack(pady=10)

entry_tarea = tk.Entry(frame_top, width=35, font=("Arial", 12))
entry_tarea.pack(side=tk.LEFT, padx=5)

tk.Button(frame_top, text="Agregar", command=agregar_tarea, bg="#3498db", fg="white").pack(side=tk.LEFT)

tabla = ttk.Treeview(ventana, columns=("Tarea", "Estado"), show="headings")
tabla.heading("Tarea", text="Tarea")
tabla.heading("Estado", text="Estado")
tabla.pack(fill="both", expand=True, padx=10, pady=10)

tk.Button(ventana, text="Marcar como Completada", command=completar, bg="#2ecc71").pack(pady=10)

ventana.mainloop()
