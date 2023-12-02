import sqlite3

def obtener_nombre_usuario_desde_BD(email):
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('C:\\Users\\Casa\\Desktop\\AppUsers.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT nombre || " " || apellido FROM usuarios WHERE email = ?', (email,))
            nombre = cursor.fetchone()

            # Retornar solo el nombre si está presente
            return nombre[0] if nombre else None
    except sqlite3.Error as e:
        print(f"Error en la consulta a la base de datos: {e}")
        return None
    
    
def agregar_usuario_a_BD(nombre, email, contrasena, apellido):
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('C:\\Users\\Casa\\Desktop\\AppUsers.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('INSERT INTO usuarios VALUES (NULL, ?, ?, ?, ?)', (nombre, email, contrasena, apellido))
            conexion.commit()
            print("Usuario agregado a la base de datos")
    except sqlite3.Error as e:
        print(f"Error en la consulta a la base de datos: {e}") 
        
def mostrar_todos_los_usuarios():
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('C:\\Users\\Casa\\Desktop\\AppUsers.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('SELECT * FROM usuarios')
            usuarios = cursor.fetchall()
            for usuario in usuarios:
                print(usuario)
    except sqlite3.Error as e:
        print(f"Error en la consulta a la base de datos: {e}")
        
def eliminar_usuario_de_BD(id):
    try:
        # Utilizar with para manejar la conexión y el cursor
        with sqlite3.connect('C:\\Users\\Casa\\Desktop\\AppUsers.db') as conexion:
            cursor = conexion.cursor()
            cursor.execute('DELETE FROM usuarios WHERE id = ?', (id,))
            conexion.commit()
            print("Usuario eliminado de la base de datos")
    except sqlite3.Error as e:
        print(f"Error en la consulta a la base de datos: {e}")                

  

mostrar_todos_los_usuarios()
