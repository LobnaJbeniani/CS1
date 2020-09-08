#Lobna Jbeniani
#CS1, Lab1
#Date: TUE 28 JAN 2019

from cs1lib import *

#General Variables
window_height=400
window_width=400


#Paddles Variables
paddle_height=70
paddle_width=30

#The Y Values for the paddles
y1=170 #left
y2=170 #right

#The X Values for the paddles
x1=0 #left
x2=370 #right

#The speed for the paddles
vpaddle=10

#Boolean Variables
key_a=False
key_z=False
key_k=False
key_m=False
key_space=False
key_q=False
key=""

game_in_process=False
#Ball Variables
xball=200
yball=200
radius=10

#Ball Speed
vxball=2
vyball=2



#Drawing Background
def background():
    set_clear_color(0.4,0.6,0.9)
    clear()
    set_font_size(13 )
    draw_text("Pong Game. SPACE TO START.", 100, 50)


#Left Paddle: Drawing+Movement
def paddle_left():
    global y1, key_z, key_a, key

    set_fill_color(0.9,0.2,0.2)
    enable_stroke()
    set_stroke_color(1,1,0)
    draw_rectangle(x1, y1, paddle_width, paddle_height)

    if key_space:
        #Paddle Movement
        if key_z and y1<=320:
            y1=y1+vpaddle
        if key_a and y1>=10:
            y1=y1-vpaddle

#Right Paddle: Drawing+Movement
def paddle_right():
    global y2, key_k, key_m, key

    set_fill_color(0.9,0.2,0.2)
    enable_stroke()
    set_stroke_color(1,1,0)
    draw_rectangle(x2, y2, paddle_width, paddle_height)

    if key_space:
        #Paddle Movement
        if key_m and y2<=320:
            y2 = y2 + vpaddle

        if key_k and y2>=10:
            y2 = y2 - vpaddle


#The Ball: Drawing+Movement
def ball():
    global xball, yball, radius, vyball, vxball, vpaddle, y1, y2, key_space, x1, x2

    set_fill_color(0,0,0)
    enable_stroke()
    draw_circle(xball,yball, radius)

    #ball movement
    if key_space:

        xball=xball+vxball
        yball=yball+vyball

        #ball hits walls

        if yball+radius==window_height:
            vyball=-vyball
            xball=xball-vyball


        if yball-radius==0:
            vyball=-vyball
            xball=xball+vxball

        #when ball hits right paddle
        if xball+radius==window_width-paddle_width and yball-radius<=y2+(paddle_height) and yball+radius>=y2-(paddle_height):
            vxball=-vxball


        #when ball hits left paddle
        if xball - radius == paddle_width and yball - radius >= y1 - (paddle_height) and yball + radius <= y1 + (paddle_height):
            vxball=-vxball

        #frozen function

        if xball>=400 or xball<0:


            xball=window_width/2
            yball=window_height/2

            key_space=False


#The winner function operates when one of the players has won the game
def winner():
    global xball, key_space
    if xball>=397:
        enable_stroke()
        draw_text("Game Over.", 160,70)
        key_space=False
    elif xball<=0:
        enable_stroke()
        draw_text("Game Over.", 160,70)
        key_space=False

#Press Function
def press(value):
    global key_a, key_z, key_k, key_m, key, key_q, key_space
    key=value.lower()
    #To Move Paddles
    if key=="a":
        key_a=True
    if key=="z":
        key_z=True
    if key=="k":
        key_k=True
    if key=="m":
        key_m=True
    #To START/RESTART
    if key==" ":
        key_space=True
    #TO QUIT
    if key=="q":
        key_q=True

#Release Function
def release(value):
    global key_a, key_z, key_k, key_m, key, key_q
    key = value.lower()

    if key=="a":
        key_a = False
    if key == "z":
        key_z = False
    if key == "k":
        key_k = False
    if key == "m":
        key_m = False


#The Play Function
def play():
    global y1, key_a, key_z, key_k, key_m, key, key_space

    background()
    paddle_left()
    paddle_right()
    ball()
    winner()
    if key_q:
        cs1_quit()

#Start The Game
start_graphics(play, key_release=release, key_press=press)


