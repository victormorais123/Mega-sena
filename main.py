import pygame
import os
import random
from func import gerarRandomNumeros


def obternumeros():
    NumerosEscolhidos = []
    while len(NumerosEscolhidos) < 6:
        entrada = input(f"Digite um numero: ")
        if entrada.isdigit() and entrada not in NumerosEscolhidos:
            NumerosEscolhidos.append(int(entrada))
        else:
            print("Entrada invalida!")
    return NumerosEscolhidos

NumerosEscolhidos = obternumeros()

print(NumerosEscolhidos)

gerarRandomNumeros()
print(gerarRandomNumeros)
