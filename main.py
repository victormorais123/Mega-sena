import pygame
import random
from func import enviar_sms
NumerosEscolhidos = []
numerosComputador = []
cont = 0
pygame.init()

while len(NumerosEscolhidos) < 2:
    try:
        entrada = int(input("digite um numero: "))
        if entrada in NumerosEscolhidos or entrada > 60 or entrada == 0:
            print("Entrada invalida!")
        else:
            NumerosEscolhidos.append(int(entrada))
    except:
        print("valor incorreto")

NumerosEscolhidos.sort()
rodarnumero = True

while rodarnumero:
    for i in range(0,2):
        numero = random.randint(0,61)
        numerosComputador.append(numero)
    numerosComputador.sort()
    print(NumerosEscolhidos)
    print(numerosComputador)
    if numerosComputador == NumerosEscolhidos:
        print("parabens, voce ganhou")
        print("os numeros sorteados foram", numerosComputador)
        print("foi tentado", cont, "vezes")
        rodarnumero = False
    else:
        cont = cont + 1
        numerosComputador = []
enviar_sms("+5554999837827", "Acertei  numeros")