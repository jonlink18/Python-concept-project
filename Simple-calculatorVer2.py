print("Calculadora")
e1 = float(input("Digita el primer numero: "))
e2 = float(input("Digite el segundo numero: "))

while True:
    print("Opciones:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Divicion")
    print("5. Potencia")
    print("6. Salir")

    try:
        opc = int(input("Elije una opcion: "))
    except ValueError:
        print("Por favor, ingresa un numero valido")
        continue

    if opc ==1:
        print("La suma de los dos numeros es: ")
        print(f"{e1}  +  {e2} = ",e1 + e2)
        break
    elif opc ==2:
        print("La resta de los dos numeros es: ")
        print(f"{e1}  -  {e2} = ",e1 - e2)
        break
    elif opc ==3:
        print("La multiplicacion de los dos numeros es: ")
        print(f"{e1}  x  {e2} = ",e1 * e2)
        break   
    elif opc ==4:
        print("La divicion de los dos numeros es: ")
        print(f"{e1}  /  {e2} = ",e1 / e2)
        break
    elif opc ==5:
        print("La resta de los dos numeros es: ")
        print(f"{e1}  ^  {e2} = ",e1 ** e2)
        break
    elif opc == 6:
        print("Ten un buen dia")
        break
    else:
        print("Opción inválida. Por favor, intenta nuevamente.")