#This is a game where there are four doors and u have to choose the right door.# 
#If u choose the wrong door u get caught and u lose# 



print("CHOOSE A DOOR")
print("Four doors ahead of you, and a monster behind one of them")
print("Which door will you choose?")
door = input("1, 2, 3, or 4?: ")
score = 0

if door=="1":
    print("You are save!")
    score += 5

elif door=="2":
    print("You are save!")
    score += 5

elif door=="3":
    print("OH NO!! The monster caught you!")
    score -= 10

elif door=="4":
    print("You are save!")
    score += 5

print("Your score:"+str(score)) 