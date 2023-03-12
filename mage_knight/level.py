import pygame
from tiles import Tile, StaticTile
from settings import tile_size, screen_width, screen_height
from player import Player
from support import importer_csv, import_cut_graphics

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        #self.setup_level(level_data)
        
        #Terreng
        terreng = importer_csv(level_data["terrain"])
        self.terreng_objekter = self.create_tile_group(terreng, "terrain")
        
        #Gress
        gress = importer_csv(level_data["grass"])
        self.gress_objekter = self.create_tile_group(gress, "grass")
        
        #Penger
        penger = importer_csv(level_data["coins"])
        self.penger_objekter = self.create_tile_group(penger, "coins")
        #self.penger_samlet = penger_samlet
        
        #Spiller
        spiller = importer_csv(level_data["player"])
        self.spiller = pygame.sprite.GroupSingle()
        #self.goal = pygame.sprite.GroupSingle()
        self.spiller_setup(spiller)
        
        """
        #Spiker
        spiker = importer_csv(level_data["spikes"])
        self.spiker_objekter = self.create_tile_group(spiker, "spikes")
        
        """
        
        
        #.score = 0
        #self.hent_penge = hent_penge
        
        
    
        #Spillet starter i ro
        self.world_shift = 0
        
        self.current_x = 0
    
    """
    def endre_score(self, antall):
        self.score += antall
        
    def penger_kollisjon(self):
        penger_kollidert = pygame.sprite.spritecollide(self.player.sprite, self.penger_objekter, True)
        
        if penger_kollidert:
            for penger in penger_kollidert:
            self.endre_score(1)
    """

        
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        
        for rad_nummer, rad in enumerate(layout):
            for kolonne_nummer, value in enumerate(rad):
                
                x = kolonne_nummer * tile_size
                y = rad_nummer * tile_size   
                    
                #Hvis verdien i csv-filen = "-1", betyr dette at det ikke er noe på posisjonen
                if value != "-1":
                    
                    if type == "terrain":
                        terrain_tile_list = import_cut_graphics("bilder/objekter/terrain_tiles.png")
                        tile_surface = terrain_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        
                    if type == "grass":
                        grass_tile_list = import_cut_graphics("bilder/objekter/grass.png")
                        tile_surface = grass_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        
                    if type == "coins":
                        coins_tile_list = import_cut_graphics("bilder/objekter/coin_tiles.png")
                        tile_surface = coins_tile_list[int(value)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                           
                    if type == "spikes":
                        sprite = StaticTile(tile_size, x, y, ("bilder/objekter/spikes.png"))
                    
                    
                    sprite_group.add(sprite)
                      
        return sprite_group
    
    
    def spiller_setup(self, layout):
        #sprite_group = pygame.sprite.Group()
        
        for rad_nummer, rad in enumerate(layout):
            for kolonne_nummer, value in enumerate(rad):
                x = kolonne_nummer * tile_size
                y = rad_nummer * tile_size
                if value == "0":
                    sprite = Player((x,y), self.display_surface)
                    self.spiller.add(sprite)         
    
    
    def scroll_x(self):
        spiller = self.spiller.sprite
        spiller_x = spiller.rect.centerx
        direction_x = spiller.direction.x
        
        #Sjekker spilleren sin x-posisjon og når den når denne x-posisjonen settes hans hastighet til 0, men bakgrunnen beveger seg i stedet
        #Den sjekker også om man beveger seg til høyre eller venstre
        if spiller_x < screen_width*(1/4) and direction_x < 0:
            self.world_shift = 8
            spiller.speed = 0
        elif spiller_x > screen_width*(3/4) and direction_x > 0:
            self.world_shift = -8
            spiller.speed = 0
        else:
            self.world_shift = 0
            spiller.speed = 8
            

    def horisontal_kollisjon(self):
        spiller = self.spiller.sprite
        
        spiller.rect.x += spiller.direction.x * spiller.speed
        
        #Kolliderer med terreng objekter, men ikke med pengene
        for objekt in self.terreng_objekter.sprites():
            #Sjekker om spilleren kolliderer med sprites, altså objekter i spillet
            if objekt.rect.colliderect(spiller.rect):
                #Hvis spilleren beveger seg mot venstre, treffer han den høyre delen av objektet og omvendt
                #Dette hindrer spilleren fra å gå igjennom objektet
                if spiller.direction.x < 0:
                    spiller.rect.left = objekt.rect.right
                    spiller.on_left = True
                    self.current_x = spiller.rect.left
                if spiller.direction.x > 0:
                    spiller.rect.right = objekt.rect.left
                    spiller.on_right = True
                    self.current_x = spiller.rect.right
                    
        if spiller.on_left and (spiller.rect.left < self.current_x or spiller.direction.x >= 0):
            spiller.on_left = False
        if spiller.on_right and (spiller.rect.right < self.current_x or spiller.direction.x <= 0):
            spiller.on_right = False
            
    
    def vertikal_kollisjon(self):
        spiller = self.spiller.sprite
        
        spiller.apply_gravity()
        
        for objekt in self.terreng_objekter.sprites():
            #Sjekker om spilleren kolliderer med sprites, altså objekter i spillet
            if objekt.rect.colliderect(spiller.rect):
                #Hvis spilleren beveger seg oppover, treffer den nederste del av objektet og omvendt
                #Dette hindrer spilleren fra å gå igjennom objektet
                if spiller.direction.y > 0:
                    spiller.rect.bottom = objekt.rect.top
                    spiller.direction.y = 0
                    #Vi nullstiller y-hastighet for å unngå at gravitasjonen stadig øker
                    
                    spiller.on_ground = True
                    
                elif spiller.direction.y < 0:
                    spiller.rect.top = objekt.rect.bottom
                    spiller.direction.y = 0
                    #Vi nullstiller y-hastighet for å ikke kunne "lime" seg til taket. På denne måten fungerer gravitasjonen som vanlig
                    #Vi må altså endre hastigheten fra negativ til 0 for å unngå at posisjonen låser seg
                    
                    spiller.on_ceiling = True
                    
            #Sjekker om spilleren er på bakken
            if spiller.on_ground and spiller.direction.y < 0 or spiller.direction.y > spiller.gravity:
                spiller.on_ground = False
                
            if spiller.on_ceiling and spiller.direction.y > 0:
                spiller.on_ceiling = False
                

    def run(self):
        #Lar oss skrolle spillet til sidene
        self.scroll_x()
        
        #Terreng
        self.terreng_objekter.update(self.world_shift)
        self.terreng_objekter.draw(self.display_surface)
        
        #Gress
        self.gress_objekter.update(self.world_shift)
        self.gress_objekter.draw(self.display_surface)
        
        #Penger
        self.penger_objekter.update(self.world_shift)
        self.penger_objekter.draw(self.display_surface)
        #self.penge_kollisjon()
        
        #Spiller
        self.spiller.update()
        self.spiller.draw(self.display_surface)
        #self.goal.update(self.world_shift)
        #self.goal.draw(self.display_surface)
        self.horisontal_kollisjon()
        self.vertikal_kollisjon()
        self.spiller.draw(self.display_surface)
        
        
        
        
        
        