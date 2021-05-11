# Declaro las variables para las operaciones

primerNumero = int(input('Ingrese el primer numero Real: '))
segundoNumero = int(input('Ingrese el segundo numero Real: '))

# Imprimo los resultados utilizando las operaciones aritmeticas.
if segundoNumero <= 0 :
    # Suma
    suma = primerNumero + segundoNumero
    # Resta
    resta = primerNumero - segundoNumero
    # Multiplicacion
    multiplicacion = primerNumero * segundoNumero

    print('---------------- Resultados -------------------')
    print('')
    print('Suma: ',suma)
    print('Resta: ',resta)
    print('Multiplicacion: ', multiplicacion)
    print('La division no se puede realizar')
else :
    suma = primerNumero + segundoNumero
    resta = primerNumero - segundoNumero
    multiplicacion = primerNumero * segundoNumero
    division = primerNumero / segundoNumero

    print('---------------- Resultados -------------------')
    print('')
    print('Suma: ',suma)
    print('Resta: ',resta)
    print('Multiplicacion: ', multiplicacion)
    print('division: ', division)