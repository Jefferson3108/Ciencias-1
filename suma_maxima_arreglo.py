import random  # Importamos el módulo para generar números aleatorios

# Pedimos al usuario los límites del rango
print("Ingrese el numero minimo que puede tener el arreglo")
num_a = int(input())

print("Ingrese el numero maximo que puede tener el arreglo")
num_b = int(input())

print("Ingrese cuantos numeros quiero que tenga el arreglo")
num_c = int(input())

# Generamos un arreglo con números aleatorios SIN repetir
# range(num_a, num_b) genera números desde num_a hasta num_b - 1
# random.sample toma num_c números distintos de ese rango
numeros = random.sample(range(num_a, num_b), num_c)


# Función principal que calcula la suma máxima de un subarreglo
def calcular_suma_maxima(array):
    
    # Si el arreglo está vacío, la suma máxima es 0
    if not array:
        return 0
    
    # Llamamos a la función recursiva que aplica divide y vencerás
    return calcular_mitad(array, 0, len(array) - 1)


# Función recursiva que divide el arreglo en mitades
def calcular_mitad(array, low, high):
    
    # Caso base: si solo hay un elemento
    if low == high:
        return array[low]
    
    # Calculamos el punto medio
    mitad = (low + high) // 2

    # Suma máxima en la mitad izquierda
    max_izq = calcular_mitad(array, low, mitad)

    # Suma máxima en la mitad derecha
    max_der = calcular_mitad(array, mitad + 1, high)

    # Suma máxima cruzando el centro
    max_cruz = max_cruzando(array, low, mitad, high)

    # Retornamos la mayor de las tres
    return max(max_izq, max_der, max_cruz)


# Función que calcula la suma máxima que cruza la mitad
def max_cruzando(array, low, mid, high):
    
    # ---- Parte izquierda ----
    suma = 0
    suma_izq = float('-inf')  # Inicializamos en menos infinito
    
    # Recorremos desde el medio hacia la izquierda
    for i in range(mid, low - 1, -1):
        suma += array[i]
        suma_izq = max(suma_izq, suma)

    # ---- Parte derecha ----
    suma = 0
    suma_der = float('-inf')
    
    # Recorremos desde el medio+1 hacia la derecha
    for i in range(mid + 1, high + 1):
        suma += array[i]
        suma_der = max(suma_der, suma)

    # Retornamos la suma combinada izquierda + derecha
    return suma_izq + suma_der


# Mostramos el arreglo generado
print(numeros)

# Mostramos la suma máxima encontrada
print("La suma maxima es:", calcular_suma_maxima(numeros))
   




                


 
