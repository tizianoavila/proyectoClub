import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date, timedelta

import database
from database import insertar_socio, obtener_todos_los_socios
from database import obtener_socio_por_credenciales

def iniciar():
    usuario_valido = "a"
    contrasena_valida = "v"

    if entrada_usuario.get() == usuario_valido and entrada_contrasena.get() == contrasena_valida:
        ventanaInicial.withdraw()
        cambiarHome()
    else:
        mostrar_resultado.config(text="Usuario o contraseña incorrecta", fg="red")
        
#   VENTANA INICIAL (LOGIN)

ventanaInicial = tk.Tk()
ventanaInicial.title("Inicio de Sesión")
ventanaInicial.geometry("420x520")
ventanaInicial.config(bg="#dcdcdc")
ventanaInicial.resizable(False, False)

# Título
titulo = tk.Label(
    ventanaInicial,
    text="Bienvenido al Quinto Escalón",
    font=("Arial", 22, "bold"),
    fg="purple",
    bg="#dcdcdc"
)
titulo.pack(pady=30)

# Marco login
seccion1 = tk.Frame(
    ventanaInicial,
    bg="grey",
    bd=5,
    relief="groove",
    width=400,
    height=250
)
seccion1.pack(pady=50)
seccion1.pack_propagate(False)

# Campos
tk.Label(
    seccion1,
    text="Ingresa Usuario",
    font=("Arial", 14, "bold"),
    bg="grey"
).pack()

entrada_usuario = tk.Entry(seccion1, font=("Arial", 14))
entrada_usuario.pack(pady=10)

tk.Label(
    seccion1,
    text="Ingresa Contraseña",
    font=("Arial", 14, "bold"),
    bg="grey"
).pack()

entrada_contrasena = tk.Entry(seccion1, font=("Arial", 14), show="*")
entrada_contrasena.pack(pady=20)

# Botón iniciar sesión
tk.Button(
    seccion1,
    text="Iniciar sesión",
    font=("Arial", 14),
    bg="purple",
    fg="white",
    command=iniciar
).pack(pady=5)

#   FUNCIÓN HOME

def cambiarHome():
    ventanaHome = tk.Toplevel()
    ventanaHome.title("Home")
    ventanaHome.geometry("350x550")
    ventanaHome.config(bg="#dcdcdc")
    ventanaHome.resizable(False, False)

    # Estilo general de cada cuadro
    estilo_cuadro = {
        "bg": "#b3b3b3",
        "bd": 4,
        "relief": "ridge",
        "width": 260,
        "height": 120
    }

    # Función que crea cada "cuadradito"
    def crear_cuadro(parent, texto):
        frame = tk.Frame(parent, **estilo_cuadro)
        frame.pack(pady=20)
        frame.pack_propagate(False)

        tk.Button(
            frame,
            text=texto,
            font=("Fira Code", 16, "bold"),
            bg="#2b2b2b",
            fg="yellow",
            activebackground="#444",
            activeforeground="white",
            relief="flat",
            width=12,
            height=2
        ).pack(expand=True)

        return frame

    # Crear los 3 cuadros
    crear_cuadro(ventanaHome, "Batallas")
    crear_cuadro(ventanaHome, "Tabla")
    crear_cuadro(ventanaHome, "Participantes")

#   LOGIN

mostrar_resultado = tk.Label(ventanaInicial, bg="#dcdcdc")
mostrar_resultado.pack()

ventanaInicial.mainloop()
