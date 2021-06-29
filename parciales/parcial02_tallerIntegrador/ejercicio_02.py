# Importo el randomizer
import random

# Declaro las variables del inicio, fin y limite de numeros por lista
start = 2000
stop = 5000
limit = 1000

# Ejercicio 2.1
## Lista de 1000 numeros en el rango de 2000 a 5000
randomNumbersList = [random.randrange(start, stop) for iter in range(limit)]
print("Ejercicio 2.1: ")
print("Lista de 1000 numeros entre 2000 a 5000: ")
print()
print(randomNumbersList)
print()
print("Elementos dentro de la lista: ")
print(len(randomNumbersList))

# Ejercicio 2.2
evenNumbers = list(filter(lambda x : x%2==0 ,randomNumbersList))
print()
print("Ejercicio 2.2: ")
print("Filtro solo los pares de la lista anterior usando una lambda: ")
print()
print(evenNumbers)