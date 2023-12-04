# Modulo del login

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO  
from Usuarios import *
from ConnnBD import *
from ConnWithNasaApi import *
from tkinter import simpledialog



# variables globales 
global_email = ""
registro_window = None

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

# Función para abrir la ventana de registro de usuarios
def open_registro_window():
    global global_email, registro_window  # Indicar que estamos utilizando la variable global_email
    registro_window = tk.Toplevel(window)
    
    registro_window.title("Registro de Usuario")

    # Crear un contenedor para el formulario de registro
    registro_frame = tk.Frame(registro_window, padx=20, pady=20)
    registro_frame.pack()

    # Etiquetas y entradas para los datos del usuario
    tk.Label(registro_frame, text="Nombre:").grid(row=0, column=0, pady=(0, 5))
    entry_nombre = tk.Entry(registro_frame)
    entry_nombre.grid(row=0, column=1)

    tk.Label(registro_frame, text="Apellido:").grid(row=1, column=0, pady=(0, 5))
    entry_apellido = tk.Entry(registro_frame)
    entry_apellido.grid(row=1, column=1)

    tk.Label(registro_frame, text="Email:").grid(row=2, column=0, pady=(0, 5))
    entry_email_registro = tk.Entry(registro_frame)
    entry_email_registro.grid(row=2, column=1)

    tk.Label(registro_frame, text="Contraseña:").grid(row=3, column=0, pady=(0, 5))
    entry_contrasena_registro = tk.Entry(registro_frame, show="*")
    entry_contrasena_registro.grid(row=3, column=1)

    # Botón para registrar al usuario
    btn_registro = tk.Button(registro_frame, text="Registrarse", command=lambda: registrar_usuario(entry_nombre.get(), entry_email_registro.get(), entry_contrasena_registro.get(), entry_apellido.get()))
    btn_registro.grid(row=4, columnspan=2, pady=10)

# Función para registrar un nuevo usuario
def registrar_usuario(nombre, email, contrasena, apellido):
    # Agregar usuario a la BD
    agregar_usuario_a_BD(nombre, email, contrasena, apellido)
    
    nuevo_usuario = Usuario(email, contrasena)
    usuarios.extend([nuevo_usuario])
    label_result_registro.config(text="Registro exitoso", fg="green")
    window.after(1500, destroy_open_registro_window)

# funcion para destrior la ventana de registro una vez que se registra un usuario    
def destroy_open_registro_window():
    registro_window.destroy()

# Función para destruir la ventana actual y abrir una nueva ventana
def destroy_login_window():
    window.destroy()
    open_main_window()

# Función para abrir la ventana principal
def open_main_window():
    # Obtener el nombre de usuario desde la base de datos
    nombre_usuario = obtener_nombre_usuario_desde_BD(global_email)

    # Crear la ventana principal
    main_window = tk.Tk()
    main_window.title(f"PlanetaryApp - Bienvenido(a) {nombre_usuario}")

    # Configurar la nueva ventana para ocupar toda la pantalla
    width, height = main_window.winfo_screenwidth(), main_window.winfo_screenheight()
    main_window.geometry(f"{width}x{height}+0+0")

    # Crear un contenedor principal para organizar elementos
    container_frame = tk.Frame(main_window)
    container_frame.pack(expand=True, fill="both")

    # Descargar la imagen desde la URL para el fondo
    url_background = "https://images.unsplash.com/photo-1538370965046-79c0d6907d47?q=80&w=1469&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    response_background = requests.get(url_background)
    image_data_background = response_background.content

    # Abrir la imagen con Pillow y ajustar al tamaño de la ventana principal
    image_background = Image.open(BytesIO(image_data_background))
    image_background = image_background.resize((width, height))

    # Convertir la imagen a un formato compatible con tkinter
    tk_image_background = ImageTk.PhotoImage(image_background)

    # Configurar el fondo de la nueva ventana
    background_label_main = tk.Label(container_frame, image=tk_image_background)
    background_label_main.place(x=0, y=0, relwidth=1, relheight=1)

    # Crear un Frame para la barra de navegación lateral
    nav_frame = tk.Frame(container_frame, bg="#333333", width=500)
    nav_frame.pack(side="right", fill="y")

    # Nombre de la aplicación
    app_name_label = tk.Label(nav_frame, text="Menu", font=("Helvetica", 18), fg="white", bg="#333333", padx=100, pady=10)
    app_name_label.pack()

    # Botones de muestra en la barra lateral
    button1 = tk.Button(nav_frame, text="Ver la foto del día", command=ver_foto_del_dia)
    button1.pack(pady=10)

    button2 = tk.Button(nav_frame, text="Ver la foto de un dia X", command=solicitar_fecha)
    button2.pack(pady=10)


    # Crear un Label de bienvenida para el nombre de usuario
    global label_welcome
    label_welcome = tk.Label(container_frame, text=f"""Bienvenido(a) a PlaneryApp {nombre_usuario}!
                                
    PlaneryApp se conecta a la API de la NASA 
    permitiendo así renderizar datos en pantalla.

    La aplicación también permite llevar un registro
    de los usuarios y sus preferencias en una base de datos.

    Al costado derecho encontrarás una serie de funcionalidades
    de las cuales te provee nuestra aplicación

    con PlanaryApp explorar el universo está al alcance de un click!""", font=("Helvetica", 20), fg="white", bg="#000000")
    label_welcome.pack(pady=20)

    # Crear un Label para la foto del día
    global label_foto_del_dia
    label_foto_del_dia = tk.Label(container_frame)
    label_foto_del_dia.pack(pady=10)

    # Crear un Label para la descripción
    global label_descripcion
    label_descripcion = tk.Label(container_frame, text="", font=("Helvetica", 12), fg="white", bg="#000000", wraplength=1000, justify="left")
    label_descripcion.pack(pady=10)

    # Puedes agregar más contenido a la nueva ventana aquí si es necesario

    # Iniciar el bucle principal de la nueva ventana
    main_window.mainloop()







# funcion para ver la foto del dia
def ver_foto_del_dia():
    # Obtener los datos de la foto del día desde la API de la NASA
    api_key = "HLFsRfhi3gr2qxHdowAo6rjIr3xjUHtCdtcaDCk6"  # Coloca aquí tu clave de API
    data = obtener_datos_foto_del_dia(api_key)

    # Verificar si se obtuvieron los datos correctamente
    if data:
        # Obtener el título, la URL de la imagen y la descripción
        titulo = data['title']
        url_imagen = data['url']
        descripcion = data.get('explanation', 'No hay descripción disponible.')

        try:
            # Obtener la imagen desde la URL
            response_imagen = requests.get(url_imagen)
            response_imagen.raise_for_status()  # Verificar si la descarga fue exitosa
            image_data = response_imagen.content

            # Abrir la imagen con Pillow
            imagen = Image.open(BytesIO(image_data))

            # Ajustar la imagen al tamaño deseado (ancho, alto)
            imagen = imagen.resize((400, 400))

            # Convertir la imagen a un formato compatible con tkinter
            tk_imagen = ImageTk.PhotoImage(imagen)

            # Actualizar las etiquetas con los nuevos datos
            label_welcome.config(text=f"La foto del día es: {titulo}")
            label_foto_del_dia.config(image=tk_imagen)
            label_foto_del_dia.image = tk_imagen  # Evita que el recolector de basura elimine la imagen
            label_descripcion.config(text=descripcion)
        except requests.exceptions.RequestException as e:
            print(f"Error al descargar la imagen: {e}")
            label_result.config(text="Error al descargar la imagen", fg="red")
    else:
        print("Error al obtener los datos de la foto del día")


# funcion para solicitar una fecha y ver la foto del dia de esa fecha
def solicitar_fecha():
    # Crear una nueva ventana de diálogo para la entrada de fecha
    fecha = tk.simpledialog.askstring("Ingresar fecha", "Ingrese la fecha (YYYY-MM-DD):")

    # Verificar si se ingresó una fecha
    if fecha:
        # Llamar a la función con la fecha ingresada
        ver_foto_segun_fecha(fecha)

def ver_foto_segun_fecha(fecha):
    # Obtener los datos de la foto del día desde la API de la NASA
    api_key = "HLFsRfhi3gr2qxHdowAo6rjIr3xjUHtCdtcaDCk6"  # Coloca aquí tu clave de API
    data = obtener_foto_del_dia_segun_fecha(api_key, fecha)

    # Verificar si se obtuvieron los datos correctamente
    if data:
        # Obtener el título, la URL de la imagen y la descripción
        titulo = data['title']
        url_imagen = data['url']
        descripcion = data.get('explanation', 'No hay descripción disponible.')

        # Obtener la imagen desde la URL
        response_imagen = requests.get(url_imagen)
        image_data = response_imagen.content

        # Abrir la imagen con Pillow
        imagen = Image.open(BytesIO(image_data))

        # Ajustar la imagen al tamaño deseado (ancho, alto)
        imagen = imagen.resize((400, 400))

        # Convertir la imagen a un formato compatible con tkinter
        tk_imagen = ImageTk.PhotoImage(imagen)

        # Actualizar las etiquetas con los nuevos datos
        label_welcome.config(text=f"La foto del día ({fecha}): {titulo}")
        label_foto_del_dia.config(image=tk_imagen)
        label_foto_del_dia.image = tk_imagen  # Evita que el recolector de basura elimine la imagen
        label_descripcion.config(text=descripcion)

    else:
        print("Error al obtener los datos de la foto del día")








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
url = "https://images.unsplash.com/photo-1606125784258-570fc63c22c1?q=80&w=1522&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
response = requests.get(url)
image_data = response.content

# Abrir la imagen con Pillow y ajustar al tamaño de la ventana principal
image = Image.open(BytesIO(image_data))
image = image.resize((800, 500))

# Convertir la imagen a un formato compatible con tkinter
tk_image = ImageTk.PhotoImage(image)

# Configurar la imagen de fondo
background_label = tk.Label(window, image=tk_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Crear un contenedor para el formulario de login
login_frame = tk.Frame(window, padx=20, pady=10)
login_frame.place(relx=0.2, rely=0.5, anchor="center")

# Crear un estilo para ttk.Frame con fondo negro semi transparente y bordes redondeados
style = ttk.Style()
style.configure("TFrame", background="#000000", borderwidth=5, relief="flat")
login_frame = ttk.Frame(window, style="TFrame", padding=(20, 20))
login_frame.place(relx=0.5, rely=0.5, anchor="center")

# Crear la etiqueta de título en 3D
label_title = ttk.Label(login_frame, text="PlanetaryApp", font=("Helvetica", 24, "bold"), background="#000000", foreground="white")
label_title.grid(row=0, column=0, pady=(0, 20))

# Crear la etiqueta de nombre de usuario y la entrada
label_username = tk.Label(login_frame, text="Email:", bg="#000000", fg="white")
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

# Crear el botón para abrir la ventana de registro de usuarios
button_registro = tk.Button(login_frame, text="Crear Usuario", command=open_registro_window, bg="blue", fg="white")
button_registro.grid(row=7, column=0, pady=(10, 0))

# Crear la etiqueta de resultado
label_result = tk.Label(login_frame, text="", bg="#000000", fg="white")
label_result.grid(row=6, column=0)

label_result_registro = tk.Label(login_frame, text="", bg="#000000", fg="white")
label_result_registro.grid(row=8, column=0)

# Configurar el tamaño y centrar la ventana
window.geometry("800x500")
centrar_ventana(window)

# Iniciar el bucle principal
window.mainloop()
