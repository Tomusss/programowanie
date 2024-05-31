import pygame
import random

pygame.init()

# Ustawienia ekranu
SZEROKOSC = 800
WYSOKOSC = 600

# Ekran
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption('Mates łapie owoce')

class Owoce(pygame.sprite.Sprite):
    def __init__(self, szerokosc_ekranu, wysokosc_ekranu):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, szerokosc_ekranu - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(1, 3)
        self.wysokosc_ekranu = wysokosc_ekranu

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > self.wysokosc_ekranu:
            self.kill() 
class Bomby(Owoce):
    def __init__(self, szerokosc_ekranu, wysokosc_ekranu):
        super().__init__(szerokosc_ekranu, wysokosc_ekranu)
        self.image.fill('black')
    def update(self):
        super().update()
# Ustawienia gry
FPS = 60
dziala = True
zegar = pygame.time.Clock()

owoce = pygame.sprite.Group()
bomby = pygame.sprite.Group()

while dziala:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala = False
    
    # Dodawanie nowych owoców
    if random.random() < 0.01:
        nowy_owoc = Owoce(SZEROKOSC, WYSOKOSC)
        owoce.add(nowy_owoc)
    if random.random() < 0.005:
            bomby.add(Bomby(SZEROKOSC, WYSOKOSC))
    owoce.update()
    bomby.update()
    # Rysowanie
    ekran.fill('lightblue')
    owoce.draw(ekran)
    bomby.draw(ekran)
    pygame.display.update()

    zegar.tick(FPS)

pygame.quit()
