def while_loop(): 
    range=input("Enter the range")   #takes a range as input from the user,and appends the numbers in the range into an empty list.The list is printed in each iteration.
    i = 0
    numbers = []
    while i < int(range):
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


        print("The numbers: ")

    for num in numbers:
        print(num)

while_loop()