import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

estudiante = {
    "horas_estudio":[2,4,5,6,8,10,3,7,9,1],
    "asistencia":[60,70,75,80,90,95,65,85,92,50],
    "aprobo":[0,0,1,1,1,1,0,1,1,0]
}
#print("---------------------------PANDAS--------------------------------------------------")
df =pd.DataFrame(estudiante)
df["promedio_samanal"]=df["horas_estudio"]/7
filtro_aprobados =df[(df["aprobo"]==1)&(df["horas_estudio"]<6)]
#print("-------------------------------NUMPY----------------------------------------------")
asistencia_1=np.array(estudiante["asistencia"])
promedio_asistencia =np.mean(asistencia_1)
desviacion = np.std(asistencia_1)
#print("-------------------------SCIKIT-LEARN----------------------------------------------")
x = df[["horas_estudio","asistencia"]]
y= df["aprobo"]
x_train, x_test, y_train, y_test= train_test_split(
    x,y, test_size=0.3, random_state=42, stratify=y
)
modelo=DecisionTreeClassifier(random_state=42)
modelo.fit(x_train, y_train)
predicciones = modelo.predict(x_train)
precision = accuracy_score(y_train, predicciones)
print("precision del modelo", precision*100,"%")
nuevo_aprendiz = pd.DataFrame({"horas_estudio":[5],"asistencia":[78]})
resultado= modelo.predict(nuevo_aprendiz)
print("resultado numerico", resultado[0])
if resultado[0]==1:
    print("el modelo predice qu el aprendiz aprobara")
else:
    print("el modelo predice que el aprendiz no aprobara")
#print("---------------------------PANDAS--------------------------------------------------")
#print("\nestadistica", df.describe())
#print("-----------------------------------------------------------------------------")
#print("\npromedio semanal", df)
#print("-----------------------------------------------------------------------------")
#print("estudiantes aprobados con menos horas", filtro_aprobados)
#print("-----------------------------------------------------------------------------")
#print("-------------------------------NUMPY----------------------------------------------")
#print("promedio de asistencia", promedio_asistencia)
#print("desviacion", desviacion)