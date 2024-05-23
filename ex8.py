formatter = "{} {} {} {}" #creates four placeholders
print(formatter.format(1,2,3,4))   #This line substitutes the numbers 1, 2, 3, and 4 into the placeholders of the formatter string. 
print(formatter.format("one","two","three","four"))    #This line substitutes the numbers one, two, three, and four into the placeholders of the formatter string. 
print(formatter.format("True","False","False","True"))   #substituting it using boolean values true and false.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))



