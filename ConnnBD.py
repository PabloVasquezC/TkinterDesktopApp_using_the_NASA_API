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
    
    
print(obtener_nombre_usuario_desde_BD("vascor.pablo@gmail.com"))    

