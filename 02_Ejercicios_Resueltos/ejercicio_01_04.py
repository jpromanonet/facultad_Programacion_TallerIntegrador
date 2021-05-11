# Declaro las variables y solicito al usuario que ingrese los numeros
primerNumero = int(input('Ingresar el numero de inicio: '))
segundoNumero = int(input('Ingresar el numero de fin: '))

# Arranco un bucle while entre el primer y segundo numero hasta que resuelva la condicion.
while primerNumero <= segundoNumero :
    if primerNumero%2 == 0 :
        print(primerNumero)
        primerNumero = primerNumero + 1
    else :
        primerNumero = primerNumero + 1
    