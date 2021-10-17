
import pygame 

pygame.init()


window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Bouncy ball")


clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

x = 50
y = 50

#change_x = 2
change_y = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
   # x += change_x
    y += change_y
    
    if y > 350 or y <0:
        change_y = change_y * -1
    
                
                
    
    window.fill((255,0,0))
    box = pygame.Rect(x,y,60,60)
    pygame.draw.rect(window,WHITE,box)
    
   
    clock.tick(60)
    pygame.display.update()

quit()
