import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")
ventana.geometry("300x400")

# Variable para mostrar los números y operaciones
entrada_texto = tk.StringVar()

# Campo de entrada
entrada = tk.Entry(ventana, textvariable=entrada_texto, font=("Arial", 20), bd=10, relief=tk.RIDGE, justify="right")
entrada.pack(fill="both", ipadx=8, ipady=20, padx=10, pady=10)

# Función para agregar texto al campo de entrada
def agregar(valor):
    entrada_texto.set(entrada_texto.get() + valor)

# Función para borrar todo
def borrar():
    entrada_texto.set("")

# Función para calcular el resultado
def calcular():
    try:
        resultado = eval(entrada_texto.get())
        entrada_texto.set(str(resultado))
    except:
        entrada_texto.set("Error")

# Crear botones
botones = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for fila in botones:
    marco = tk.Frame(ventana)
    marco.pack(expand=True, fill="both")
    for boton in fila:
        accion = lambda x=boton: calcular() if x == "=" else agregar(x)
        tk.Button(marco, text=boton, font=("Arial", 18), command=accion).pack(side="left", expand=True, fill="both")

# Botón para borrar
tk.Button(ventana, text="C", font=("Arial", 18), bg="red", fg="white", command=borrar).pack(fill="both", padx=10, pady=5)

# Iniciar ventana
ventana.mainloop()
