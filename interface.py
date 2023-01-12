import random
import pygame
import sprite_movement
import unlock_sprite
import main
import collisions

win = pygame.display.set_mode((1375,758))

dice_images = [pygame.image.load('1.png'),pygame.image.load('2.png'),pygame.image.load('3.png'),
               pygame.image.load('4.png'),pygame.image.load('5.png'),pygame.image.load('6.png')]
turn_list=['player1','player2','player3','player4']
turn_sprites = [pygame.image.load('Blue Turn.png'),pygame.image.load('Yellow Turn.png'), pygame.image.load('Green Turn.png'),pygame.image.load('Red Turn.png')]
pawn_sprites = [pygame.image.load('Red.png'), pygame.image.load('Blue.png'), pygame.image.load('Yellow.png'), pygame.image.load('Green.png')]
bg = pygame.image.load('Background.png')
img = pygame.image.load('Game Logo.png')
pygame.display.set_caption('LUDO')
pygame.display.set_icon(img)
clock = pygame.time.Clock()

class Players():
    
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.og_x = x
        self.og_y = y        
        self.width = width
        self.height = height
        self.unlock = False
        self.step = -1
        self.check_home = -1
    
    def draw_blue(self, win):
        win.blit(pawn_sprites[1],(self.x,self.y))
    def draw_yellow(self,win):
        win.blit(pawn_sprites[2],(self.x,self.y))
    def draw_red(self,win):
        win.blit(pawn_sprites[0],(self.x,self.y))
    def draw_green(self,win):
        win.blit(pawn_sprites[3],(self.x,self.y))
        
    def unlocked_blue(self):
        self.x = 91-(39//2)
        self.y = 332-(64//2)
    def unlocked_yellow(self):
        self.x = 428-(39//2)
        self.y = 94-(64//2)
    def unlocked_green(self):
        self.x = 666-(39//2)
        self.y = 426-(64//2)
    def unlocked_red(self):
        self.x = 330-(39//2)
        self.y = 666-(64//2)
        
    def locked(self):
        self.x = self.og_x
        self.y = self.og_y  
        
    def map_blue(self, movespace):
        self.check_home += movespace
        if self.check_home >=57:
            self.check_home -= movespace
        else:  
            self.step += movespace
            self.x = sprite_movement.map_blue[self.step][0] - (39//2)
            self.y = sprite_movement.map_blue[self.step][1] - (64//2)
    
    def map_yellow(self, movespace):
        self.check_home += movespace
        if self.check_home >=57:
            self.check_home -= movespace
        else:  
            self.step += movespace
            self.x = sprite_movement.map_yellow[self.step][0] - (39//2)
            self.y = sprite_movement.map_yellow[self.step][1] - (64//2)
            
    def map_green(self, movespace):
        self.check_home += movespace
        if self.check_home >=57:
            self.check_home -= movespace
        else:  
            self.step += movespace
            self.x = sprite_movement.map_green[self.step][0] - (39//2)
            self.y = sprite_movement.map_green[self.step][1] - (64//2)
            
    def map_red(self, movespace):
        self.check_home += movespace
        if self.check_home >=57:
            self.check_home -= movespace
        else:  
            self.step += movespace
            self.x = sprite_movement.map_red[self.step][0] - (39//2)
            self.y = sprite_movement.map_red[self.step][1] - (64//2)
        
        
    
def redrawGameWindow(num, face_number):
    win.blit(turn_sprites[num],(759,0))
    win.blit(dice_images[face_number],(759+250,383))
    win.blit(bg,(0,0))
    player1_a.draw_blue(win)
    player1_b.draw_blue(win)
    player1_c.draw_blue(win)
    player1_d.draw_blue(win)
    player2_a.draw_yellow(win)
    player2_b.draw_yellow(win)
    player2_c.draw_yellow(win)
    player2_d.draw_yellow(win)
    player3_a.draw_red(win)
    player3_b.draw_red(win)
    player3_c.draw_red(win)
    player3_d.draw_red(win)
    player4_a.draw_green(win)
    player4_b.draw_green(win)
    player4_c.draw_green(win)
    player4_d.draw_green(win)
    pygame.display.update()

#Mainloop
run = True

player1_a = Players(101-(39//2), 158-(64//2), 39, 64)
player1_b = Players(162-(39//2), 104-(64//2), 39, 64)
player1_c = Players(220-(39//2), 158-(64//2), 39, 64)
player1_d = Players(163-(39//2), 220-(64//2), 39, 64)
player2_a = Players(596-(39//2), 102-(64//2), 39, 64)
player2_b = Players(534-(39//2), 166-(64//2), 39, 64)
player2_c = Players(595-(39//2), 223-(64//2), 39, 64)
player2_d = Players(651-(39//2), 165-(64//2), 39, 64)
player3_a = Players(167-(39//2), 535-(64//2), 39, 64)
player3_b = Players(103-(39//2), 592-(64//2), 39, 64)
player3_c = Players(167-(39//2), 654-(64//2), 39, 64)
player3_d = Players(220-(39//2), 594-(64//2), 39, 64)
player4_a = Players(590-(39//2), 534-(64//2), 39, 64)
player4_b = Players(532-(39//2), 596-(64//2), 39, 64)
player4_c = Players(591-(39//2), 653-(64//2), 39, 64)
player4_d = Players(652-(39//2), 597-(64//2), 39, 64)
i=0
while run:
    click = True
    if i>3:
        i=0
    clock.tick(100)
    face_num = random.randint(0,5)
    number = face_num+1
    redrawGameWindow(i,face_num)
    if number==6 or number==1:
        unlock_sprite.unlock(turn_list[i])
    else:
        main.diceroll_step(number, turn_list[i])
    collisions.lock_case(turn_player=turn_list[i])
    i+=1
    
pygame.quit()
 