def add(a,b):               #function to add 2 numbers and the output is returned.
    print(f"ADDING {a} + {b}")   #The function parameters are accessed using string formatting.
    return a + b                         

def subtract(a,b):          #function to subtract 2 numbers and the output is returned.
    print(f"SUBTRACING {a} - {b}")
    return a - b      

def multiply(a,b):          #function to multiply 2 numbers and the output is returned.
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):            #function to divide 2 numbers and the output is returned.
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Lets do some math with just functions!")

age = add(30,5)   #passing arguments to 'age()' function and the output is stored to the variable 'age'.
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, Iq: {iq}")    #accessing and printing the values using string formatting.


#A puzzle for the extra credit,type it in anyway.
print("Here is a puzzle.")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))  #nested function call.

print("That becomes: ",what, "Can you do it by hand?")