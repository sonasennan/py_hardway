import sys
script,encoding,error=sys.argv       


def main(language_file,encoding,errors):
    line=language_file.readline()           #function to read file line-by-line.

    if line:                                  #checks whether there is data in the variable named 'line'.
        print_line(line,encoding,errors)       #this line will be executed only if returns True.
        return main(language_file,encoding,errors)   #calling main() function again inside the main function itself.


def print_line(line,encoding,errors):
    next_lang=line.strip()                #stripping of trailing \n.
    raw_bytes=next_lang.encode(encoding,errors=errors)        #encoding the UTF-8 string.Pass to encode(),the encoding i want and how to handle error.
    cooked_string=raw_bytes.decode(encoding,errors=errors)     #decoding the raw data.

    print(raw_bytes,"<===>",cooked_string)   #displaying the encoded and decoded data.


languages=open("languages.txt",encoding="utf-8")   #opening the file and tells encoding type.

main(languages,encoding,error)   #main function call.