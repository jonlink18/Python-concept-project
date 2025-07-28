print ("Verificador de Numero primos!")

num =int(input("Coloca un numero para saber si un numero primo:"))

def n_primos(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n% i ==0:
            return False
        
    return True

if n_primos(num):
    print(f"{num} es primo")
else:
    print (f"{num} no es primo")
    
