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
    


"""
otro ejemplo a detalle!
 ¡Perfecto! Vamos a agregar un `print()` dentro del bucle para ver **qué valores prueba la función y cómo decide si un número es primo**.

---

### ✅ Versión explicada de `es_primo(n)` con `print()` paso a paso:

```python
def es_primo(n):
    if n < 2:
        print(f"{n} no es primo (menor que 2)")
        return False
    
    print(f"Probando si {n} es primo...")
    for i in range(2, int(n**0.5) + 1):
        print(f"  ¿{n} divisible por {i}? → {n % i == 0}")
        if n % i == 0:
            print(f"  Sí, {n} es divisible por {i}, entonces NO es primo.\n")
            return False

    print(f"  No se encontró ningún divisor. {n} ES primo.\n")
    return True
```

---

### 🧪 Prueba con un número primo (`n = 29`):

```python
es_primo(29)
```

**Salida:**

```
Probando si 29 es primo...
  ¿29 divisible por 2? → False
  ¿29 divisible por 3? → False
  ¿29 divisible por 4? → False
  ¿29 divisible por 5? → False
  No se encontró ningún divisor. 29 ES primo.
```

---

### 🧪 Prueba con un número NO primo (`n = 15`):

```python
es_primo(15)
```

**Salida:**

```
Probando si 15 es primo...
  ¿15 divisible por 2? → False
  ¿15 divisible por 3? → True
  Sí, 15 es divisible por 3, entonces NO es primo.
```

---

Esto te permite **ver claramente cómo trabaja el `for` paso a paso**, y por qué se detiene apenas encuentra un divisor.

¿Quieres que agreguemos una lista de todos los divisores encontrados también?
"""