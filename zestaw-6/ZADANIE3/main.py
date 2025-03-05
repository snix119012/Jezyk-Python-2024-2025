import pygame
from random import randint

pygame.init()

# Kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)
CZERWONY = (255, 0, 0)

class Rakietka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        if self.rect.x < 0:
            self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        if self.rect.x > 600:
            self.rect.x = 600

class Pilka(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        self.velocity = [randint(-5, 5), randint(4, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = -self.velocity[1] + randint(-2, 2)

# Rozmiary i okno gry
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietkaA = Rakietka(BIALY, 100, 10)
rakietkaA.rect.x = 300
rakietkaA.rect.y = 450

pileczka = Pilka(BIALY, 10, 10)
pileczka.rect.x = 345
pileczka.rect.y = 195

all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(rakietkaA)
all_sprites_list.add(pileczka)

kontynuuj = True
clock = pygame.time.Clock()
score = 0

# Funkcja do obsługi ekranu Game Over
def game_over():
    global score
    # Odczyt najlepszego wyniku z pliku
    try:
        with open("highscore.txt", "r") as file:
            highscore = int(file.read())
    except (FileNotFoundError, ValueError):
        highscore = 0

    # Aktualizacja najlepszego wyniku
    if score > highscore:
        highscore = score
        with open("highscore.txt", "w") as file:
            file.write(str(highscore))

    font = pygame.font.Font(None, 74)
    screen.fill(CZARNY)

    # Wyświetlanie komunikatu Game Over
    text = font.render("Game Over", 1, BIALY)
    screen.blit(text, (250, 150))

    # Wyświetlanie aktualnego wyniku
    current_score_text = font.render(f"Score: {score}", 1, BIALY)
    screen.blit(current_score_text, (250, 250))

    # Wyświetlanie najlepszego wyniku
    highscore_text = font.render(f"Highscore: {highscore}", 1, BIALY)
    screen.blit(highscore_text, (250, 300))

    # Rysowanie przycisku "Play Again"
    button_font = pygame.font.Font(None, 50)
    button_text = button_font.render("Play Again", 1, CZARNY)
    button_rect = pygame.Rect(275, 400, 200, 50)
    pygame.draw.rect(screen, BIALY, button_rect)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return

# Główna pętla programu
while kontynuuj:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            kontynuuj = False

    # Obsługa klawiszy
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        rakietkaA.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        rakietkaA.moveRight(5)

    # Aktualizacja pozycji piłeczki
    all_sprites_list.update()

    # Sprawdzanie kolizji piłki z krawędziami
    if pileczka.rect.x >= 690 or pileczka.rect.x <= 0:
        pileczka.velocity[0] = -pileczka.velocity[0]
    if pileczka.rect.y <= 0:
        pileczka.velocity[1] = -pileczka.velocity[1]
    if pileczka.rect.y >= 490:  # Piłka dotarła na dół ekranu
        game_over()
        pileczka.rect.x = 345
        pileczka.rect.y = 195
        pileczka.velocity = [randint(-5, 5), randint(4, 8)]
        score = 0

    # Sprawdzanie kolizji piłki z rakietką
    if pygame.sprite.collide_mask(pileczka, rakietkaA):
        pileczka.bounce()
        score += 1

    # Rysowanie obiektów na ekranie
    screen.fill(CZARNY)
    pygame.draw.line(screen, CZERWONY, [0, 450], [700, 450], 5)
    all_sprites_list.draw(screen)

    # Wyświetlanie wyniku
    font = pygame.font.Font(None, 74)
    text = font.render(str(score), 1, BIALY)
    screen.blit(text, (350, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
