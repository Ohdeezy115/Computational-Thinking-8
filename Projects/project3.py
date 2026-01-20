import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 =-350
y1 =200
x2 =-350
y2 =100
x3 =-350
y3 = -50
x4 =-350
y4 =-225


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("steven_a_smith")
t1 = create_sprite("bike",x1,y1)
t2 = create_sprite("fish",x2,y2)
t3 = create_sprite("holdup",x3,y3)
t4 = create_sprite("City_Boy",x4,y4)


# Section 3 - Racing
# TODO - set how much each variable changes by and increase the number of repeats to at least 30
# Comment - the bike has the highest chance to win but it can get unlucky and go backwords. city boy is next but it can also get stuck going only five or six pixels if it gets unlucky
# Comment Shaq has a low chance to win but not zero if city boy and the bike get unlucky he can win
# comment it is impossible for the fish to win Shaq is always going to be past it so the fish has no hope of winning
for i in range(37):
    x1 += random.randint (-10, 50)
    x2 += 10
    x3 += 15
    x4 += random.randint (1, 35)

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# Section 4 - Winner
# TODO - complete the elif for player 2 winning
# TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("The bike wins!")
elif x2 >= x1 and x2 >= x3 and x2 >= x4:
    print("The Fish wins!")
elif x3 >= x2 and x3 >= x1 and x3 >= x4:
    print("Shaqirk O'neal wins!")
elif x4 >= x2 and x4 >= x3 and x4 >= x1:
    print("City boy City boy wins!")

turtle.exitonclick()