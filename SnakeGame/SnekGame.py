import pygame,random
from pygame.locals import *
from sys import exit
import math


class Snake:
    def __init__(self,body , direction, color,speed):
        self.speed=speed
        self.body=body 
        self.color=color
        self.direction=self.newdirection=direction
        self.IsDead=False
    def UpdateDirection(self,game):
        self.direction=self.newdirection 
    def Update(self,game):
        #Logic for the Fading body Effect when Player Dies
        if self.IsDead:
            fadestep=5
            self.color=(max(self.color[0]-fadestep,0),max(self.color[1]-fadestep,0),max(self.color[2]-fadestep,0))
            if self.color[0]==0 and self.color[1]==0 and self.color[2]==0:
                self.color=(0,0,0)
                game.players.remove(self)
        else:
            #updates the snake...
            head=self.body[0]#head of snake
            head=(head[0]+self.direction[0],head[1]+self.direction[1])
            #wrap the snake around the window
            headx=game.HorizontalTiles if head[0]<0 else 0 if head[0]>game.HorizontalTiles else head[0]
            heady=game.VerticalTiles if head[1]<0 else 0 if head[1]>game.VerticalTiles else head[1]
            head=(headx,heady)
            #Updating the Body of the Snake and See if the Snake is Dead
            alivelist=[snake for snake in reversed(game.players) if not snake.IsDead]
            for snake in alivelist:
                if head in snake.body:
                    if head == snake.body[0]:#If Snake Collides with Body
                        snake.IsDead=True
                    self.IsDead=True
                    return
                #Logic for Eating and Collision
            if head in game.obstacles: #If the Snake Hit an Obstacle
                self.IsDead=True
                return
            elif head == game.foodpos: #If the Snake Ate a Food
                game.foodpos=0,0
                self.body.append((self.body[0]))
            
            self.body=[head]+[self.body[i-1] for i in range(1,len(self.body))]
    def Draw(self,screen,game):
        for part in self.body:
            pygame.draw.rect(screen,self.color,(part[0]*game.tilesize,part[1]*game.tilesize,game.tilesize,game.tilesize),0)
    


class HumanSnake(Snake): #Snake Controls 
    def __init__(self,body=[(0,0)] , direction=(1,0),upkey=K_UP,downkey=K_DOWN,rightkey=K_RIGHT,leftkey=K_LEFT,color=(125,255,0)): #Color ng Isnek
        super().__init__(body,direction,color,1)
        self.upkey=upkey
        self.downkey=downkey
        self.rightkey=rightkey
        self.leftkey=leftkey
        
    def processkey(self,key):
       #Checking of Directions
        if key==self.upkey:
            if self.direction != down:
                self.newdirection=up
        elif key==self.downkey:
            if self.direction != up:
                self.newdirection=down
        elif key==self.rightkey:
            if self.direction != left:
                self.newdirection=right
        elif key==self.leftkey:
            if self.direction != right:
                self.newdirection=left   

class SnakeGame:
    tilesize=15
    HorizontalTiles=20
    VerticalTiles=20
    def __init__(self):
        #Initializing the Window for the Game
        pygame.init()
        self.screen = pygame.display.set_mode(((self.HorizontalTiles+1)*self.tilesize,(self.VerticalTiles+1)*self.tilesize+25))
        pygame.display.set_caption('Isnek')
        
        #load Font and Edit Colors
        #load the font
        self.font = pygame.font.Font(None, 30)
        self.obstacles=[]
        self.obscolor=(255,0,255)
        self.foodcolor=(255,255,255)
        self.foodpos=(0,0)
        self.playercount=0

    def GenerateFood(self): #Generating Food into Random Pixels on the Screen
        if(self.foodpos == (0,0)):
            self.foodpos=random.randrange(1,self.HorizontalTiles),random.randrange(1,self.VerticalTiles)
            while (self.foodpos in self.playerpos or self.foodpos in self.obstacles):
                self.foodpos=random.randrange(1,self.HorizontalTiles),random.randrange(1,self.VerticalTiles)

    def SetObstacles(self,level):
        for i in range(1,level+1):
            lo=random.randrange(1,self.HorizontalTiles),random.randrange(1,self.VerticalTiles) #last obstacle
            self.obstacles.append(lo)
            for j in range(1,random.randint(1,int(level/2))):
                if(random.randint(1,2) == 1):
                    lo=(lo[0]+1,lo[1])
                else:
                    lo=(lo[0],lo[1]+1)
                if( 0<lo[0]<=self.HorizontalTiles and 0<lo[1]<=self.VerticalTiles ):
                    self.obstacles.append(lo)
    def setplayers(self,players):
        self.playercount+=len(players)
        self.players=players
    
    def printstatus(self): #Printing the Status of the Game
        if(len(self.players) >0):
            text = self.font.render("Press 'ESC' to Quit", 1,(255,255,255))
        else:
            text=self.font.render("Game Over",1,(255,0,0))
            pygame.quit()
        textpos = text.get_rect(centerx=self.screen.get_width()/2,y=(self.VerticalTiles+1)*self.tilesize)
        self.screen.blit(text, textpos)
    
    def UpdatePlayerInfo(self):
        #Update Player Position
        self.playerpos=[]
        for player in self.players:
            self.playerpos+=player.body

    def start(self,Difficulty): #Setting the Difficulty/Speed of the Game via changing of Ticks
        clock = pygame.time.Clock()
        count=0
        self.players.append(HumanSnake())
      
        while True:
            clock.tick(Difficulty)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    for player in self.players:
                        player.processkey(event.key)
                    if event.key == K_ESCAPE:
                        pygame.quit()
                
                    
            self.screen.fill((0,0,0))
            self.UpdatePlayerInfo()
            self.GenerateFood() #Generate food if there is no food
            for player in [a for a in self.players if not a.IsDead]:
                player.UpdateDirection(self) #Updating Game Logic
            for player in [a for a in self.players if  count%a.speed == 0]:
                player.Update(self)
            #print all the content in the screen
            for player in self.players:
                player.Draw(self.screen,self)
            for obstacle in self.obstacles:
                pygame.draw.rect(self.screen,self.obscolor,(obstacle[0]*self.tilesize,obstacle[1]*self.tilesize,self.tilesize,self.tilesize),0)
            pygame.draw.rect(self.screen,self.foodcolor,(self.foodpos[0]*self.tilesize,self.foodpos[1]*self.tilesize,self.tilesize,self.tilesize),0)
            self.printstatus()
            pygame.display.update()

left=-1,0
right=1,0
up=0,-1
down=0,1
directions=[up,down,right,left]
