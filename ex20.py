from sys import argv   #importing argv module from sys library.

script,input_file = argv  #unpacking the command-line argument.

def print_all(f):
    print(f.read())     #function to read file.

def rewind(f):
    f.seek(0)       #function to change the file pointer to the beginning of the file.

def print_a_line(line_count,f):
    print(line_count,f.readline())   #to print the file again.

current_file = open(input_file)   #opening the input_file and the reference in stored in a variable named current_file.

print("First,lets print the whole file:\n")

print_all(current_file)    #calling the 1st function by passing 'current_file' as parameter.

print("Now lets rewind,kind of like a tape.")

rewind(current_file)   #calling the second function 'rewind()'.passing current_file to the function.

print("Lets print three lines:")

current_line = 1
print_a_line(current_line,current_file)  #calling print_a_line().

current_line += 1   #increamenting the value by 1 by using += operator.
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)
