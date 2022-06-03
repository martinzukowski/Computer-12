# python game
import pygame
import os
pygame.font.init()
pygame.mixer.init()

width, height = 700, 900
WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Marty Party! ")

WHITE = (255,255,255)
BLACK = (0, 0, 0)
BORDER = pygame.Rect(0, height//2 - 5, width, 10)
HIT_SOUND = pygame.mixer.Sound(os.path.join('games', 'pygame', 'Assets', 'sonic.mp3'))
FIRE_SOUND = pygame.mixer.Sound(os.path.join('games', 'pygame', 'Assets', 'gunsound.mp3'))
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
HEALTH_FONT = pygame.font.SysFont('comicsans' , 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
VEL = 5
BULLET_VEL = 7
FPS = 60
MAX_BULLETS = 10
character_width, character_height = 55, 40

BOTTOM_HIT = pygame.USEREVENT + 1
TOP_HIT = pygame.USEREVENT + 2

megaman_image = pygame.image.load(os.path.join('games', 'pygame', 'Assets', 'megaman.png'))
mega_man = pygame.transform.rotate(pygame.transform.scale(megaman_image, (character_width, character_height)), 0)
otherguy_image = pygame.image.load(os.path.join('games', 'pygame', 'Assets', '8bit.png'))
other_guy = pygame.transform.rotate(pygame.transform.scale(otherguy_image, (character_width, character_height)), 0)

SPACE = pygame.transform.scale(pygame.image.load(os.path.join('games', 'pygame', 'Assets', 'sea.png')), (width, height))

def handle_bullets(bottom_bullets, top_bullets, bottom, top):
    for bullet in bottom_bullets:
        bullet.y -= BULLET_VEL
        if top.colliderect(bullet):
            pygame.event.post(pygame.event.Event(TOP_HIT))
            bottom_bullets.remove(bullet)
        elif bullet.y < 0:
            bottom_bullets.remove(bullet)
    
    for bullet in top_bullets:
        bullet.y += BULLET_VEL
        if bottom.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BOTTOM_HIT))
            top_bullets.remove(bullet)
        elif bullet.y > height:
            top_bullets.remove(bullet)

def draw_window(top, bottom, top_bullet, bottom_bullet, top_health, bottom_health):
    WIN.blit(SPACE, (0,0))
    top_health_text = HEALTH_FONT.render("Health: " + str(top_health), 1, WHITE)
    bottom_health_text = HEALTH_FONT.render("Health: " + str(bottom_health), 1, WHITE)
    WIN.blit(top_health_text, (width - top_health_text.get_width() - 10, 10))
    WIN.blit(bottom_health_text, (10, 10))

    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(mega_man, (bottom.x, bottom.y))
    WIN.blit(other_guy, (top.x, top.y))

    
    for bullet in top_bullet:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in bottom_bullet:
        pygame.draw.rect(WIN, YELLOW, bullet)
    pygame.display.update()

def megaman_handle_movement(keys_pressed, bottom):
    if keys_pressed[pygame.K_a] and bottom.x - VEL > 0: #LEFT
        bottom.x -= VEL
    if keys_pressed[pygame.K_d] and bottom.x + VEL + bottom.height < 700: #RIGHT
        bottom.x += VEL
    if keys_pressed[pygame.K_w] and bottom.y - VEL > BORDER.y + 10 : #UP
        bottom.y -= VEL
    if keys_pressed[pygame.K_s] and bottom.y + VEL + bottom.width < height: #DOWN
        bottom.y += VEL

def otherguy_handle_movement(keys_pressed, top):
    if keys_pressed[pygame.K_LEFT] and top.x - VEL > 0: #LEFT
        top.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and top.x + VEL + top.height < 700: #RIGHT
        top.x += VEL
    if keys_pressed[pygame.K_UP] and top.y - VEL > 0: #UP
        top.y -= VEL
    if keys_pressed[pygame.K_DOWN] and top.y + VEL < 410: #DOWN
        top.y += VEL

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1 ,WHITE)
    WIN.blit(draw_text, (width/2 - draw_text.get_width()/2, height/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)

def main():
    red = pygame.Rect(340, 200, character_width, character_height)
    yellow = pygame.Rect(340,600, character_width, character_height)
    red_bullet = []
    yellow_bullet = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullet) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullet.append(bullet)
                    FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullet) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullet.append(bullet)
                    FIRE_SOUND.play()
            if event.type == TOP_HIT:
                red_health -= 1
                HIT_SOUND.play()
            if event.type == BOTTOM_HIT:
                yellow_health -= 1
                HIT_SOUND.play()
        winner_text = ""
        if red_health <= 0:
            winner_text = "YELLOW WINNER"

        if yellow_health <= 0:
            winner_text = 'RED WINNER'

        if winner_text != "":
            draw_winner(winner_text) 
            break #WINNER
        keys_pressed = pygame.key.get_pressed()
        
        megaman_handle_movement(keys_pressed, yellow)
        otherguy_handle_movement(keys_pressed, red)
        handle_bullets(yellow_bullet, red_bullet, yellow, red)
        draw_window(red, yellow, red_bullet, yellow_bullet, red_health, yellow_health)
    main()
if __name__ == '__main__':
    main() 