import pygame
import os
import random
from func import lerString

NumerosEscolhidos = []
while len(NumerosEscolhidos) < 6:
    try:
        entrada = int(input("digite um numero: "))
        if entrada in NumerosEscolhidos or entrada > 60 or entrada == 0:
            print("Entrada invalida!")
        else:
            NumerosEscolhidos.append(int(entrada))
    except:
        print("valor incorreto")
print(NumerosEscolhidos)

