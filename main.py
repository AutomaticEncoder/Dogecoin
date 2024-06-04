import pygame
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Dogecoin clicker')
doge = pygame.image.load('doge.jpg')
coin = 0
run = True
while run:
    mouse = pygame.mouse.get_pos()
    doge_rect = doge.get_rect(topleft = (150, 150))
    screen.blit(doge, (150, 150))
    pygame.display.update()
    if doge_rect.collidepoint(mouse):
        if pygame.mouse.get_pressed()[0]:
            clock.tick(3)
            coin += 1
            print(f'Coin: {coin}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
