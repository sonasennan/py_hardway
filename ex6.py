types_of_people = 10           #Initializes a variable with value 10.
x = f"There are {types_of_people} types of people."   #Creates a string 'x' and its value is the value of type_of_people.

binary = "binary"    #The binary variable stores the value 'binary'.
do_not = "don't"     #The do_not variable stores the value 'don't'.
y = f"Those who know {binary} and those who {do_not}."   #assignes the value of binary and do_not to the string.

print(x)   #prints the value of x
print(y)   #prints the value of y

print(f"I said : {x}")              #substitutes the value of x
print(f"I also said : '{y}'")       #substitutes the value of y

hilarious = False               #Initializing a boolean variable 'hilarious' with value False.
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of ..."   #
e = "a string with a right side"     #Initializes 2 variables with string values.

print(w + e) #concatenates w and e to print the result.