import pygame
from os import walk
from csv import reader
from settings import tile_size

def hent_mappe(path):
    surface_list = []
    
    for _, __, bilder in walk(path):
        for bilde in bilder:
            vei_til_mappe = path + "/" + bilde
            image_surface = pygame.image.load(vei_til_mappe).convert_alpha()
            surface_list.append(image_surface)
        
              
    return surface_list


#Funksjon for å importere csv filer fra Tiled
def import_csv_layout(path):
    terreng_kart = []
    with open(path) as kart:
        level = reader(kart, delimiter = ",")
        for row in level:
            #Lager en liste med hele kartet, med hver rad
            terreng_kart.append(list(row))
            
        return terreng_kart
    
#"Plukker" opp biter av grafikken som er av størrelse tile_size
def import_cut_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_number_x = int(surface.get_size()[0] / tile_size)
    tile_number_y = int(surface.get_size()[1] / tile_size)
    
    cut_tiles = []
    for rad in range(tile_number_y):
        for kolonne in range(tile_number_x):
            x = kolonne * tile_size
            y = rad * tile_size                                          #Gjør at ubrukt plass bak objektene ikke fylles med svart, men blir usynlig
            new_surface = pygame.Surface((tile_size, tile_size), flags = pygame.SRCALPHA)
            new_surface.blit(surface, (0, 0), pygame.Rect(x, y, tile_size, tile_size))
            cut_tiles.append(new_surface)
            
    return cut_tiles
    