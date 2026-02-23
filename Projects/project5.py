import turtle, math, time, random
from utils import *

# Section 1: Setup
s1 = create_sprite("MJ",-310,-100) 
s3 = create_sprite("basketball2",-255,40)
s6 = create_sprite("hoop",300,100)
s5 = create_sprite("meter2",-325,100)
s2 = create_sprite("arrow3",-240,50)
s4 = create_sprite("alien",280,100)
t1 =create_sprite("alien",-350, 250)


#- create your player character and any other sprites
set_background("flight")
points = 0

sprite_list = []

# Section 2: Controls
def move_up1():
    x = s2.xcor()
    y = s2.ycor() + 10
    s2.goto(x,y)
        
def move_down1 ():
    x = s2.xcor()
    y = s2.ycor() - 10
    s2.goto(x,y)

def move_up():
    x = s3.xcor()
    y = s3.ycor() + 10
    s3.goto(x,y)
        
def move_down():
    x = s3.xcor()
    y = s3.ycor() - 10
    s3.goto(x,y)

window.onkeypress(move_up1, "w")
window.onkeypress(move_down1, "s")
window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
# TODO - define your controls
# TODO - pick keys for each control

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    # TODO - add code for automatic actions
    if s2.ycor() >=200:
        s3.forward(1)
    t1.clear()
    t1.color("red")
    t1.write(f"points{points}",font=("arial",25,"normal"))

    if get_distance (s3,s4) < 50:
        s3.goto(-255,40)
        s2.goto(-240,50)
        points+=2
    s4.hideturtle()
    t1.hideturtle()

    if points >= 10:
        print("You Win")
        set_background("lebron")
        t1.write("YOU WIN")
        s1.hideturtle()
        s2.hideturtle()
        s3.hideturtle()
        s4.hideturtle()
        s5.hideturtle()
        s6.hideturtle()
    # TODO - make an if statement for ending the game


    time.sleep(0.01)
    window.update()
    

	
print("Game Over")