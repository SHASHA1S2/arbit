
# coded by Rishabh Nigam

import os, random, sys, math
import pygame
from pygame.locals import *
arrsensor=[0]*8

hypothesis =[]
for i in xrange(4):
	 hypothesis.append([])
	 for j in xrange(8):   
		hypothesis[i].append(0)

key=0
board =[]
for i in xrange(61):
	 board.append([])
	 for j in xrange(61):     # board to store
		board[i].append(0)

arrsensors=[0]*8     # sensor values
gameClock = pygame.time.Clock() 
temp=[]
for i in xrange(61):
	 temp.append([])
	 for j in xrange(61):     # board to store
		temp[i].append(0)
area=[0]*4	
def hypoinit():
	hypothesis[0][0]=1
	hypothesis[1][2]=1
	hypothesis[2][4]=1
	hypothesis[3][6]=1

hypoinit()

def findarea( x, y):
	c=0
	if temp[x][y+1]==0 :
		c=c+1
		temp[x][y+1]=1
					c=c+findarea(x,y+1)
	if temp[x][y-1]==0 :
		c=c+1
		temp[x][y-1]=1
		c=c+findarea(x,y-1)
	if temp[x+1][y]==0 :
		c=c+1
		temp[x+1][y]=1
		c=c+findarea(x+1,y)
	if temp[x-1][y]==0 :
		c=c+1
		temp[x-1][y]=1
		c=c+findarea(x-1,y)
	return c
	

def keyarea( x,  y):
	for i in range(0,61):
		for j in range(0,61):
			if board[i][j]!=0 :
				temp[i][j]=1
			else:
				temp[i][j]=0
	temp[x][y]=1
	temp[x][y+1]=1
	area[0]=findarea(x,y+1)
	for i in range(0,61):
		for j in range(0,61):
			if board[i][j]!=0 :
				temp[i][j]=1
			else:
				temp[i][j]=0
	temp[x][y]=1
	temp[x-1][y]=1
	area[1]=findarea(x-1,y)
# area for left
	for i in range(0,61):
		for j in range(0,61):
			if board[i][j]!=0 :
				temp[i][j]=1
			else:
				temp[i][j]=0
	temp[x][y]=1
	temp[x][y-1]=1
	area[2]=findarea(x,y-1)
# area for bottom
	for i in range(0,61):
		for j in range(0,61):
			if board[i][j]!=0 :
				temp[i][j]=1
			else:
				temp[i][j]=0
	temp[x][y]=1
	temp[x+1][y]=1
	area[3]=findarea(x,y+1)
	m=area[0] 
	index=0
	for i in range (1,4):
		if area[i]>m:
			index=i
			m=area[i]

	return index
def printboard():
	for i in range(61):
		for j in range(61):
			print board[i][j],
		print

def update(a,b):
	board[a[1]/10][a[0]/10]=b
	
	
def resetboard():
	for i in range(61):
		for j in range(61):
			board[i][j]=0	

def sensorvalue(x,y):
	x1,y1=x,y
	direction=0
	while direction<8:
		x,y=x1,y1			
		for i in range (61):			
			if direction==0:
				x=x+1	
				#print x,y					
			elif direction==1:
				x=x+1
				y=y+1
				#print x,y	
			elif direction==2:
				y=y+1
				#print x,y	
			elif direction==3:
				x=x-1
				y=y+1
				#print x,y	
			elif direction==4:
				x=x-1
				#print x,y	
			elif direction==5:
				x=x-1
				y=y-1
				#print x,y	
			elif direction==6:
				y=y-1
				#print x,y	
			elif direction==7:
				x=x+1
				y=y-1
				#print x,y	
			if x>60 or x<-1:
				break
			if y>60 or y<-1:
				break					
			if board[y][x]==1 or board[y][x]==2:
				break
		arrsensor[direction]=i+1
		direction+=1
def printsens(a):
	for i in range (8):
		print a[i],
	print

def evaluate(hyp,sens):
	maximum=0	
	for i in range(4):
		c=0
		for j in range(8):
			c=c+hyp[i][j]*sens[j]
		print c,		
		if c>maximum:
			maximum,key=c,i
	print
	return key


#Player 1 Class
class Snake(object):

        def __init__(self):
                self.pos = [400, 300] 
                self.body = []        
                self.angle = 0        
                self.alive = True     
          	update(self.pos,1)         

        def update(self):

                #Insert the new position of the snake's head
                self.body.insert(0, list(self.pos))
		update(self.pos,1)         


                #Move 10 pixels according to the angle
                if self.angle == 0:
                        self.pos[1] -=10 
                if self.angle == 90:
                        self.pos[0] -=10 
                if self.angle == 180:
                        self.pos[1] +=10
                if self.angle == 270:
                        self.pos[0] +=10
                #If your head ran into your body, die!
                for b in self.body:
                       if self.pos == b:
                                self.alive = False

                #If your body is not in the 600x600 screen area, die!
                if self.pos[0] not in range(600):
                        self.alive = False
                if self.pos[1] not in range(600):
                        self.alive = False

        def draw(self, surf):

                #Draw the head
                surf.fill((0, 0, 255), (self.pos[0], self.pos[1], 10, 10))

                #Draw the body
                for b in self.body:
                        surf.fill((0, 0, 255), (b[0], b[1], 10, 10))

#Snake Class
class Snake2(object):

	def __init__(self):
                self.pos = [200, 300] 
                self.body = []       
                self.angle = 0        
                self.alive = True     
        	update(self.pos,2)         

           
	def update(self):
                self.body.insert(0, list(self.pos))
		update(self.pos,2)         
		
                #Move 16 pixels according to the angle
                if self.angle == 0:
                        self.pos[1] -= 10
                if self.angle == 90:
                        self.pos[0] -= 10
                if self.angle == 180:
                        self.pos[1] += 10
                if self.angle == 270:
                        self.pos[0] += 10
                #If your head ran into your body, die!
                for b in self.body:
                       if self.pos == b:
                              self.alive = False

                #If your body is not in the 600x600 screen area, die!
                if self.pos[0] not in range(600):
                        self.alive = False
                if self.pos[1] not in range(600):
                        self.alive = False

        def draw(self, surf):
               surf.fill((255, 0, 0), (self.pos[0], self.pos[1], 10, 10))
               for b in self.body:
                        surf.fill((255, 0, 0), (b[0], b[1], 10, 10))
                        


	
		
def dist(x1,y1,x2,y2):
        dx = x2 - x1
        dy = y2 - y1
        dsquared = dx**2 + dy**2
        result = math.sqrt(dsquared)
        return result
        

def main():
    
        #Call the SDL arg to center the window when it's inited, and then init pygame
        os.environ["SDL_VIDEO_CENTERED"] = "1"
        pygame.init()


        #Set up the pygame window
        pygame.display.set_caption("TRON 2")
        screen = pygame.display.set_mode((600, 600))
	
	
	snake = Snake()
        snake2= Snake2()  # 20,30 & 40,30
        
        #Instantiate multiple font types
        font = pygame.font.Font(None, 32)
        defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
        hugeFont= pygame.font.Font( pygame.font.get_default_font(), 30)
	smallFont= pygame.font.Font( pygame.font.get_default_font(), 25)

        #Score variables
        score1 =0
        score2 =0

        #Total time passed in the game
        totaltime = 0

	screen.fill((0,0,0))                
	for i in range(0,600,10):
	  pygame.draw.line(screen,(81,81,81),(i,0),(i,600),1)
	for i in range(3,600,10):
	  pygame.draw.line(screen,(81,81,81),(0,i),(600,i),1)
	
        snake.draw(screen)
        snake2.draw(screen)

        gamebegintext = smallFont.render("Press any key to continue......", 1, (0,255,0))
        screen.blit(gamebegintext, (screen.get_width()/2-200, screen.get_height()/2))
	pygame.display.flip()
                
	pygame.event.clear()
	pygame.event.wait()
	
	
	
	#printboard()
        while 1:
                #Total time accrued
                gameClock.tick()
                totaltime += gameClock.get_time()
              
         
                #Get the key input from pygame's event module
                for e in pygame.event.get():

                        #QUIT is the big red X button on the window bar
                        if e.type == QUIT:
                                pygame.quit()
                                return

                        #Check if a key was pressed
                        if e.type == KEYDOWN:

                                #Quit if the Escape key is pressed
                                if e.key == K_ESCAPE:
                                        pygame.quit()
                                        return
				if e.key ==K_SPACE:
					pygame.time.wait(50000)
                                #Change the snake's angle if the arrow keys are pressed
                                if e.key == K_UP:
				  if(not(snake.angle==180)):
                                        snake.angle = 0
                                        
                                if e.key == K_LEFT:
				  if(not(snake.angle==270)):
                                        snake.angle = 90
                                        
                                if e.key == K_DOWN:
				  if(not(snake.angle==0)):
                                        snake.angle = 180
                                        
                                if e.key == K_RIGHT:
				  if(not(snake.angle==90)):
                                        snake.angle = 270
                                        


                                #Player 2 keys               
                sensorvalue(snake2.pos[0]/10,snake2.pos[1]/10)
		key=keyarea(snake2.pos[0]/10,snake2.pos[1]/10)
		
		print key
		if key==0:
			 snake2.angle=270
		if key==1:
			 snake2.angle=180		
		if key==2:
			 snake2.angle=90	
		if key==3:
			 snake2.angle=0

                #call the snakes update function
                snake.update()
                snake2.update()

		        


                        
                #Collision Detection for the Snakes!
                for b in snake.body:
                        if snake2.pos == b:
                                snake2.alive = False

                for b in snake2.body:
                        if snake.pos == b:
                                snake.alive = False



                #If the snake died, draw text that says you died, and reinit the snake , reset variables.
                if not snake.alive:
                        score2+=1 
			

                        #If snake 2 has 10 points-- give winning screen
                        if score2== 10:
                                 gameovertext = hugeFont.render("Player 2 WINS!", 1, (0,255,0))
                                 screen.blit(gameovertext, (screen.get_width()/2-200, screen.get_height()/2))
                                 pygame.display.flip()
                                 pygame.time.wait(2000)
                                 score1=0
                                 score2=0
                                 snake = Snake()
                                 snake2= Snake2()
                                 totaltime= 0
                                 
                        
                        else:
                                gameovertext = hugeFont.render("Player 1 has died", 1, (0,255,0))
                                screen.blit(gameovertext, (screen.get_width()/2-200, screen.get_height()/2))
                                pygame.display.flip()
                                pygame.time.wait(1000)
				sensorvalue(snake2.pos[0]/10,snake2.pos[1]/10)
                                printsens(arrsensor)
				#printboard()
				resetboard()
				snake = Snake()
                                snake2 = Snake2()
                                totaltime=0
				
			pygame.event.clear()
			pygame.event.wait()

                if not snake2.alive:
                        score1+=1
			

                        #If snake 1 has 10 points-- give winning screen
                        if score1== 10:
                                 gameovertext = hugeFont.render("Player 1 WINS!", 1, (0,255,0))
                                 screen.blit(gameovertext, (screen.get_width()/2-200, screen.get_height()/2))
                                 pygame.display.flip()
                                 pygame.time.wait(2000)
                                 score1=0
                                 score2=0
                                 snake = Snake()
                                 snake2= Snake2()
                                 totaltime=0
                        
                        else:
                                gameovertext = hugeFont.render("Player 2 has died", 1, (0,255,0))
                                screen.blit(gameovertext, (screen.get_width()/2-200, screen.get_height()/2))
                                pygame.display.flip()
                                pygame.time.wait(1000)
                                sensorvalue(snake2.pos[0]/10,snake2.pos[1]/10)
				printsens(arrsensor)
				#printboard()
        			resetboard()
				snake = Snake()
                                snake2= Snake2()
                                totaltime=0
				
				pygame.event.clear()
			pygame.event.wait()

                #Draw everything!

                screen.fill((0,0,0))
                for i in range(0,600,10):
		  pygame.draw.line(screen,(81,81,81),(i,0),(i,600),1)
		for i in range(0,600,10):
		  pygame.draw.line(screen,(81,81,81),(0,i),(600,i),1)
 
                snake.draw(screen)
                snake2.draw(screen)
                        
                pygame.display.flip()

                #Wait 100 milliseconds every frame. This keeps things from going a million miles per hour!
                pygame.time.wait(100)

#Run if executeed
if __name__ == "__main__":
    main()
