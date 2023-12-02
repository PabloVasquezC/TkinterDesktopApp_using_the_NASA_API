import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO  
from Usuarios import *
from ConnnBD import *



# Declarar una variable global para almacenar el email
global_email = ""

# Función de inicio de sesión
def login():
    global global_email  # Indicar que estamos utilizando la variable global_email
    email = entry_username.get()
    contrasena = entry_password.get()
    
    login_correcto = False
    for i in usuarios:
        if i.validar_usuario(email, contrasena):
            login_correcto = True
            break

    if login_correcto:
        label_result.config(text="Login correcto", fg="green")
        global_email = email  # Almacenar el email como variable global
        # Destruir la ventana actual después de un breve retraso
        window.after(1500, destroy_login_window)
    else:
        label_result.config(text="Login incorrecto", fg="red")

# Función para destruir la ventana actual y abrir una nueva ventana
def destroy_login_window():
    window.destroy()
    open_main_window()

# Función para abrir la nueva ventana de tamaño completo
def open_main_window():
    # Obtener el nombre de usuario desde la base de datos
    nombre_usuario = obtener_nombre_usuario_desde_BD(global_email)

    # Crear la ventana principal
    main_window = tk.Tk()
    main_window.title(f"PlanetaryApp - Bienvenido(a) {nombre_usuario}")

    # Configurar la nueva ventana para ocupar toda la pantalla
    width, height = main_window.winfo_screenwidth(), main_window.winfo_screenheight()
    main_window.geometry(f"{width}x{height}+0+0")

    # Descargar la imagen desde la URL para el fondo
    url_background = "https://images.unsplash.com/photo-1538370965046-79c0d6907d47?q=80&w=1469&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    response_background = requests.get(url_background)
    image_data_background = response_background.content

    # Abrir la imagen con Pillow y ajustar al tamaño de la ventana principal
    image_background = Image.open(BytesIO(image_data_background))
    image_background = image_background.resize((width, height), Image.ANTIALIAS)

    # Convertir la imagen a un formato compatible con tkinter
    tk_image_background = ImageTk.PhotoImage(image_background)

    # Configurar el fondo de la nueva ventana
    background_label_main = tk.Label(main_window, image=tk_image_background)
    background_label_main.place(x=0, y=0, relwidth=1, relheight=1)

    # Crear un Frame para la barra de navegación lateral
    nav_frame = tk.Frame(main_window, bg="#333333", width=200)
    nav_frame.pack(side="left", fill="y")

    # Nombre de la aplicación
    app_name_label = tk.Label(nav_frame, text="PlanetaryApp", font=("Helvetica", 18), fg="white", bg="#333333", padx=10, pady=10)
    app_name_label.pack()

    # Botones de muestra en la barra lateral
    button1 = tk.Button(nav_frame, text="Botón 1", command=funcion_boton1)
    button1.pack(pady=10)

    button2 = tk.Button(nav_frame, text="Botón 2", command=funcion_boton2)
    button2.pack(pady=10)

    button3 = tk.Button(nav_frame, text="Botón 3", command=funcion_boton3)
    button3.pack(pady=10)

    # Crear un Label de bienvenida para el nombre de usuario
    label_welcome = tk.Label(main_window, text=f"Bienvenido(a), {nombre_usuario}!", font=("Helvetica", 20), fg="white", bg="#000000")
    label_welcome.pack(pady=20)

    # Puedes agregar más contenido a la nueva ventana aquí si es necesario

    # Iniciar el bucle principal de la nueva ventana
    main_window.mainloop()

# Funciones de muestra para los botones
def funcion_boton1():
    print("Botón 1 presionado")

def funcion_boton2():
    print("Botón 2 presionado")

def funcion_boton3():
    print("Botón 3 presionado")


# Resto del código...



# Función para centrar la ventana
def centrar_ventana(window):
    window.update_idletasks()
    ancho_ventana = window.winfo_width()
    alto_ventana = window.winfo_height()
    x_ventana = (window.winfo_screenwidth() // 2) - (ancho_ventana // 2)
    y_ventana = (window.winfo_screenheight() // 2) - (alto_ventana // 2)
    window.geometry('{}x{}+{}+{}'.format(ancho_ventana, alto_ventana, x_ventana, y_ventana))

# Crear la ventana principal
window = tk.Tk()
window.title("Login")

# Descargar la imagen desde la URL para el fondo
url = "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
response = requests.get(url)
image_data = response.content

# Abrir la imagen con Pillow y ajustar al tamaño de la ventana principal
image = Image.open(BytesIO(image_data))
image = image.resize((900, 700), Image.ANTIALIAS)

# Convertir la imagen a un formato compatible con tkinter
tk_image = ImageTk.PhotoImage(image)

# Configurar la imagen de fondo
background_label = tk.Label(window, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un contenedor para el formulario de login
login_frame = tk.Frame(window, padx=20, pady=20)
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Crear un estilo para ttk.Frame con fondo negro semi transparente y bordes redondeados
style = ttk.Style()
style.configure("TFrame", background="#000000", borderwidth=5, relief="flat")
login_frame = ttk.Frame(window, style="TFrame", padding=(20, 20))
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Crear la etiqueta de título en 3D
label_title = ttk.Label(login_frame, text="PlanetaryApp", font=("Helvetica", 24, "bold"), background="#000000", foreground="white")
label_title.grid(row=0, column=0, pady=(0, 20))

# Crear la etiqueta de nombre de usuario y la entrada
label_username = tk.Label(login_frame, text="Username:", bg="#000000", fg="white")
label_username.grid(row=1, column=0, pady=(0, 5))
entry_username = tk.Entry(login_frame)
entry_username.grid(row=2, column=0)

# Crear la etiqueta de contraseña y la entrada
label_password = tk.Label(login_frame, text="Password:", bg="#000000", fg="white")
label_password.grid(row=3, column=0, pady=(10, 5))
entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=4, column=0)

# Crear el botón de inicio de sesión
button_login = tk.Button(login_frame, text="Login", command=login, bg="green", fg="white")
button_login.grid(row=5, column=0, pady=(20, 0))

# Crear la etiqueta de resultado
label_result = tk.Label(login_frame, text="", bg="#000000", fg="white")
label_result.grid(row=6, column=0)

# Configurar el tamaño y centrar la ventana
window.geometry("900x700")
centrar_ventana(window)

# Iniciar el bucle principal
window.mainloop()
