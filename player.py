import pygame


class Player(pygame.sprite.Sprite):
   def __init__(self, pos):
       super().__init__()
       #draws the player image qith the rect
       #note to self, resize the image for better viewing
       img = pygame.image.load('idlea.png')
       self.image = img
       self.rect = self.image.get_rect(topleft = pos)


       #player movement
       self.direction = pygame.math.Vector2(0,0)
       # connects one point to another, alot like the line function in processing
       self.speed = 8
       self.gravity = 0.8
       #negative so the player jumps up
       self.jump_height = -10






   def get_input(self):
      """character movement"""

      #arrow keys
      keys = pygame.key.get_pressed()
      if keys[pygame.K_RIGHT]:
        self.direction.x = 1
      elif keys[pygame.K_LEFT]:
        self.direction.x = -1
      else:
        self.direction.x = 0
          
      if keys[pygame.K_UP]:
          self.jump()

   def apply_gravity(self):
       self.direction.y += self.gravity
       self.rect.y += self.direction.y


   def jump(self):
       self.direction.y = self.jump_height

   def update(self):
       self.get_input()



