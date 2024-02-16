# Crear un pequeño programa que realice una función aritmética que permita al usuario ingresar datos por la terminal acorde a distintas opciones.  Para ellos debemos definir una función que reciba parámetros:
# Combinar funciones nativas y funciones definidas,
# condicionales, y bucles.
# Si el usuario ingresa el nro 1, realiza la acción A.
# Si el usuario ingresa el nro 2, realiza la acción B.

def accion_A(num1, num2):
    return num1 + num2

def accion_B(num1, num2):
    return num1 - num2

def main():
    opcion = input("Ingrese 1 para realizar la acción A o 2 para realizar la acción B: ")

    while opcion not in ('1', '2'):
        print("Opción inválida. Por favor ingrese 1 o 2.")
        opcion = input("Ingrese 1 para realizar la acción A o 2 para realizar la acción B: ")

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == '1':
        resultado = accion_A(num1, num2)
        print("El resultado de la acción A es:", resultado)
    elif opcion == '2':
        resultado = accion_B(num1, num2)
        print("El resultado de la acción B es:", resultado)

if __name__ == "__main__":
    main()
