import pygame
import random
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Fruit Catch")

white = (255,255,255)

basket_img = pygame.image.load("basket.png")
apple_img = pygame.image.load("apple.png")
banana_img = pygame.image.load("banana.png")

class Basket(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = basket_img
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def update(self):
        key = pygame.key.get_pressed()
        if key[K_LEFT] and self.rect.left > 0:
            self.rect.x -= 7
        if key[K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += 6  
            
class Fruit(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]
        self.speed = random.randint(4,7)

    def update(self):
        self.rect.y += self.speed

basket_group = pygame.sprite.Group()
fruit_group = pygame.sprite.Group()

basket = Basket(screen_width//2, screen_height - 60)
basket_group.add(basket)

spawn_timer = 0
spawn_delay = 800

run = True
while run:
    clock.tick(fps)
    screen.fill((255,255,254))  

    time_now = pygame.time.get_ticks()
    if time_now - spawn_timer > spawn_delay:
        x = random.randint(0, screen_width - 64)
        fruit1 = Fruit(x, 0, random.choice([apple_img, banana_img]))
        fruit2 = Fruit(x, 0, random.choice([apple_img, banana_img]))
        fruit_group.add(fruit1)
        fruit_group.add(fruit2)
        spawn_timer = time_now

    basket_group.update()
    fruit_group.update()

    basket_group.draw(screen)
    fruit_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:   
            run = False

    pygame.display.update()

pygame.quit()