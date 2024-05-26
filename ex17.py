from sys import argv    #import argv module from sys library.
from os.path import exists   #importing exists() function from the sub module 'path' in os module.

script,from_file,to_file=argv   #unpacking the command-line arguments.

print(f"Copying from {from_file} to {to_file}")   #accesssing and printing the variables in argv.


in_file=open(from_file,'r')   #opening the file in read mode.
indata=in_file.read()      #stored the read data in a variable.

print(f"The input file is {len(indata)} bytes long.")  #used 'len()' function to find the length of content in file.

print(f"Does the output file exist? {exists(to_file)}")  #used 'exists()' function to check whether the particular file exists or not.
print("Ready,hit RETURN to continue,CTRL-C to abort.")
input()

out_file=open(to_file,'w')   #opening file in write mode.
out_file.write(indata)   #writing the content in one file to another.

print("Alright,all done.")

out_file.close()  #closing 'w' mode.
in_file.close()   #closing 'r' mode.