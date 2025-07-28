def agragar_usuario (nombre, edad, correo):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{nombre},{edad},{correo}\n")

def leer_usuarios():
    with open ("usuarios.txt", "r") as archivo:
        for linea in archivo:
         nombre, edad, correo =linea.strip().split(",")
         print(f"Nombre:{nombre},Edad: {edad}, Correo: {correo}")

while True:
    print ("\n1.Agregar usuario")
    print("2. Mostar usuario") 
    print("3. Salir")
    opcion = input("Selecciona una opcion:  ")

    if opcion == "1":
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        correo = input("Correo: ")
        agragar_usuario(nombre, edad, correo)
        print ("Usuario guardado")
    elif opcion =="2":
        leer_usuarios()
    elif opcion == "3":
        break
    else:
        print("Opcion no valida.")
    
