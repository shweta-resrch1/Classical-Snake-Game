import pygame
import sys
import random
import time
pygame.init()
screen_width=500
screen_height=500
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Classical Snake Game")
white=(255,255,255)
black=(0,0,0)
play=True
box_x=50#snake coordinates
box_y=50# snake coordinates
speed_x=0#snake speed
speed_y=0#snake speed
box_block=10# width and height of snake
food_p=0# for food position
food_x=100
food_y=100
collision_count=0
box_count=1
snake_list=[]
replay=True# for restart the loop
def restart():
    global replay
    global play
    global box_x
    global box_y
    global box_count
    
    box_count=0
    
    box_x=50
    box_y=50
    white=(255,255,255)
    while replay:
        font=pygame.font.SysFont("Times New Roman",30)
        text=font.render("To Play again Press Space Key",white,True)
        screen.fill((100,100,100))
        screen.blit(text,(50,200))
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    print("Let call")
                    play_again(True)
                    
                    pygame.display.update()
        pygame.display.update()
            
        
    

def inside(snake_x,snake_y):
    global play
    if snake_x>=screen_width:
        play=False
        restart()# to restart the loop
    elif snake_x<=0:
        play=False
        restart()
    elif snake_y>=screen_height:
        play=False
        restart()
    elif snake_y<=0:
        play=False
        restart()
    

def snake_face():
    global play
    global box_x
    global box_y
    global speed_x
    global speed_y
    global box_block
    global box_count
    global black
    box_x=box_x+speed_x
    box_y=box_y+speed_y
    #--------------code to check snake inside------
    inside(box_x,box_y)#inside Function
    #-----------------------------------
    box=pygame.draw.rect(screen,(0,0,0),(box_x,box_y,box_block,box_block))
    snake_head=[]
    snake_head.append(box_x)
    snake_head.append(box_y)
    
    snake_list.append(snake_head)
    for j in range(box_count):
        for i in snake_list:
            pygame.draw.rect(screen,black,(i[0],i[1],box_block,box_block))
    if len(snake_list)>box_count:
        del snake_list[0]
    
    return box

def food_(x,y):
    global box_block
    food=pygame.draw.rect(screen,(255,125,255),(x,y,box_block,box_block))
    return food
    
clock=pygame.time.Clock()

def collision_detection(snake,food):
    global food_x
    global food_y
    global collision_count
    global box_count
    snake1=snake
    food1=food
    collide=snake1.colliderect(food1)
    if collide:
       collision_count=collision_count+1
       if collision_count%13==0:
           food_x=random.randint(50,450)
           food_y=random.randint(50,450)
           
           box_count+=5# box count is been increased to increase the size of the snake by one box           
           
def play_again(play1):
    
    global speed_x
    global speed_y
    global play
    global food_p
    global food_x
    global food_y
    play=play1
    while play:
        
        
        clock.tick(30)
        food_p+=1
        
        screen.fill((255,255,255))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    speed_x=1
                    speed_y=0
                if event.key==pygame.K_LEFT:
                    speed_x=-1
                    speed_y=0
                if event.key==pygame.K_UP:
                    speed_x=0
                    speed_y=-1
                if event.key==pygame.K_DOWN:
                    speed_x=0
                    speed_y=1
        snake=snake_face()
    
        if food_p%250==0:
            food_x=random.randint(50,450)
            food_y=random.randint(50,450)
        food=food_(food_x,food_y)
        collision_detection(snake,food)
       
   
        pygame.display.update()
        
play_again(True)

            

        
