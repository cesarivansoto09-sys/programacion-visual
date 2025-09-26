import tkinter as tk
from tkinter import messagebox

#funcion que se llama cuando se preciona un boton 
def manejar_boton(numero_dispositivo):
    respuesta = messagebox.askyesno("confirmar",
                                      f"quieres activar el dispositivo{numero_dispositivo}.")
    if respuesta:
        #si el usuario confirma muestra otro cuadro notificando la accion
        messagebox.showinfo("accion realizada"
                            f"dispositivo{numero_dispositivo} activado correctamente"
                     )
    else: 
        #si el usuario cancela muestra una notificacion de cancelacion(opcion)
        messagebox.showinfo("accion cancelada",
                            f"no se activo el disositivo{numero_dispositivo}.")
#creacion de la ventana principal
ventana= tk.Tk()
ventana.title("control electronico(simulacion)")
ventana.geometry("350x250")

#creacion de botones
boton1 = tk.Button(ventana, text="activar dispositivo 1",
                    command=lambda: manejar_boton(1))
boton1.pack(pady=10)

boton2 = tk.Button(ventana, text="activar dispositivo 2",
                    command=lambda: manejar_boton(2))
boton2.pack(pady=10)


boton3 = tk.Button(ventana, text="activar dispositivo 3",
                    command=lambda: manejar_boton(3))
boton3.pack(pady=10)

boton4 = tk.Button(ventana, text="activar dispositivo 4",
                    command=lambda: manejar_boton(4))
boton4.pack(pady=10)

ventana.mainloop()    


