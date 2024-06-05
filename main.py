import pygame
import random

pygame.init()
pygame.font.init()

# Ustawienia ekranu
SZEROKOSC = 800
WYSOKOSC = 600

# Ekran
screen = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))

pygame.display.set_caption('Mates łapie owoce')

class Owoce(pygame.sprite.Sprite):
    mnoznik = 1.1
    def __init__(self, szerokosc_ekranu, wysokosc_ekranu):
        super().__init__()
        self.image = pygame.Surface([30, 30])
        self.image.fill('red')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, szerokosc_ekranu - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randrange(2, 4)/3
        self.wysokosc_ekranu = wysokosc_ekranu

    def update(self):
        self.rect.y += (1+self.speed)*Owoce.mnoznik
        if self.rect.top -10 > self.wysokosc_ekranu:
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
        self.image = pygame.Surface([60,10])
        self.image.fill('blue')
        self.rect = self.image.get_rect()
        self.rect.x = szerokosc_ekranu/2
        self.rect.y = wysokosc_ekranu - self.rect.height
        self.predkosc = 6

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.predkosc
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.predkosc

        if self.rect.x > SZEROKOSC-self.rect.width:
            self.rect.x = SZEROKOSC-self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0

#def Pauza():
   



# Ustawienia gry
FPS = 60
dziala = True
zegar = pygame.time.Clock()

owoce = pygame.sprite.Group()
bomby = pygame.sprite.Group()
gracz = pygame.sprite.GroupSingle(Gracz(SZEROKOSC, WYSOKOSC))
wynik = 0
zycia = 3
max_owocow = 3
max_bomb = 1
szansa_owocow = 0.003
szansa_bomb = 0.001
poziom = 1
pauza = False



while dziala:

    # Zamykanie
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            dziala = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pauza = not pauza
       
    # Dodawanie nowych owoców
    if len(owoce) < max_owocow:
        if random.random() < szansa_owocow:
            nowy_owoc = Owoce(SZEROKOSC, WYSOKOSC)
            owoce.add(nowy_owoc)
    if len(bomby) < max_bomb:
        if random.random() < szansa_bomb:
            bomby.add(Bomby(SZEROKOSC, WYSOKOSC))

    # Kolizje
    kolizje_owoce = pygame.sprite.spritecollide(gracz.sprite,owoce,True)
    for kolizja in kolizje_owoce:
        wynik += 1
        if wynik%5== 0:
            poziom = wynik//10
            szansa_bomb += 0.0005
            szansa_owocow += 0.0001
            Owoce.mnoznik += 0.1
            poziom += 1
        if wynik%10 == 0:
            max_owocow += 1
            max_bomb += 1

    if pygame.sprite.spritecollide(gracz.sprite,bomby,False):
        dziala = False
    for owoc in owoce:
        if owoc.rect.top > WYSOKOSC:
            owoc.kill()
            zycia -=1
            if zycia <= 0:
                dziala = False

    # Aktualizacja
    if not pauza:
        owoce.update()
        bomby.update()
        gracz.update()
    


    # Rysowanie
    screen.fill('lightblue')
    owoce.draw(screen)
    bomby.draw(screen)
    gracz.draw(screen)

    # Wynik
    font = pygame.font.Font(None, 20)
    wynik_text = font.render(f'Wynik: {wynik}', True, 'black')
    zycia_text = font.render(F'Życia: {zycia}', True, 'red')
    poziom_text = font.render(F'Poziom: {poziom}', True, 'blue')
    screen.blit(wynik_text, (10, 10))
    screen.blit(zycia_text,(10,30))
    screen.blit(poziom_text,(10,50))


    pygame.display.update()

    # FPS
    zegar.tick(FPS)

pygame.quit()
