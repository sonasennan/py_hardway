print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")    #print statement which asks input from the user.

door = input("> ")    #user input.

if door == "1":            #this block will be executed if the user inputs 1.
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")   #user input.

    if bear == "1":    #nested if.      
        print("The bear eats your face off. Good job!")  # will be executed if the user inputs 1.
    elif bear == "2":
        print("The bear eats your legs off. Good job!")   # will be executed if the user inputs 2.
    else:
        print(f"Well, doing {bear} is probably better.")  # will be executed if the user inputs a number other than  1 and 2.
        print("Bear runs away.")

elif door == "2":    #will be executed if the first condition is false and the user input is 2.
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")      #will be executed only if the first 2 conditions are false.