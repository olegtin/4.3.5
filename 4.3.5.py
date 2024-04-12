import pygame
import sys


pygame.init()
screen = pygame.display.set_mode((600, 600))
score = 0


class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Sprite, self).__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        screen.blit(self.image, (self.x, self.y))


lenin = Sprite(100, 100,50,50)
clock = pygame.time.Clock()
zlo = Sprite(300, 500, 60, 10)
while True:
    screen.fill((128, 255, 128))

    clr = (0, 0, 0)
    font = pygame.font.Font(None, 36)
    text = font.render(f"Счет {score}", True, clr)
    text_rect = text.get_rect()
    text_rect.center = (50, 50)

    if pygame.event.get(pygame.QUIT):
        sys.exit()
    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] :
            lenin.x += 9
        elif keys[pygame.K_a] :
            lenin.x -= 9
        elif keys[pygame.K_s] :
            lenin.y += 9
        elif keys[pygame.K_w]  and not pygame.sprite.collide_mask(zlo, lenin):
            lenin.y -= 9
    if not pygame.sprite.collide_mask(zlo, lenin):
        zlo.y += 1

    if pygame.sprite.collide_mask(zlo, lenin):
        print(f'столкновение номер {score}')
        score+=1
        zlo.y = 0

    screen.blit(text, text_rect)
    lenin.update()
    zlo.update()
    pygame.display.update()
    clock.tick(60)

pygame.quit()