import pygame
from support import hent_mappe
from settings import screen_width, screen_height, tile_size


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface):
        super().__init__()
        self.hent_karakter()
        self.frame_index = 0
        self.animasjon_hastighet = 0.15 #Hvor ofte animasjoner skal oppdateres
        self.image = self.animasjoner["idle"][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos)
        
        #Todimensjonal vektor fra pygame
        self.direction = pygame.math.Vector2()
        self.speed = 6
        self.gravity = 0.981
        self.jump_speed = -18
        
        #Spiller status
        self.status = "idle"
        self.retning_høyre = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        
        self.font_size = 64
        self.font = pygame.font.Font("font/pixel_font.ttf" , self.font_size)
        self.TEKST_FARGE = "red"
        
        #Skjermen
        self.screen = pygame.display.set_mode((screen_width, screen_height))
    
    
    def hent_karakter(self):
        karakter_mappe = "bilder/karakterer/trollmann/"
        self.animasjoner = {"idle":[], "run":[], "jump":[]}
        
        for animasjon in self.animasjoner.keys():
            vei_til_mappe = karakter_mappe + animasjon
            self.animasjoner[animasjon] = hent_mappe(vei_til_mappe)
            
        
    def animer(self):
        animasjon = self.animasjoner[self.status]
        
        self.frame_index += self.animasjon_hastighet
        
        #Gjentar animasjoner etter at vi har gått igjennom alle animasjonene i mappen
        if self.frame_index >= len(animasjon):
            self.frame_index = 0
            
        image = animasjon[int(self.frame_index)]
        
        if self.retning_høyre == True:
            self.image = image
        
        #Hvis man snur retning
        else:
            flipped_image = pygame.transform.flip(image, True, False)
                                                 #(bildet, snu om x-akse, snu om y-akse)
            self.image = flipped_image
        
        
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        if self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        

            
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.retning_høyre = True
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.retning_høyre = False
        else:
            self.direction.x = 0
            
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.on_ground:
            self.jump()
            
    #Finner ut hvordan spilleren beveger seg
    def get_status(self):
        if self.direction.y < 0:
            self.status = "jump"
        
        #Siden vår metode vertikal kollisjon oppdaterer y-posisjonen etter at gravitasjonen har dratt den ned 0.8 i y retning, må vi skrive at y-retningen må være større enn 0.8
        elif self.direction.y > self.gravity:
            self.status = "idle"
        
        else:
            if self.direction.x != 0:
                self.status = "run"
            else:
                self.status = "idle"
        
    def tegnTekst(self,tekst, font, tekst_farge):
        tekst = self.font.render(tekst, True, tekst_farge)
        tekst_rect = tekst.get_rect(center = (screen_width, screen_height))
        screen.blit(tekst, tekst_rect)
    
    
    def gameOver(self):
        #Sjekker om spilleren er under skjermen. I så fall er det gameOver
        if self.rect.y > screen_height:
            #print("Prøv igjen")
            #self.gameOver = True
            pygame.mixer.music.stop()
            self.screen.fill("black")
            global game_over
            game_over = True
            
            
        
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        
    def jump(self):
        self.direction.y = self.jump_speed
        
    
    def update(self):
        self.get_input()
        self.get_status()
        self.animer()
        self.gameOver()
        

        
        
        