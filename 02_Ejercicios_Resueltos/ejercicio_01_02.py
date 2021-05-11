# Ejercio 1.2 de la Guia Tematica de ejercicios del taller integrador

## Declaro variables y asigno valores

print("<===== Calculo de Area y Perimetro de un rectangulo =====>")
print("")
baseRectangulo = input("Por favor, ingresa la base del rectangulo: ")
alturaRectangulo = input("Por favor, ingresa la altura del rectangulo: ")
print("")

## Calculo perimetro y area

perimetroRectangulo = (float(baseRectangulo)*2) + (float(alturaRectangulo)*2)
areaRectangulo = float(baseRectangulo)*float(alturaRectangulo)

## Imprimo en pantalla

print("El area del rectangulo es: ")
print(areaRectangulo)
print("")
print("El perimetro del rectangulo es: ")
print(perimetroRectangulo)