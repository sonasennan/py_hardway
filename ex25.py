def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words            #function to split the inputed string and the otput is returned.

def sort_words(words):
        """Sorts the words."""
        return sorted(words)   #function to sort the inputed string.

def print_first_word(words):
        """Prints the first word after popping it off."""
        word = words.pop(0)
        print(word)      #function to display and remove the first word in a sentence.

def print_last_word(words):
        """Prints the last word after popping it off."""
        word = words.pop(-1)
        print(word)               #function to display and remove the last word in a sentence.  

def sort_sentence(sentence):
        """Take in a full sentence and returns the sorted words."""
        words = break_words(sentence)
        return sort_words(words)   #this function takes a sentence,split the sentence into words and sort them.

def print_first_and_last(sentence):
        """Prints the first and last words of the sentence."""
        words = break_words(sentence)
        print_first_word(words)
        print_last_word(words)       #function which accepts a sentence,split it into words and then remove and display the first and last words.

def print_first_and_last_sorted(sentence):
        """Sorts the word then prints first and last one."""
        words = sort_sentence(sentence)
        print_first_word(words)
        print_last_word(words)  #this function takes a sentence,split it to words,sort it and then displays and removes the first and last word.