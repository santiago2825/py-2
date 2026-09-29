# Diccionario con las materias y sus notas
Notas = {"Matemáticas": 8.5,"Inglés": 7.0, "Programación": 9.2}
# Variable para guardar la suma de las notas
total= 0
# Recorre solo las notas
for Nota in Notas.values():
    total += Nota
# Calcula el promedio dividiendo entre la cantidad de materias
promedio = total / len(Notas)
# Muestra el promedio en pantalla
print("Promedio:", promedio)
    