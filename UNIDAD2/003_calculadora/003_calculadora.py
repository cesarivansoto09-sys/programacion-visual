
import tkinter as tk


def presionar(valor):
    entry_num1.insert(tk.END, valor)


def calcular():
    try:
        expresion = entry_num1.get()  
        resultado = eval(expresion)  
        label_resultado.config(text=f"= {resultado}")
    except:
        label_resultado.config(text="Error")


def borrar():
    entry_num1.delete(0, tk.END)
    label_resultado.config(text="= ")


ventana = tk.Tk()
ventana.title("Calculadora Feaaa")


tk.Label(ventana, text="Entrada:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, columnspan=3, padx=5, pady=5)

# Fila 2 (1, 2, 3, +)
btn_1 = tk.Button(ventana, text="1", width=5, height=2, command=lambda: presionar("1"))
btn_1.grid(row=2, column=0, padx=5, pady=5)

btn_2 = tk.Button(ventana, text="2", width=5, height=2, command=lambda: presionar("2"))
btn_2.grid(row=2, column=1, padx=5, pady=5)

btn_3 = tk.Button(ventana, text="3", width=5, height=2, command=lambda: presionar("3"))
btn_3.grid(row=2, column=2, padx=5, pady=5)

btn_sumar = tk.Button(ventana, text="+", width=5, height=2, command=lambda: presionar("+"))
btn_sumar.grid(row=2, column=3, padx=5, pady=5)

# Fila 3 (4, 5, 6, -)
btn_4 = tk.Button(ventana, text="4", width=5, height=2, command=lambda: presionar("4"))
btn_4.grid(row=3, column=0, padx=5, pady=5)

btn_5 = tk.Button(ventana, text="5", width=5, height=2, command=lambda: presionar("5"))
btn_5.grid(row=3, column=1, padx=5, pady=5)

btn_6 = tk.Button(ventana, text="6", width=5, height=2, command=lambda: presionar("6"))
btn_6.grid(row=3, column=2, padx=5, pady=5)

btn_restar = tk.Button(ventana, text="-", width=5, height=2, command=lambda: presionar("-"))
btn_restar.grid(row=3, column=3, padx=5, pady=5)

# Fila 4 (7, 8, 9, x)
btn_7 = tk.Button(ventana, text="7", width=5, height=2, command=lambda: presionar("7"))
btn_7.grid(row=4, column=0, padx=5, pady=5)

btn_8 = tk.Button(ventana, text="8", width=5, height=2, command=lambda: presionar("8"))
btn_8.grid(row=4, column=1, padx=5, pady=5)

btn_9 = tk.Button(ventana, text="9", width=5, height=2, command=lambda: presionar("9"))
btn_9.grid(row=4, column=2, padx=5, pady=5)

btn_multiplicar = tk.Button(ventana, text="x", width=5, height=2, command=lambda: presionar("*"))
btn_multiplicar.grid(row=4, column=3, padx=5, pady=5)

# Fila 5 (0, C, =, /)
btn_0 = tk.Button(ventana, text="0", width=5, height=2, command=lambda: presionar("0"))
btn_0.grid(row=5, column=0, padx=5, pady=5)

btn_clear = tk.Button(ventana, text="C", width=5, height=2, command=borrar)
btn_clear.grid(row=5, column=1, padx=5, pady=5)

btn_igual = tk.Button(ventana, text="=", width=5, height=2, command=calcular)
btn_igual.grid(row=5, column=2, padx=5, pady=5)

btn_dividir = tk.Button(ventana, text="/", width=5, height=2, command=lambda: presionar("/"))
btn_dividir.grid(row=5, column=3, padx=5, pady=5)


label_resultado = tk.Label(ventana, text="= ")
label_resultado.grid(row=6, column=0, columnspan=4, padx=5, pady=5)


ventana.mainloop()
