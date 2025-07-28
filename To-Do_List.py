#✅ Lista de tareas (To-Do List) con diccionarios

tareas = [
    {"tarea":"Estudiar Python", "completada": False}, # tarea 0
    {"tarea":"Hacer ejercicio", "completada": True},  # tarea 1
    {"tarea":"Leer un libro", "completada": False}   # tarea 2
]

print ("Tareas pendientes:")
for tarea in tareas:
    if not tarea["completada"]:
        print ("-", tarea["tarea"])


tareas[0]["completada"] = True 

tareas.append({"tarea":"Limpiar la casa","completada":False})

print("\nTodas las tareas")

for tarea in tareas:
    estado = "✔️ " if tarea["completada"] else "❌ "
    print(f"{estado} {tarea['tarea']}")