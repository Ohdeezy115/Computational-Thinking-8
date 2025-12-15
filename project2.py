lebron_points = 0
Larry_bird_points = 0
will_Baker_points = 0

answer1 = input ("Wich of these colors are the best A, Purple B, Green Or C, Red?")
if answer1 == "A":
    lebron_points += 1
elif answer1 == "B":
    Larry_bird_points += 1
elif answer1 == "C":
    will_Baker_points += 1

answer2 = input ("Wich of these numbers are the coolest A, 33 B, 23 C, 1")
if answer2 == "A":
    Larry_bird_points += 1
elif answer2 == "B":
    lebron_points += 1
elif answer2 == "C":
    will_Baker_points += 1

answer3 = input ("Wich of these months are your favorite A,December  B,November  C,February ")
if answer3 == "A":
    Larry_bird_points += 1
elif answer3 == "B":
    lebron_points += 1
elif answer3 == "C":
    will_Baker_points += 1

answer4 = input ("Where out of these choices would you want to live A,Seattle  B,Boston  C,Los Angeles ")
if answer4 == "A":
    will_Baker_points += 1
elif answer4 == "B":
    Larry_bird_points += 1
elif answer4 == "C":
    lebron_points += 1


answer5 = input (" wich of these movies are the most fun to watch A,The Lorax  B,The Godfather  C,The incredibles ")
if answer5 == "A":
    will_Baker_points += 1
elif answer5 == "B":
    Larry_bird_points += 1
elif answer5 == "C":
    lebron_points += 1


answer6 = input ("Final Question Wich animal is the coolest out of these A,Cardinal  B,Goat  C,Dog ")
if answer6 == "A":
    Larry_bird_points += 1
elif answer6 == "B":
    lebron_points += 1
elif answer6 == "C":
    will_Baker_points += 1

if lebron_points > Larry_bird_points and lebron_points > will_Baker_points:
    print(" Your favorite basketball player is LEBRON!!!")

if will_Baker_points > Larry_bird_points and will_Baker_points > lebron_points:
    print(" Your favorite basketball player is WIlliam Baker!!!")

if Larry_bird_points > lebron_points and Larry_bird_points > will_Baker_points:
    print(" Your favorite basketball player is LARRY BIRD!!!")



print(f" your score is {lebron_points} Lebron, {Larry_bird_points} Larry Bird, and {will_Baker_points} Will Baker")
