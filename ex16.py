from sys import argv   #importing argv module from sys library.   

script,filename = argv        #unpacking the command-line arguments into variables.

print(f"We are going to erase {filename}.")    #accessing the filename from argv using string formatting.
print("If you don't want that,hit CTRL-C (^C.)")
print("If you want that,hit RETURN")

input("?")    #user input

print("Opening the file...")
target = open(filename,'w')      #opening the file in w mode and the reference is send to the variable 'target'.

print("Truncating the file..Goodbye!")
target.truncate()              #To remove the data in file inside the variable 'target', the variable is passed to the function truncate().*

print("Now i am going to ask you for three lines.")

line1 = input("Line 1:  ")   #input from the user.
line2 = input("Line 2:  ")
line3 = input("Line 3:  ")

print("I am going to write these to the file")

target.write(f"{line1}\n{line2}\n{line3}\n ")    #writing the data inputed from the user to the variable 'target'.


print("And finally,we close it.")
target.close()    #closing the file opened in write mode.

target1 = open(filename,'r')   #opening the file in read mode and the reference is saved in a variable.
print(target1.read()) #reading and then printing the content in the file.
target1.close()