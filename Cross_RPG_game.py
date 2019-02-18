#První hra
#Zobrazení objektů na screen

import pygame #podobne include v c (knihovna na hry)

SCREEN_TITUL="MOJE PRVNI RPG"
screen_width=800
screen_height=800
SCREEN_SIZE=(screen_width,screen_height)
WHITE_COLOR=(255,255,255)
BLACK_COLOR=(0,0,0)
clock=pygame.time.Clock()
#p_image=pygame.image.load("Char.png")
#p_image=pygame.transform.scale(p_image,(80,80))
class GAME:
    tick_rate=60
    def __init__(self,title,width,height):
        self.title=title
        self.width=width
        self.height=height
        
        self.game_screen=pygame.display.set_mode((width,height))
        self.game_screen.fill(WHITE_COLOR)
        pygame.display.set_caption(title)
        
    def run_game_loop(self):
        game_over=False
        direction=0

        player_character=PlayerCharacter("Char.png",375,700,50,50)
        
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over=True
                elif event.type ==pygame.KEYDOWN:#po zmačknutí
                    if event.key== pygame.K_UP:
                        direction =1
                    elif event.key==pygame.K_DOWN:
                        direction =-1
                        
                elif event.type ==pygame.KEYUP:#po uvolnění tlačítka
                    if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                        direction=0
            #pygame.draw.rect(game_screen,(51,250,0),[350,350,100,100])#vykresleni obdelniku(pozice,velikost)
            #pygame.draw.circle(game_screen,BLACK_COLOR,(400,300),50)#vykresleni kolecka (barva,pozice,radius)
            #self.game_screen.blit(p_image,(360,360))
            self.game_screen.fill(WHITE_COLOR)
            player_character.move(direction)
            player_character.draw(self.game_screen)
                
                        
            pygame.display.update()
            clock.tick(self.tick_rate)

class GameObject:
    def __init__(self,image_path,x,y,width,height):
        self.x_pos=x
        self.y_pos=y
        self.width=width
        self.height=height
        obj_image=pygame.image.load(image_path)
        self.image=pygame.transform.scale(obj_image,(width,height))
        
    def draw(self,background):
        background.blit(self.image,(self.x_pos,self.y_pos))

class PlayerCharacter(GameObject):
    speed=10

    def __init__(self,image_path,x,y,width,height):
        super().__init__(image_path,x,y,width,height)

    def move(self,direction):
        if direction >0:
            self.y_pos -=self.speed
        elif direction <0:
            self.y_pos +=self.speed
            
        


pygame.init()        

new_game=GAME(SCREEN_TITUL,screen_width,screen_height)
new_game.run_game_loop()



pygame.quit()
quit()

