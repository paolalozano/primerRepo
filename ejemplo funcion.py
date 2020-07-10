def repetir(texto,numero):
    texto += "\n"
    print(texto*numero)

texto = input("ingresa un texto: ")
numero = int(input("ingresa un numero: "))
repetir(texto,numero)