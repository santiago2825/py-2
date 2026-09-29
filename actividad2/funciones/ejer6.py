def verificar(asistencias):
    falta = 0
    for dia in asistencias:
        if dia == 0:
            falta +=1
    print("el aprendiz falto",falta,"veces")
    if falta > 2:
        print("ALERTA")

REGISTRO = [1,1,0,0,0,0]
verificar(REGISTRO)