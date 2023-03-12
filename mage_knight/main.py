import pygame, sys, os
from settings import *
from tiles import Tile
from level import Level
from game_data import level_0
import knapp
from pygame.locals import *
from player import Player

pygame.display.set_caption("Mage Knight")


pygame.init()


#Initialiserer musikken
pygame.mixer.init()
#Henter musikken
pygame.mixer.music.load("lyd/meny.wav")
#Looper musikken
pygame.mixer.music.play(-1)


#Bakgrunn
bakgrunnsbilde = pygame.image.load("bilder/bakgrunn/meny.png")
bakgrunnsbilde = pygame.transform.scale(bakgrunnsbilde, (screen_width, screen_height))


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()



#level = Level(level_map, screen)
level = Level(level_0, screen)

pause = False

# Variabel som styrer om spillet skal kjøres
run = True

spill = False

# Variabel som styrer om spillet er ferdig
#gameOver = False


#Tekst
font_size = 32
font = pygame.font.Font("font/pixel_font.ttf" , font_size)
TEKST_FARGE = "red"

resume_bilde = pygame.image.load("bilder/knapper/resume.png").convert_alpha()
#resume_rektangel = resume_bilde.get_rect()
resume_knapp = knapp.Button(screen_width//2 - (191//2), screen_height//2 - (82), resume_bilde, 1)

quit_bilde = pygame.image.load("bilder/knapper/quit.png").convert_alpha()
quit_knapp = knapp.Button(screen_width//2 - (128//2), screen_height//2, quit_bilde, 1)

def tegnTekst(tekst, font, tekst_farge, senter):
    tekst = font.render(tekst, True, tekst_farge)
    tekst_rect = tekst.get_rect(center = (screen_width//2, screen_height//2))
    screen.blit(tekst, tekst_rect)
    #screen.blit(tekst, (x,y))
    
     

# Spill-løkken
while run:
    # Fyller skjermen med et bakrunnsbilde
    screen.blit(bakgrunnsbilde, (0,0))
    if spill == True:
        screen.fill("purple")
        level.run()
    else:
        tegnTekst("Trykk ENTER!", font, TEKST_FARGE, (screen_width//2, screen_height//2))
    
    # Går gjennom hendelser (events)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                #Starter musikken hvis man trykker enter
                pygame.mixer.music.load("lyd/spill.wav")
                pygame.mixer.music.play(-1)
                spill = True
                
            if event.key == pygame.K_ESCAPE:
                #Stopper musikken hvis man tar på pause
                pygame.mixer.music.stop()
                pause = True
                
                
    #Hva som skjer hvis man har trykket ESCAPE, altså pause
    if pause == True:
        screen.fill("black")
        if resume_knapp.draw(screen):
            pygame.mixer.music.load("lyd/spill.wav")
            pygame.mixer.music.play(-1)
            pause = False
        elif quit_knapp.draw(screen):
            run = False
                
    # Sjekker om vi ønsker å lukke vinduet
    if event.type == pygame.QUIT:
        run = False # Spillet skal avsluttes
            
    #if not gameOver:
        #level.run()
        
    

    
    pygame.display.update()
    clock.tick(60)
    
# Avslutter pygame
pygame.quit()
#sys.exit()
