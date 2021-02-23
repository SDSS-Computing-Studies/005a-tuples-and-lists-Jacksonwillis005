#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

computer = str(input("Enter a word:")).strip()
bug = str(input("Enter a word:")).strip()
virus = str(input("Enter a word:")).strip()
memory = str(input("Enter a word:")).strip()
storage = str(input("Enter a word:")).strip()

word=[computer, bug, virus, memory, storage]

print(word)