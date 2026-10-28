import tkinter as tk

def click(boton):
    entrada.insert(tk.END, boton)

def borrar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

ventana = tk.Tk()
ventana.title("Calculadora")

entrada = tk.Entry(ventana, font=("Arial", 18), width=15, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

botones = ['7','8','9','/','4','5','6','*','1','2','3','-','0','.','=','+']
f = 1
c = 0
for b in botones:
    cmd = lambda x=b: calcular() if x=='=' else click(x)
    tk.Button(ventana, text=b, width=5, height=2, command=cmd).grid(row=f, column=c, padx=2, pady=2)
    c+=1
    if c>3:
        c=0
        f+=1

tk.Button(ventana, text="C", width=22, command=borrar, bg="#e74c3c", fg="white").grid(row=5, column=0, columnspan=4, pady=5)

ventana.mainloop()
