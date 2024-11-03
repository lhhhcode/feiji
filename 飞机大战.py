import pygame
import random
import math


pygame.init()
screen=pygame.display.set_mode((800,600))
pygame.display.set_caption('飞机大战')
bgImg=pygame.image.load('bg.png')


playerImg=pygame.image.load('player.png')
playerX=350
playerY=500
playerStep=0
playerYStep=0


number_of_enemies=6
class Enemy():
    def __init__(self):
        self.img=pygame.image.load('enemy.png')
        self.x=random.randint(200,600)
        self.y=random.randint(5,150)
        self.step=random.uniform(0.5,1.5)
        self.enemies=enemies
    def disappear(self):
        for b in bullets:
            if(distance(self.x,self.y,b.x,b.y)<50):  
                enemies.remove(self)     
enemies=[]
for i in range(number_of_enemies):
    enemies.append(Enemy())
    
    
class Bullet():
    def __init__(self):
        self.img=pygame.image.load('bullet.png')
        self.x=playerX+16
        self.y=playerY+10
        self.step=2                    
bullets=[]  
    
def show_bullets():
    for b in bullets:
        screen.blit(b.img,(b.x,b.y))
        b.y-=b.step
        if b.y<0:
            bullets.remove(b)    
    
def show_enemy():
    for e in enemies:
        screen.blit(e.img,(e.x,e.y))
        e.disappear()
        e.x+=e.step
        if (e.x>736 or e.x<0):
            e.step*=-1
            e.y+=50
        if e.y>=800:
            enemies.remove(e)    
    
def move_player():
    global playerX,playerY
    playerX+=playerStep
    playerY+=playerYStep
    if playerX>736:
        playerX=736
    if playerX<0:
        playerX=0 
    if playerY>536:
        playerY=536
    if playerY<0:
        playerY=0        
    
def distance(bx,by,ex,ey):
    a=bx-ex
    b=by-ey
    return math.sqrt(a*a+b*b)
    
timer_event=pygame.USEREVENT
pygame.time.set_timer(timer_event,1000)




running=True
while running:
    screen.blit(bgImg,(0,0))
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==timer_event:
            enemies.append(Enemy())
        
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                playerStep=5
            elif event.key==pygame.K_LEFT:
                playerStep=-5
            elif event.key==pygame.K_UP:
                playerYStep=-5
            elif event.key==pygame.K_DOWN:
                playerYStep=5         
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==3:
            bullets.append(Bullet())   
                    
        if event.type==pygame.KEYUP:
            playerStep=0
            playerYStep=0
                  
    
    
    
    
    screen.blit(playerImg,(playerX,playerY))
    show_enemy()
    move_player()
    show_bullets()
   
    
    pygame.display.update()       