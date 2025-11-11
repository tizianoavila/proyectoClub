import tkinter as tk

ventanaInicial = tk.Tk()
ventanaInicial.title ("inicio de sesion")
ventanaInicial.geometry("800x500")


titulo = tk.Label(ventanaInicial, text="Bienvenido al Quinto Escalon", font=("Arial", 22,"bold"), fg ="purple") 
titulo.pack(pady=30)

seccion1= tk.Frame(ventanaInicial, bg="grey", bd= 5, relief= "groove", width=400)
seccion1.pack(pady=50)

etiqueta_usuario = tk.Label(seccion1, text="Ingresa Usuario",font=("Arial", 14,"bold"), fg ="black", background="grey")
etiqueta_usuario.pack()
entrada_usuario = tk.Entry (seccion1, font=("Arial", 14))
entrada_usuario.pack(pady=10)

etiqueta_contrasena = tk.Label(seccion1, text="Ingresa Contraseña",font=("Arial", 14,"bold"), fg ="black", background="grey")
etiqueta_contrasena.pack()
entrada_contrasena = tk.Entry(seccion1, font=("Arial", 14))
entrada_contrasena.pack(pady=20)

def cambiarHome():
    ventanaHome = tk.Tk()
    ventanaHome.title ("Home")
    ventanaHome.geometry("300x500")
    
    #Seccion 1
    seccionHome1= tk.Frame(ventanaHome, bg="grey", bd= 5, relief= "groove", width=400)
    seccionHome1.pack(pady=30)
    etiquetaTexto1 = tk.Label(seccionHome1,text= "Batallas", background="black", font=("Fira Code", 15), fg="yellow")
    etiquetaTexto1.pack(pady=30)
    #Seccion 2
    seccionHome2= tk.Frame(ventanaHome, bg="grey", bd= 5, relief= "groove", width=400)
    seccionHome2.pack(pady=30)
    etiquetaTexto2 = tk.Label(seccionHome2,text= "Tabla", background="black", font=("Fira Code", 15), fg="yellow")
    etiquetaTexto2.pack(pady=30)
    botonIntegrante= tk.Button (seccionHome2,text= "Participantes", background ="black", font= ("Fira Code", 15), fg="blue")
    botonIntegrante.pack (pady=20)
    #Seccion 3
    seccionHome3= tk.Frame(ventanaHome, bg="grey", bd= 5, relief= "groove", width=400)
    seccionHome3.pack(pady=30)
    etiquetaTexto3 = tk.Label(seccionHome3,text= "Participantes", background="black", font=("Fira Code", 15), fg="yellow")
    etiquetaTexto3.pack(pady=30)
    botonIntegrante= tk.Button (seccionHome3,text= "Participantes", background ="black", font= ("Fira Code", 15), fg="blue")
    botonIntegrante.pack (pady=20)

    ventanaHome.mainloop()
    
def iniciar():
    usuario = "a"
    contrasena = "v"
    if usuario == entrada_usuario.get() and contrasena == entrada_contrasena.get():
        ventanaInicial.withdraw()
        cambiarHome()
    else:
        mostrar_resultado.config(text=f'Usuario o contraseña Incorrecta')


boton = tk.Button(ventanaInicial, text="Iniciar sesion", font=("Arial", 14), bg="purple", fg="white", command=iniciar)
boton.pack(pady=20)

mostrar_resultado = tk.Label(ventanaInicial)
mostrar_resultado.pack()

ventanaInicial.mainloop()