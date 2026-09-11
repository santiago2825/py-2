# Lista inicial con 5 notas
notas=[3.5,4.0,4.5,25,3.0]
# Agrega la nota
notas.append(4.8)
# Imprime: Notas
print("Notas",notas)

notas.remove(min(notas))
# Imprime la lista final sin el 3.0: [3.5, 4.0, 4.5, 25, 4.8]
print("Notas despues de elimina la más baja",notas)