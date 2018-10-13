#Author: Rissalat A. Kapdi
#Program: Simple dictionary
#The program takes a word as an input, check a dictionary file for a matching word and provides its meaning
#If the word is misspelled, it provides a suggestion for what you might have meant.

#import libraries
import json
from difflib import get_close_matches

#file variable
data = json.load(open("data.json"))

#@input @ w word to find meaning
#@returns String representation of word definition if word found, otherwise displays a message
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn= input("Did you mean %s instead? Enter Y for yes or N for no. " % get_close_matches(w, data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn=="N":
            return("No such word found. ")
        else:
            return("Please try a differnt input. ")
    else:
        return "The word does not exist, Please check yourself before you wreck yourself!! "

#if the output is in a list form, it iterates and prints through it
word = input("Enter word: ")
output = translate(word)
if type(output)== list:
    for item in output:
        print(item)
#if input is not a List, the output is printed without any iteration
else:
    print(output)
