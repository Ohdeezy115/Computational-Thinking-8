# Section 1 - Your code
from utils import *
set_background("gloving")

s1 = create_sprite("ireland", 150, 200)
s2 = create_sprite("Odin", -225, 30)
s3 = create_sprite("City_Boy", 0, 0)
s4 = create_sprite("Odin_Football", 230, -35)

message1 = create_sprite("alien",-200,200)
message1.color("purple")
message1.write("Odin",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-300,-250)
message2.color("green")
message2.write("I have a hole in my shoes",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()