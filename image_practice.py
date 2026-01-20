# Section 1 - Your code
from utils import *
set_background("gloving")

s1 = create_sprite("cardinal", 300, 300)
s2 = create_sprite("cardinal", -300, 300)
s2 = create_sprite("cardinal", -300, -300)
s2 = create_sprite("cardinal", 300, -300)
s2 = create_sprite("holdup", -0, 0)


message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Odin",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()