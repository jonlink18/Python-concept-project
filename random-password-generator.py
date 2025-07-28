import random
import string

longitud = 12

caracteres = string.ascii_letters + string.digits +string.punctuation

contrasena = '' .join(random.choice(caracteres) for _ in range(longitud))

print("Contraseña generada:", contrasena)


"""🔍 Explicación paso a paso:

    import random – para elegir al azar.

    import string – trae listas de letras, números y símbolos:

        string.ascii_letters: letras A-Z y a-z.

        string.digits: números 0-9.

        string.punctuation: símbolos como !@#$%&*.

    longitud – decides cuántos caracteres tendrá la contraseña.

    random.choice(caracteres) – elige un carácter aleatorio.

    ''.join(... for _ in range(longitud)) – une todos los caracteres en un solo string."""
