class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Clase Estudiante hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llama al constructor de Persona
        self.carrera = carrera
    
    def mostrar_info(self):
        print(f"Soy {self.nombre}, estudio {self.carrera} y tengo {self.edad} años.")


### ✅ 5. Uso de las clases:


persona1 = Persona("Carlos", 45)
persona1.saludar()

estudiante1 = Estudiante("Ana", 20, "Ingeniería")
estudiante1.saludar()
estudiante1.mostrar_info()