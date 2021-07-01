class Alumno():
    nombre = None
    apellido = None
    notas = []
    promedio = None
    estado = None

    def __init__(self):
        print("Ejercicio 1: ")
        print()
        self.nombre = input('Nombre del alumno: ')
        self.apellido = input('Apellido del alumno: ')
        print()
        print('Para salir ingresar 0 como nota')
        print()
        while True:
            nota = int(input('Ingrese una nota: '))
            if nota == 0:
                self.promedio = sum(self.notas) / len(self.notas)
                break
            elif nota >= 1 and  nota <=10:
                self.notas.append(nota)
            else:
                print("Nota invalidad intente de nuevo.")

    def __str__(self):
        if (self.promedio >= 7):
            self.estado = ' \"Promociona =)\"'
        elif(self.promedio >= 4 and self.promedio < 7):
            self.estado = ' \"Final :|\"'
        else:
            self.estado = ' \"Recursa... nos vemos el año que viene =(\"'
        return f"""
        ===> Estado del alumno y la materia <===

        * Alumno: {self.nombre} {self.apellido}

            * Promedio final: {self.promedio}
            * Estado de la materia: {self.estado}
        """


alumno = Alumno()
print(alumno)
