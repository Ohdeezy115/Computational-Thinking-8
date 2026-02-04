import turtle, time, random
from utils import *

# Comment- in this game your goal is to get as much ramen as possible by clicking space. when you get enough ramen you can buy a big ramen wich gives you more ramen per second
# once you get to ten big ramen you win and your ramen score goes really high.


# Section 1 - setup
set_background("Mooseman")

t1 =create_sprite("alien",-350, 150)

# TODO - create at least two variables and set their starting value. ex: cookies = 0
ramen = 0
big_ramen = 0
cost = 10




# Section 2 - controls
# TODO - define an action. ex: def my_control()

def make_ramen ():
    global ramen
    ramen += 1
    x = random.randint (200,350)
    y = random.randint (-300,300)
    create_sprite ("ramen",x,y)

def get_big_ramen ():
    global big_ramen,ramen,cost
    if ramen >= cost:
        ramen = ramen - cost
        cost = cost * 1.5
        big_ramen += 1
    
        x = random.randint (-100,100)
        y = random.randint (-100,100)
        create_sprite ("big_ramen",x,y)


        

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")
# when you press space you get one ramen and it will apear on the right of your screen
 # when you press r and have enough money for a big ramen it will appear in the middle of the screen and start giving you one ramen every second.
window.onkeypress(make_ramen,"space")
window.onkeypress(get_big_ramen, "r")

# TODO - make a second control





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    t1.clear()
    t1.write(f"ramen: {ramen}\ncost: {cost}\nbig_ramen: {big_ramen})",font=("arial",25,"normal"))
    
    # TODO - put any repeating actions here
    if i % 70 == 0:
        ramen += big_ramen

    if big_ramen >= 10:
        big_ramen += 1000

    time.sleep(0.01)
    window.update()