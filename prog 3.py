print(f'{"programa 3 operaciones":.^90}')
print(f'{"MENU PRINCIPAL":.^90}')
print("S. suma")
print("R. resta")
print("M. multiplicacion")
print(]"D. division")
print("A. salir")
opcion = input("¿que opcion desea utilizar?: ").lower()
if opcion == S:
    num1 = int(input("ingrerse numero 1: "))
    num2 = int(input("ingrese numero 2: "))
    result = (f'{"resultado: "}{num1+num2}')
elif opcion == R:
    num1 = int(input("ingrese numnero 1: "))
    num2 = int(input("ingrese numero 2: "))
    result = (f'{"resultado: "}{num1-num2}')
elif opcion == M:
    num1 = int(input("ingrese numero 1: "))
    num2 = int(input("ingrese numero 2: "))
    result = (f'{"resultado: "}{num1*num2}')
elif opcion == D:
    num1 = int(input("ingrese numero 1: "))
    num2 = int(input("ingrese numero 2: "))
    result = (f'{"resultado: "}{num1/num2}')
elif opcion == A:
    result = (f'{"saliendo del programa..."}')
print (result)

