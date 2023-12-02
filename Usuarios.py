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



pablo = Usuario("vascor.pablo@gmail.com", "CATA.7531")
nicolas = Usuario("nicolas.riquelme40@inacapmail.cl", "NICOLAS.1234")
ester = Usuario("ester.godoy@inacapmail.cl", "ESTER.1234")

# Crear la lista de usuarios antes de la instancia
usuarios = [pablo, nicolas, ester]


for i in usuarios:
    print(i)

    
