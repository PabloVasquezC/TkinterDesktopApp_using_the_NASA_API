# Archivo donde se crea la clase Usuario y se instancias los usuarios, además de la lista de usuarios y las funciones para agregar usuarios a la lista  

class Usuario:
    def __init__(self, email, contrasena):
        self.email = email
        self.contrasena = contrasena

    def __str__(self):
        return f"Usuario: {self.email}"

    def validar_usuario(self, email, contrasena):
        for usuario in usuarios:
            if usuario.email == email and usuario.contrasena == contrasena:
                return True
        return False

# Crear la lista de usuarios antes de la instancia
usuarios = []

# funcion para agregar usuarios a la lista
def agregar_usuarios():
    pablo = Usuario("vascor.pablo@gmail.com", "CATA.7531")
    nicolas = Usuario("nicolas.riquelme40@inacapmail.cl", "NICOLAS.1234")
    ester = Usuario("ester.godoy@inacapmail.cl", "ESTER.1234")

    # Agregar usuarios a la lista
    usuarios.extend([pablo, nicolas, ester])

# Llamar a la función para agregar usuarios cuando se importa el módulo
agregar_usuarios()





    
