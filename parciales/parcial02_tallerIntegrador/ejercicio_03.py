# Ejercicio 3

# importo functools
import functools

# declaro variables e inputs
number = input("Introduzca un numero: ")
factorialNumber = (functools.reduce(lambda x,y:x*y,list(range(2,int(number)+1))))
print()
print("El factorial es: ")
print(factorialNumber)
