#Clase base:Empleado

class Empleado():
    def __init__(self, nombre,salario):
        self.nombre =nombre
        self.salario=salario

    def mostrar_info(self):
        print(f"Nombre:{self.nombre}, Salario: ${self.salario}") 

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def mostrar_info(self):
        print(f"Gerente:{self.nombre}, Salario: ${self.salario}, Departamento:{self.departamento}")


class Tecnico(Empleado):
    def __init__(self, nombre, salario, especialidad):
        super().__init__(nombre, salario)
        self.especialidad = especialidad

    def mostrar_info(self):
        print(f"Tecnico:{self.nombre}, Salario: ${self.salario}, :{self.especialidad}")


empleados = [
    Empleado("Ana",1000),
    Gerente("Luis",2000,"Ventas"),
    Tecnico("Marta", 1500,"Redes"),
]

for e in empleados:
    e.mostrar_info()
