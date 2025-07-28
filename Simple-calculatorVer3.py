def sumar():
    while True:
        try:
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            result= n1+n2
            print (f"la suma de {n1} + {n2} = {result}")  
            break
        except ValueError:
            print("Por favor, ingresa un numero valido")

def resta():
    while True:
        try:
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            result= n1-n2
            print (f"la resta de {n1} - {n2} = {result}")  
            break
        except ValueError:
            print("Por favor, ingresa un numero valido")

def multi():
    while True:
        try:
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            result= n1*n2
            print (f"la multiplicacion de {n1} * {n2} = {result}")  
            break
        except ValueError:
            print("Por favor, ingresa un numero valido")

def div():
    while True:
        try:
            n1 = int(input("Ingresa el primer numero: "))
            n2 = int(input("Ingresa el segundo numero: "))
            result= n1/n2
            print (f"la division de {n1} / {n2} = {result}")  
            break
        except ValueError:
            print("Por favor, ingresa un numero valido.")
        except ZeroDivisionError:
            print ("No se puede dividir entre cero.")


print("Calculadora")

while True:
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. salir")

    try:
        opc = int(input("Elige que quieres hacer: "))
    except ValueError:
        print("Por favor, ingresa un numero valido")
        continue

    if opc == 1:
        sumar()
        break
    elif opc == 2:
        resta()
        break
    elif opc == 3:
        multi()
        break
    elif opc == 4:
        div()
        break
    elif opc == 5:
        print("Ten un buen dia")
        break
    else:
         print("Opción inválida. Por favor, intenta nuevamente.")



