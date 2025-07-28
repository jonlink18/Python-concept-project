class Estudiante():
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
    
    def __str__(self):
        return f"{self.nombre},{self.edad},{self.carrera}"
    

def guardar_estudiante(estudiante, archivo = "estudiante.txt"):
    with open (archivo, "a") as f :
        f.write(str(estudiante)+ "\n")

def mostrar_estudiante(archivo = "estudiante.txt"):
    try:
        with open (archivo, "r") as f:
            for linea in f:
                nombre, edad, carrera =linea.strip().split(",")
                print(f"Nombre:{nombre}, Edad:{edad}, Carrera:{carrera}")
    except FileExistsError:
        print("No hay estudiantes Resgistrados aún.")
        

def buscar_estudiante(nombre_buscar, archivo = "estudiante.txt"):
    encontrado = False
    try:
        with open(archivo, "r") as f:
            for linea in f:
                nombre, edad, carrera = linea.strip().split(",")
                if nombre.lower() == nombre_buscar.lower():
                    print(f"Nombre:{nombre}, Edad;{edad}, Carrera:{carrera}")
                    encontrado = True
                    break
        if not encontrado:
            print("Estudiante no encontrado.")
    except FileExistsError:
        print("NO hay estudiantes registrados aún.")

def menu():
    while True:
        print("\n---Sistema de gestion de estudiantes---")
        print("1. Agregar estudiante")
        print("2. Mostrar estudiante")
        print("3. Buscar estudiante")
        print("4. Salir")
        try:
            opc = int(input("Elige qué quieres hacer: "))
        except ValueError:
            print("❌ Ingresa un número válido.")
            continue
        if opc == 1:
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            carrera = input("Carrrera: ")
            
            estudiante = Estudiante(nombre, edad, carrera)

            guardar_estudiante(estudiante)
            print("Estudiante guardado")
        elif opc == 2:
            mostrar_estudiante()
        elif opc ==3:
            nombre_buscar = input("Nombre a buscar:")
            buscar_estudiante(nombre_buscar)
        elif opc == 4:
            print("Saliendo del sistema.")
            break
        else:
          print("Opción no válida.")      

if __name__ == "__main__":
    menu()