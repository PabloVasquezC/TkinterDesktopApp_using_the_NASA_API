from Usuarios import *

nuevo_usuario = Usuario("peo@gmail.com", "1234")
usuarios.extend([nuevo_usuario])
for usuario in usuarios:
    print(usuario)