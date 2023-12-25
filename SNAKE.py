import pygame
from pygame .locals import QUIT, KEYDOWN, K_ESCAPE,K_UP,K_DOWN,K_LEFT,K_RIGHT,K_RETURN
import time
import random
Size=50



class Apple:
    def __init__(self,parent_screen):
        self.parent_screen=parent_screen
        self.app=pygame.image.load("resources/pngegg (6).png").convert() 
        self.app_size = (50, 50)                                              #DIMENSION OF IMAGE ACCORDINGLY
        self.app = pygame.transform.scale(self.app, self.app_size)
        self.app_x= Size*3
        self.app_y= Size*3



    def draw_apple(self):
        self.parent_screen.blit(self.app,(self.app_x,self.app_y))
        pygame.display.flip()



    def move(self):
        self.app_x=random.randint(1,27)*Size
        self.app_y=random.randint(1,15)*Size




class Snake:  

    def __init__ (self,parent_screen,lenght):
        self.parent_screen=parent_screen
        self.lenght=lenght
        self.block=pygame.image.load("resources/233.jpg").convert()             #IMPORTING IMAGE IN JPG ONLY
        self.block_size = (50, 50)                                              #DIMENSION OF IMAGE ACCORDINGLY
        self.block = pygame.transform.scale(self.block, self.block_size)
        self.block_x=[Size]*lenght
        self.block_y=[Size]*lenght
        self.block_direction="down"
        

    def increase_len(self):
        self.lenght=self.lenght+1
        self.block_x.append(-1)
        self.block_y.append(-1)
       
    
        

        



    def snake_changes(self):
        for i in range(self.lenght):

            self.parent_screen.blit(self.block, (self.block_x[i],self.block_y[i]))
        pygame.display.flip()




    def Snake_up(self):
        self.block_direction="up"


    def Snake_down(self):
        self.block_direction="down"


    def Snake_right(self): 
        self.block_direction="right"

    def Snake_left(self):      
        self.block_direction="left"
    

    def walk(self):
        for i in range(self.lenght-1,0,-1):
            self.block_x[i]=self.block_x[ i - 1 ]
            self.block_y[i]=self.block_y[ i - 1 ]
        if self.block_direction=="up":
            self.block_y[0]-=50
        if self.block_direction=="down":
            self.block_y[0]+=50
        if self.block_direction=="right":
            self.block_x[0]+=50
        if self.block_direction=="left":
            self.block_x[0]-=50
        self.snake_changes()

    
    


    
class Game():
    def __init__ (self):
        pygame.init()
        pygame.mixer.init()
        self.background_music()
        self.surface=pygame.display.set_mode((1400,800))                #FOR DISPLAYING THE SCREEN DIMENSION
        self.snake=Snake(self.surface,1)
        self.snake.snake_changes()   
        self.apple=Apple(self.surface) 
        self.apple.draw_apple()
        


    def bac_grass(self):
        self.fake_grass=pygame.image.load("resources/fake.jpg")
        self.surface.blit(self.fake_grass,(0,0))
        

    def background_music(self):
        pygame.mixer.music.load("resources/happy.mp3")
        pygame.mixer.music.play()
    
    def reset(self):
        self.snake=Snake(self.surface,1)
        self.apple=Apple(self.surface)


    def collision(self,x1,y1,x2,y2):
        if y1>=y2 and y1<y2+Size:
            if x1>=x2 and x1<x2+Size:
            
                return True
        return False

    def score(self):
        self.paste=pygame.font.SysFont("arial",58,bold=True)
        self.sco=self.paste.render(f"SCORE : {self.snake.lenght}",True,(255,255,0))
        self.surface.blit(self.sco,(1100,10))


    def show_game_over(self):
        self.bac_grass()
        self.quit=pygame.font.SysFont("arial",30,bold=True)
        self.quitpaste=self.quit.render(f"GAME OVER AND YOUR SCORE IS  :  {self.snake.lenght}",True,(232, 237, 81))
        self.surface.blit(self.quitpaste,(40,300))
        self.quitmore=self.quit.render(f"IF WANT TO PLAY AGAIN PRESS THE ENTER KEY AND FOR QUIT PREE ESC ! ",True,(232, 237, 81))
        self.surface.blit(self.quitmore,(40,350))
        pygame.mixer.music.pause()
        pygame.display.flip()
        
    def show_well_played(self):
        self.bac_grass()
        self.quit=pygame.font.SysFont("arial",30,bold=True)
        self.quitpaste=self.quit.render(f"YOU MADE THE HIGHEST SCORE : {self.snake.lenght}",True,(232, 237, 81))
        self.surface.blit(self.quitpaste,(40,300))
        pygame.display.flip()
        pygame.time.delay(5000)
        raise"again"
        


    def sound_meet(self,many):
        s1=pygame.mixer.Sound(f"resources/{many}.mp3")
        pygame.mixer.Sound.play(s1)

    def play(self):
        self.bac_grass()
        self.snake.walk()
        self.apple.draw_apple()
        self.score()
        pygame.display.flip()


        if self.collision(self.snake.block_x[0],self.snake.block_y[0],self.apple.app_x,self.apple.app_y):
            self.sound_meet("Tada")
            self.snake.increase_len()
            self.apple.move()

        for i in range(1,self.snake.lenght):
            if self.collision(self.snake.block_x[0],self.snake.block_y[0],self.snake.block_x[i],self.snake.block_y[i]):
                self.sound_meet("glitc")
                raise"game_over"
            

        if not (0 <= self.snake.block_x[0] <= 1400 and 0 <= self.snake.block_y[0] <= 750):
                self.sound_meet("glitc")
                raise "Hit the boundry error"



    def snake_run(self):
        running=True
        pause=False
        well_played=False
        while running:         #OUTPUT OF KEYS
            for event in pygame.event.get():
                if event.type == KEYDOWN:        #ANY KEY PRESSED BY USER
                    if event.key == K_ESCAPE:    #IF KEY IS ESCAPE IT WILL SHUT THE PROGRAM
                        running=False
                    if event.key == K_RETURN:
                        pygame.mixer.music.unpause()
                        pause=False
                    if pause==False:
                        if event.key == K_UP:
                            self.snake.Snake_up()
                        if event.key == K_DOWN:
                            self.snake.Snake_down()
                        if event.key == K_RIGHT:
                            self.snake.Snake_right()
                        if event.key == K_LEFT:
                            self.snake.Snake_left()           
                elif event.type==QUIT:
                    running=False
            try:
                if pause==False:
                    self.play() 
                    if self.snake.lenght > 20:
                        well_played = True
                        self.show_well_played()
                        
                        
            except Exception as e:
                self.show_game_over()
                pause=True
                self.reset()
            if self.snake.lenght>0 and self.snake.lenght<=5:
                pygame.time.delay(300)
            elif self.snake.lenght>5 and self.snake.lenght<=10:
                pygame.time.delay(200)
            elif self.snake.lenght>10 and self.snake.lenght<=20:
                pygame.time.delay(100)
            else:
                pygame.time.delay(50)
               

if __name__ == "__main__" :
    game=Game()
    game.snake_run()

   

    
