import turtle

turtle.setworldcoordinates(0,0,500,300)
turtle.bgcolor("#9e0e98")
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


def music_node_1(i):
    turtle.penup()
    turtle.goto(i,58)
    turtle.right(90)
    turtle.pen(pencolor="black", pensize=3,pendown="True")
    turtle.fd(23);
    turtle.right(45)
    turtle.fd(7.07)
    turtle.penup()
    turtle.goto(i,35)
    turtle.right(90)
    turtle.pen(pencolor="black", pensize=1,pendown="True")
    
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(5,180)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(i+4,33)
    turtle.dot(4,"black")
    
downlane()
#wheel()
music_node_1(150)

turtle.ht()
