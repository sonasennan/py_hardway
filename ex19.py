def cheese_and_crackers(cheese_count,boxes_of_crackers):     #Defining a function with 2 arguments.
    print(f"You have {cheese_count} cheeses!")             #Assessing the value inside the argument using string formatting.
    print(f"You have {boxes_of_crackers} boxes of crackers")
    print("Get a blanket.\n")



print("We can just give the function numbers directly")
cheese_and_crackers(20,30) #function calling.


print("OR,we can use variables from our script:")
amount_of_cheese=10   #assigning values to variables.
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)  #variables are passed to function as arguments.


print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)    #doing math inside function call.

print("And we acn combine the two..Variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)   #function calling with a combination of math and variables as parameters.


