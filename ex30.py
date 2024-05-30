people = 30
cars = 40
trucks = 15


if cars > people:        #checks whether the number of cars is greater than number of people.
    print("We should take the cars.")  #prints if the first condition is true.
elif cars < people:     #this condition is checked only if the first condition is false.
    print("We should not take the cars.")   #prints if the elif condition is true.
else:             
    print("We can't decide.")  #this will be excecuted only if both the conditions are false.

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")