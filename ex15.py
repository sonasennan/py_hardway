from sys import argv   #importing argv module from sys library.

script,filename=argv        #unpacking the command-line arguments into variables. 

txt=open(filename)           #opening the file specified by the user in command and its object is assigned to a variable named "txt".

print(f"Here's your file {filename}:")   #accessing the filename using string formatting.
print(txt.read())                         #reading the object in the variable "txt" and printing it.

print("Type the filename again:")
file_again=input("> ")                   #giving an input option for the user to enter the filename again and assigned it it a variable.

txt_again=open(file_again)     #opening the object inside the variable "file_again" and assigning it to another variable named "txt_again".

print(txt_again.read())        #read the file and then print it.