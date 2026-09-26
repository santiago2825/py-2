# Lista de días (1 = vino, 0 = faltó)
asistencias = [1, 0, 1, 1, 0, 1, 1]

# Guarda el número de asistencias
contador = 0

# Revisa día por día
for asistencia in asistencias:
    # Si vino ese día
    if asistencia == 1:
        contador += 1  # Suma 1

# Muestra el total
print("el estudiante asistió", contador, "veces")