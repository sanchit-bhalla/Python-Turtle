#                                                           Imports needed
import pygame
import turtle
import math
import time

# for music
pygame.mixer.init()
pygame.init()

screen_width = 10
screen_height = 10
# Creating window
gameWindow = pygame.display.set_mode((screen_width, screen_height))

########################    Welcome Screen    ###################3
def welcome():
    turtle.title("Welcome Screen")
    screen = turtle.Screen()
    screen.addshape("welcome_img.gif")
    turtle.shape("welcome_img.gif")
    time.sleep(5)
    turtle.clearscreen()
welcome()

#########################  Background music  #####################
pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play()

##########################    Starting  Picture  ###########################

turtle.setworldcoordinates(0,0,500,300)
turtle.title("Computer Graphics Project")
turtle.colormode(255)
turtle.bgcolor(158, 14, 128)
turtle.colormode(1)
turtle.penup()
turtle.speed(0)

def wheel():
    turtle.goto(0,20)
    turtle.fillcolor('#421d02')
    turtle.begin_fill()
    turtle.circle(130)
    turtle.end_fill()

    turtle.goto(0,120)
    turtle.fillcolor('#1a91a3')
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    i = 120
    while i>20:
        i=i-5
        turtle.penup()
        turtle.goto(0,i)
        turtle.pendown()
        turtle.circle(30+120-i)


    turtle.penup()
    turtle.goto(-5,150)
    turtle.dot(10,"#e37a30")
    turtle.pendown()


def downlane():
    turtle.goto(-5,-5)
    turtle.fillcolor("#cf2e02")
    turtle.begin_fill()
    turtle.fd(505); turtle.left(90); turtle.fd(85); turtle.left(90);
    turtle.fd(505); turtle.left(90); turtle.fd(85); turtle.left(90);
    turtle.end_fill()

    p=30
    while p!=70:
        turtle.goto(0,p); turtle.setheading(0)
        turtle.pen(pencolor="white", pensize=4,pendown="True")
        turtle.fd(500)
        turtle.penup()
        p = p+10
    turtle.pen(pencolor="black", pensize=1,pendown="False")
    turtle.penup()

    turtle.penup()
    turtle.goto(0,80)
    turtle.setheading(0)
    turtle.pen(pencolor="#820511", pensize=8,pendown="True")
    turtle.fd(500)
    turtle.pen(pencolor="black", pensize=1,pendown="True")
    turtle.penup()
    
def music_node_single(i,k=35,j=58):
    turtle.setheading(0)
    turtle.penup()
    turtle.goto(i,j)
    turtle.right(90)
    turtle.pen(pencolor="black", pensize=3,pendown="True")
    turtle.fd(23);
    turtle.right(45)
    turtle.fd(7.07)
    turtle.penup()
    turtle.goto(i,k)
    turtle.right(90)
    turtle.pen(pencolor="black", pensize=1,pendown="True")
    
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(5,180)
    turtle.end_fill()


def music_node_dot(i,j=58):
    turtle.penup()
    if j<=60:
        turtle.goto(i+4,33)
    else:
        turtle.goto(i+4,43)
    turtle.dot(5,"black")


def music_node_one_half(i,j=58):
    turtle.penup()
    turtle.goto(i,j-3)
    turtle.setheading(0)
    turtle.right(60)
    turtle.pen(pencolor="black", pensize=5,pendown="True")
    turtle.fd(16.321)
    
    turtle.right(30)
    turtle.pen(pencolor="black", pensize=4,pendown="True")
    turtle.fd(8)


def single_combine(i1,j1,i2,j2):
    turtle.penup()
    turtle.goto(i1,j1)
    turtle.setheading(0)
    turtle.pen(pencolor="black", pensize=5,pendown="True")

    angle = math.acos(20/(math.sqrt(500)))  # in radians
    angle_in_degree = (180*7*angle)/22    # bcz. pie radians  ==  180 degrees

    if j1>j2:
        turtle.right(angle_in_degree)
    else:
        turtle.left(angle_in_degree)

    turtle.fd(math.sqrt(500))
    

def plant_stem(i,h=18):
    turtle.penup()
    turtle.goto(i,80)
    turtle.setheading(90)
    turtle.pen(pencolor="#820511", pensize=9,pendown="True")
    turtle.fd(h-5)
    turtle.pen(pencolor="#820511", pensize=8,pendown="True")
    turtle.fd(5)

    turtle.penup()
    turtle.goto(i-10,80+h+5)
    turtle.setheading(270)
    turtle.pen(pencolor="#820511", pensize=5,pendown="True")
    turtle.fd((h/2)-3)
    turtle.circle(5,90)
    
    turtle.goto(i+4,78+h/2)
    turtle.setheading(0)
    turtle.circle(5,90)
    turtle.setheading(90)
    turtle.fd((h/2)-3)



def flower():
    turtle.penup()
    turtle.goto(475,146)
    turtle.setheading(0)
    turtle.right(30)
    
    turtle.fillcolor('yellow')
    turtle.begin_fill()
    turtle.circle(5)
    turtle.end_fill()

    turtle.goto(477,150)
    turtle.setheading(0)
    turtle.right(30)
    size = 2
    for i in range(6):
        turtle.pen(pencolor="#02c2b2", pensize=size,pendown="True")
        turtle.fd(4)
        size=size+1

def pallette(x=300,y=100,s_angle=30,e_angle=60,length=50,fill_color='red'):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.left(s_angle)
    turtle.pen(pencolor=fill_color, pensize=1,pendown="True")
    
    turtle.fillcolor(fill_color)
    turtle.begin_fill()    
    turtle.fd(length)
    #turtle.left(90)

    turtle.right(30)
    
    turtle.circle(4,180)
    turtle.goto(x,y)
    turtle.end_fill()

def colors(n):
    color_list = ["#89118f","#67e0de","#ab005e","#153b0c","#086666"]
    index = n%len(color_list)
    return color_list[index]

def forward(x):
    for i in range (x//2):
        turtle.forward(2)
        turtle.bgcolor(colors(i))
        time.sleep(0.08)

def backward(x):
    for i in range (x//2):
        turtle.backward(2)
        turtle.bgcolor(colors(i))
        time.sleep(0.08)

def upward(x):
    turtle.setheading(0)
    turtle.left(90)
    for i in range (x//2):
        turtle.forward(2)    
        time.sleep(0.08)

def downward(x):
    turtle.setheading(0)
    turtle.right(90)
    for i in range (x//2):
        turtle.forward(2)    
        time.sleep(0.08)


def show():
    turtle.penup()
    turtle.goto(285,195)
    screen = turtle.Screen()
    #screen.bgpic("bgimg1.gif")
    screen.addshape("bgimg1.gif")
    turtle.shape("bgimg1.gif")
    
    turtle.speed(3)    
    turtle.setheading(0)    
    for i in range(3):
        forward(30)
        time.sleep(0.5)        
        backward(30)
        time.sleep(0.5)
    turtle.bgcolor("#9e0e80")
        
########################    CALLING FUNCTIONS   ######################

downlane()
wheel()
music_node_single(120)
music_node_dot(120)

music_node_single(150)
music_node_one_half(150)

music_node_single(180,25,50)
music_node_single(200)
single_combine(180,50,200,60)

music_node_single(250,25,50)
music_node_single(270)
single_combine(250,50,200,60)

music_node_single(400,45,70)
music_node_dot(400,70)

music_node_single(430)
music_node_one_half(430)

music_node_single(470)
music_node_single(490,25,50)
single_combine(470,60,490,50)


plant_stem(135)

plant_stem(180,20)

plant_stem(290,20)
plant_stem(330)

plant_stem(400,23)
plant_stem(440)

flower()
pallette(478,150,210,200,20,"#cf2e02") 
pallette(478,150,185,200,20,"#cf2e02")    
pallette(478,150,160,200,20,"#cf2e02")
pallette(478,150,135,200,20,"#cf2e02")
pallette(478,150,110,200,20,"#cf2e02")

show()
pygame.quit()
