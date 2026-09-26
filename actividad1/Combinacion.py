# Lista de estudiantes, cada uno guardado como un diccionario
estudiantes = [
    {"nombre": "Carlos", "nota": 9.0},
    {"nombre": "Ana", "nota": 5.5},
    {"nombre": "Luis", "nota": 7.0}
]
# Variable para acumular la suma de todas las notas
total = 0
# Recorre cada estudiante de la lista
for estudiante in estudiantes:

    nombre = estudiante["nombre"]
    nota = estudiante["nota"]
# Revisa si aprobó
    if nota >= 6.0:
        print(nombre, "Aprobado")
    else:
        print(nombre, "Reprobado")
# Acumula la nota al total
    total += nota
# Calcula el promedio dividiendo el total entre el número de estudiantes (3)
promedio = total / len(estudiantes)
# Imprime el promedio 
print("Promedio general del curso:", round(promedio, 2))