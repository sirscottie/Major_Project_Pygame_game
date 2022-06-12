import pygame
from tiles import Tile
from settings import tile_size, screen_width
from player import Player


#Changes all the x tikes in the settings file into interactable tiles for the player
class Level:

    def __init__(self,level_data,surface):
        #level set up 
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self,layout):
        #draws the tiles in the settings file
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            #gives the information on each row
            for col_index,cell in enumerate(row):
            #Tile placement
              if cell == 'X':
                  x = col_index * tile_size
                  y = row_index * tile_size
                  tile = Tile((x,y), tile_size)
                  self.tiles.add(tile)
            #Player placement
              if cell == 'P':
                  player_sprite = Player((x, y))
                  self.player.add(player_sprite)

    def scroll_x(self):
        """Makes the screen scroll on the left and right sides if the player reaches the end of the screen"""
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        #Checks if the player collision is happening on the left or the right
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom

    def run(self):
        #Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        #Player
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.player.draw(self.display_surface)






