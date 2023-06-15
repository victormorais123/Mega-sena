import pygame
import random
import time
from func import enviar_sms , tecladoNum

NumerosEscolhidos = []
numerosComputador = []
cont = 0

"""pygame.init()

window_width, window_height = 800,600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("MegaSena")
white = (255,255,255)
black = (0,0,0)

class Button:
    def __init__(self, rect, text):
        self.rect = rect
        self.rect = text

    def draw(self, surface):
        pygame.draw.rect(surface, white, self.rect)
        pygame.draw.rect(surface, black, self.rect, 3)
        font = pygame.font.Font(None, 36)
        text_render = font.render.get_rect(center = self.rect.center)
        text_rect = text_render.get_rect(center=self.rect.center)
        surface.blit(text_render, text_rect)

buttons = []
button_width, button_height = (60, 60)
button_margin = 10
start_x = (window_width - (3 * (button_width + button_margin))) / 2
start_y = (window_height - (4 * (button_height + button_margin))) / 2

for row in range(4):
    for col in range(3):
        number = row * 3 + col +1
        x = start_x + col * (button_width + button_margin)
        y = start_y + row * (button_height + button_margin)
        rect = pygame.Rect(x, y, button_width, button_height)
        button = Button(rect, str(number))
        buttons.append(button)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.rect.collidepoint(mouse_pos):
                        print("clicou no Botão: ", button.text)

window.fill(black)
for button in buttons:
    button.draw(window)
pygame.display.flip()"""





while len(NumerosEscolhidos) < 3:
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
inicio = time.time()
while rodarnumero:
    
    for i in range(0,3):
        
        numero = random.randint(0,61)
        numerosComputador.append(numero)
    numerosComputador.sort()
    print(NumerosEscolhidos)
    print(numerosComputador)
    if numerosComputador == NumerosEscolhidos:
        fim = time.time()
        tempo_total = fim - inicio
        minutos = int(tempo_total // 60)
        segundos_restantes = int(tempo_total % 60)
        milisegundos =int((tempo_total % 1) * 1000) 
        
        print("Tempo total:", minutos, segundos_restantes, milisegundos)
        print("parabens, voce ganhou")
        print("os numeros sorteados foram", numerosComputador)
        print("foi tentado", cont, "vezes")
        rodarnumero = False
        
    else:
        cont = cont + 1
        numerosComputador = []
enviar_sms("", "Acertei  numeros")