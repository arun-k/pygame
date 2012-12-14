import pygame
import random
from pygame.locals import *
    
screen=pygame.display.set_mode((400,400))
#screen.fill((40,70,30))
alive=(0,0,255)
dead=(0,0,0)
grid={}
for i in range(0,40):
    for j in range(0,40):
        grid[(i*10,j*10)]=0
for i in range(0,800):
    x=random.randrange(0,39)
    y=random.randrange(0,39)
    pygame.draw.rect(screen,alive,[x*10,y*10,10,10])
    grid[(x*10,y*10)]=1
running=1

def neighbours(x,y):
    counter=0
    if x!=0 and y!=0 and grid[(x-10,y-10)]:
        counter+=1
    if x!=0 and grid[(x-10,y)]:
        counter+=1
    if x!=0 and y<390 and grid[(x-10,y+10)]:
        counter+=1
    if y!=0 and grid[(x,y-10)]:
        counter+=1
    if y<390 and grid[(x,y+10)]:
        counter+=1
    if x<390 and y!=0 and grid[(x+10,y-10)]:
        counter+=1
    if x<390 and grid[(x+10,y)]:
        counter+=1
    if x<390 and y<390 and grid[(x+10,y+10)]:
        counter+=1
    return counter
def change(point_list):
    for point in point_list:
        if grid[point]:
            pygame.draw.rect(screen,dead,[point[0],point[1],10,10])
            grid[point]=0
        else:
            pygame.draw.rect(screen,alive,[point[0],point[1],10,10])
            grid[point]=1
while running:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        running=0
    #screen.fill((40,70,30))
    update=[]
    for x in range(0,40):
        for y in range(0,40):
            if grid[(x*10,y*10)]:
                if neighbours(x*10,y*10)<2 or neighbours(x*10,y*10)>3:
                    update.append((x*10,y*10))
            else:
                if neighbours(x*10,y*10)==3:
                    update.append((x*10,y*10))
    change(update)
    pygame.display.flip()
