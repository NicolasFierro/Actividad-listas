# Crear listas vacias de aprendices y edades
aprendices = []
edades = []

# Llenar las listas solicitando datos por teclado
num_aprendices = int(input("Cuantos aprendices deseas ingresar: "))
for i in range(num_aprendices):
    nombre = input(f"Ingrese el nombre del aprendiz {i + 1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    aprendices.append(nombre)
    edades.append(edad)

# Imprimir las listas
print("Lista de Aprendices:", aprendices)
print("Lista de Edades:", edades)

# Encontrar el aprendiz con la mayor edad
indice_mayor_edad = edades.index(max(edades))
print(f"El aprendiz con la mayor edad es {aprendices[indice_mayor_edad]} con {max(edades)} años.")

# Insertar el nombre de la instructora que dirije la formacion
nombre_instructora = input("Ingrese el nombre de la instructora: ")
aprendices.insert(1, nombre_instructora)

# Contar cuantos aprendices tienen la mayoria de edad
conteo_edad = edades.count(18)
print(f"Hay {conteo_edad} aprendices que son mayor de edad.")

# Agregarme al final de la lista
aprendices.append("Nicolas Fierro")

# Borrar el nombre de la instructora de la lista si existe
if nombre_instructora in aprendices:
    aprendices.remove(nombre_instructora)

# Indicar un dato a buscar en la lista de aprendices
dato_a_buscar = input("Ingrese un dato a buscar en la lista de aprendices: ")
if dato_a_buscar in aprendices:
    print(f"{dato_a_buscar} se encuentra en la lista de aprendices.")
else:
    print(f"{dato_a_buscar} no se encuentra en la lista de aprendices.")

# Mostrar los primeros 10 aprendices de la lista
print("Los primeros 10 aprendices son:", aprendices[:10])

# Mostrar los 10 ultimos aprendices de la lista
print("Los 10 ultimos aprendices son:", aprendices[-10:])

# Mostrar del elemento 10 al elemento 20
print("Del elemento 10 al elemento 20:", aprendices[9:19])

