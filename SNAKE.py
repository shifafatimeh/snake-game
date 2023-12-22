import pygame
from pygame .locals import QUIT, KEYDOWN, K_ESCAPE,K_UP,K_DOWN,K_LEFT,K_RIGHT
import time
def move_turns(): #FUNCTION SO WE CAN CALL WHEN WE WILL PRESS THE KEYS
    surface.fill((59, 12, 11))   #THIS LINE IS IMPORTANT AS IT WILL MOVE BLOCK ELSEWHWERE WITHOUT GETTING STICK IN THE MIDDLE
    surface.blit(block, (block_x,block_y))
    pygame.display.flip()
    
def change_dir():
    global block_x, block_y,block_direction   #changing the variable which is outside the function so we are importing it globally
    if block_direction=="up":
        block_y-= 10
        move_turns()
    elif block_direction=="down":
        block_y += 10
        move_turns()
    elif block_direction=="right":
        block_x += 10
        move_turns()
    else:
        block_direction="left"
        block_x -= 10
        move_turns() 
if __name__ == "__main__" :
    pygame.init()
    surface=pygame.display.set_mode((700,500)) #FOR DISPLAYING THE SCREEN DIMENSION
    
    surface.fill((59, 12, 11))           #FOR COLOR TO BE FILL IN SCREEN
    pygame.display.flip()                 #FOR DISPLAYING THE CHANGE
    block=pygame.image.load("resources/233.jpg").convert()           #IMPORTING IMAGE IN JPG ONLY
    block_size = (50, 50)           #DIMENSION OF IMAGE ACCORDINGLY
    block = pygame.transform.scale(block, block_size)
    block_direction="down"
    block_x=300
    block_y=200
    surface.blit(block, (block_x,block_y)) #PASTING THE IMAGE ONTO THE SCREEN
    pygame.display.flip()
    running=True
    while running:         #OUTPUT OF KEYS
        for event in pygame.event.get():
            if event.type == KEYDOWN: #ANY KEY PRESSED BY USER
                if event.key == K_ESCAPE: #IF KEY IS ESCAPE IT WILL SHUT THE PROGRAM
                    running=False
                if event.key == K_UP:
                    block_direction="up"
                if event.key == K_DOWN:
                    block_direction="down"
                if event.key == K_RIGHT:
                    block_direction="right"
                if event.key == K_LEFT:
                    block_direction="left"            
            elif event.type==QUIT:
                running=False
        change_dir()
        time.sleep(0.2)

    
