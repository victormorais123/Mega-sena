import pygame

pygame.init()

window_width, window_height = 800, 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("MegaSena")
white = (255, 255, 255)
black = (0, 0, 0)

class Button:
    def __init__(self, rect, text):
        self.rect = rect
        self.text = text

    def draw(self, surface):
        pygame.draw.rect(surface, white, self.rect)
        pygame.draw.rect(surface, black, self.rect, 3)
        font = pygame.font.Font(None, 36)
        text_render = font.render(self.text, True, black)
        text_rect = text_render.get_rect(center=self.rect.center)
        surface.blit(text_render, text_rect)

buttons = []
button_width, button_height = (60, 60)
button_margin = 10
start_x = (window_width - (3 * (button_width + button_margin))) / 2
start_y = (window_height - (4 * (button_height + button_margin))) / 2

for row in range(4):
    for col in range(3):
        number = row * 3 + col + 1
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
                        print("Clicked on button:", button.text)

    window.fill(black)
    for button in buttons:
        button.draw(window)
    pygame.display.flip()

pygame.quit()
