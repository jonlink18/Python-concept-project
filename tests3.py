print ("Calcualar entre dos numeros!")

num1 = input("Coloca el primer numero: ")
num2 = input("Coloca el segundo numero: ")

num1_float = float(num1) 
num2_float = float (num2)

rsum = num1_float + num2_float
rrest = num1_float - num2_float
rmult = num1_float * num2_float
rdiv = num1_float / num2_float
print("Resultados:")

print("------------------------")
print("La suma es: ", rsum)
if rsum % 2 ==0:
    print("la suma es par!")
else:
    print("la suma es impar!")


print("------------------------")
print("La resta es:", rrest)
if rrest % 2 ==0:
    print("la resta es par!")
else:
    print("la resta es impar!")

print("------------------------")
print("La resta es:", rmult)
if rmult % 2 ==0:
    print("la multiplicacion es par!")
else:
    print("la multiplicacion es impar!")



print("------------------------")
print("La division es: ", rdiv)

if rsum % 2 ==0:
    print("la divicion es par!")
else:
    print("la divicion es impar!")

