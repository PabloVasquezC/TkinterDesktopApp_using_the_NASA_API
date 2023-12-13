# Archivo que gestiona la conexión con la base de datos


# importamos el modulo de sqlite3
import sqlite3



# función para obtener nombre de usuario desde la base de datos
def obtener_nombre_usuario_desde_BD(email):
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('./AppUsers.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT nombre || " " || apellido FROM usuarios WHERE email = ?', (email,))
            nombre = cursor.fetchone()

            # Retornar solo el nombre si está presente
            return nombre[0] if nombre else None
    except sqlite3.Error as e:
        print(f"Error en la consulta a la base de datos: {e}")
        return None

    

# función para agregar usuarios a la base de datos
def agregar_usuario_a_BD(nombre, email, contrasena, apellido):
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('./AppUsers.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?)', (nombre, email, contrasena, apellido))
            conexion.commit()
            print("Usuario agregado a la base de datos")
    except sqlite3.Error as e:
        print(f"Error en la consulta a la base de datos: {e}") 


# función para mostrar todos los usuarios de la base de datos      
def mostrar_todos_los_usuarios():
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('./AppUsers.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM usuarios')
            usuarios = cursor.fetchall()
            for usuario in usuarios:
                print(usuario)
    except sqlite3.Error as e:
        print(f"Error en la consulta a la base de datos: {e}")


# función para eliminar un usuario de la base de datos      
def eliminar_usuario_de_BD(id):
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('./AppUsers.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
            conexion.commit()
            print("Usuario eliminado de la base de datos")
    except sqlite3.Error as e:
        print(f"Error en la consulta a la base de datos: {e}")  
 
        
def validar_usuario_desde_BD(email, contrasena):
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('./AppUsers.db') as conexion:
            conexion.row_factory = sqlite3.Row  # Para acceder a las columnas por nombre
            cursor = conexion.cursor()
            
            # Utilizar parámetros con un diccionario en la consulta SQL
            cursor.execute('SELECT * FROM usuarios WHERE email = :email AND contrasena = :contrasena', {"email": email, "contrasena": contrasena})

            # Obtener el usuario como un diccionario
            usuario_info = cursor.fetchone()

            if usuario_info:
                # Devolver información del usuario
                return dict(usuario_info)
            else:
                return None
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None            
    




