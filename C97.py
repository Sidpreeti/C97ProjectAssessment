import random

rand = random.randint(1, 9)
count = 5 
while (count >0):
    guess = int(input ("Guess a No Between 1 to 9 :     "))
    count = count - 1 
    if (guess == rand):
        print("Congratulations")
    else : 
        c =abs( rand - guess)
        print ("How far you are from Guess")
        print (c)

print("Done")