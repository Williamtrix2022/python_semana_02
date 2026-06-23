#Siguiente paso — Proyecto de la semana
#Ya tienes todo lo necesario para construir el procesador de calificaciones 
# — tu segundo proyecto de portafolio. Es un script que:

#Tiene una lista de estudiantes con nombre y nota
#Calcula promedio general, aprobados y reprobados
#Muestra el mejor y peor estudiante
#Genera un reporte organizado en consola

estudiantes = [
    {"nombre": "Ana", "nota": 7},
    {"nombre": "Luis", "nota": 5},
    {"nombre": "Carlos", "nota": 8},
    {"nombre": "Maria", "nota": 4},
    {"nombre": "Jose", "nota": 6}
]

total_notas = 0
aprobados = 0
reprobados = 0

for estudiante in estudiantes:
    total_notas += estudiante["nota"]
    if estudiante["nota"] >= 6:
        aprobados += 1
    else:
        reprobados += 1

promedio = total_notas / len(estudiantes) if estudiantes else 0

mejor_estudiante = max(estudiantes, key=lambda x: x["nota"]) if estudiantes else None
peor_estudiante = min(estudiantes, key=lambda x: x["nota"]) if estudiantes else None

print("Reporte de Calificaciones")
print("-" * 30)
print(f"Promedio general: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")

if mejor_estudiante:
    print(f"Mejor estudiante: {mejor_estudiante['nombre']} ({mejor_estudiante['nota']})")

if peor_estudiante:
    print(f"Peor estudiante: {peor_estudiante['nombre']} ({peor_estudiante['nota']})")

    