from Login import *
from Usuarios import *

login()

destroy_login_window()

open_main_window()

centrar_ventana(window)

# Crear la ventana principal
window = tk.Tk()
window.title("Login")

# Descargar la imagen desde la URL
url = "https://images.unsplash.com/photo-1444703686981-a3abbc4d4fe3?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
response = requests.get(url)
image_data = response.content

# Abrir la imagen con Pillow
image = Image.open(BytesIO(image_data))
image = image.resize((800, 550), Image.ANTIALIAS)

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

# Crear la etiqueta de nombre de usuario y la entrada
label_username = tk.Label(login_frame, text="Username:", bg="#000000", fg="white")
label_username.grid(row=0, column=0, pady=(0, 5))
entry_username = tk.Entry(login_frame)
entry_username.grid(row=1, column=0)

# Crear la etiqueta de contraseña y la entrada
label_password = tk.Label(login_frame, text="Password:", bg="#000000", fg="white")
label_password.grid(row=2, column=0, pady=(10, 5))
entry_password = tk.Entry(login_frame, show="*")
entry_password.grid(row=3, column=0)

# Crear el botón de inicio de sesión
button_login = tk.Button(login_frame, text="Login", command=login, bg="green", fg="white")
button_login.grid(row=4, column=0, pady=(20, 0))

# Crear la etiqueta de resultado
label_result = tk.Label(login_frame, text="", bg="#000000", fg="white")
label_result.grid(row=5, column=0)

# Configurar el tamaño y centrar la ventana
window.geometry("800x550")
window.eval('tk::PlaceWindow . center')

# Iniciar el bucle principal
window.mainloop()

