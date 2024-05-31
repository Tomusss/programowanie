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

class Gracz(pygame.sprite.Sprite):
    def __init__(self, szerokosc_ekranu, wysokosc_ekranu):
        super().__init__()
        self.image = pygame.Surface([20,10])
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.x = szerokosc_ekranu/2
        self.rect.y = wysokosc_ekranu - self.rect.height
        self.predkosc = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.predkosc
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.predkosc


# Ustawienia gry
FPS = 60
dziala = True
zegar = pygame.time.Clock()

owoce = pygame.sprite.Group()
bomby = pygame.sprite.Group()
gracz = pygame.sprite.GroupSingle(Gracz(SZEROKOSC, WYSOKOSC))

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
    # Aktualizacja
    owoce.update()
    bomby.update()
    gracz.update()
    # Rysowanie
    ekran.fill('lightblue')
    owoce.draw(ekran)
    bomby.draw(ekran)
    gracz.draw(ekran)

    pygame.display.update()

    zegar.tick(FPS)

pygame.quit()
