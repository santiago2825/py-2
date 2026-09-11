# Diccionario que asocia días de la semana con sus respectivas materias
horario = {"Lunes": "Matemáticas", "Martes": "Inglés","Miércoles": "Programación"}
# Pide al usuario que escriba un día
dia=input("Ingrese el dia: ")
# .get() busca el día en el diccionario. Si no lo encuentra, devuelve None
materia = horario.get(dia)
# Si encontró la materia 
if materia:
    print("La Materia es: ", materia)
else:
    print("Ese dia no existe en el horario")