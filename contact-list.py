#🗓️ Agenda

#datos de la agenda
agenda ={
    "Juan": "6789-1234",
    "Ana": "6123-4567",
    "Luis": "6987-2345"
}

# Acceder a un número
print ("Telefono de Ana:", agenda["Ana"])

# Agregar un nuevo contacto
agenda["Maria"] = "6111-2222"

# Eliminar un contacto
del agenda["Luis"]

# Ver toda la agenda
for nombre, telefono in agenda.items():
    print(f"{nombre}:{telefono}")