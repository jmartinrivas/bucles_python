# Bucles [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Realice una calculadora:
Dentro de un bucle se debe ingresar por línea de comando dos números
Luego se ingresará como tercera entrada al programa el símbolo de la operación
que se desea ejecutar:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Exponente/Potencia (**)
Se debe efectuar el cálculo correcto según la operación ingresada por consola
Imprimir en pantalla la operación realizada y el resultado

El programa se debe repetir dentro del bucle hasta que como operador
se ingrese la palabra "FIN", en ese momento debe terminar el programa

Se debe debe imprimir un cartel de error si el operador ingresado no es
alguno de lo soportados o no es la palabra "FIN".
'''

print("Mi Calculadora (^_^)")
# Empezar aquí la resolución del ejercicio
while True:
    try:
        numero_1 = int(input("Escribe el primer numero: "))
        numero_2 = int(input("Escribe el segundo numero: "))
        operación = input("Ingrese la oeración que desea realizar:\n Suma(+)\n Resta(-)\n Multipicación(*)\n Exponente o Potencia (**)")
    except ValueError:
        print("El valor ingresado es incorrecto, por favor vuelva a intentarlo")
        continue
    if operación.lower() == "fin":
        break
    elif operación == "+":
        suma=numero_1+numero_2
        print ("La operacion seleccionada es suma entre:",numero_1,"y",numero_2, "y el resultado es:",suma)
    elif operación == "-":
        resta=numero_1-numero_2
        print ("La operacion seleccionada es resta entre:",numero_1,"y",numero_2, "y el resultado es:",resta)
    elif operación == "*":
        multiplicacion=numero_1*numero_2
        print ("La operacion seleccionada es multiplicacion entre:",numero_1,"y",numero_2, "y el resultado es:",multiplicacion)
    elif operación == "/":
        division=numero_1/numero_2
        print ("La operacion seleccionada es division entre:",numero_1,"y",numero_2, "y el resultado es:",division)
    elif operación == "**":
        potencia=numero_1**numero_2
        print ("La operacion seleccionada es potencia entre:",numero_1,"y",numero_2, "y el resultado es:",potencia)
    else:
        print("La opcion ingresada es incorrecta, por favor vuelva a seleccionar la operacion deseada:")
print("Fin del Programa")
