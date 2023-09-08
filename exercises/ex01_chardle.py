"""Ex01 - Chardle. Working towards wordle"""
__author__ = "730679428"

#ask user for the word
word: str = input("Enter a 5-character word: ")
#throw an error if the user-inputted word is not 5 character
if len(word)!=5:
    print("Error: Word must contain 5 characters")
    exit()
#ask user for letter
letter: str = input("Enter a single character: ")
#throw an error if user-inputted letter is more than one character
if len(letter)!=1:
    print("Error: Character must be a single character.")
    exit()
    
print("Searching for " + letter + " in " + word)

#initialize count
count=0
#check first character of word
if word[0]==letter:
    count+=1
    print(letter + " found at index " + str(0))
#check second character of word
if word[1]==letter:
    count+=1
    print(letter + " found at index " + str(1))
#check third character of word
if word[2]==letter:
    count+=1
    print(letter + " found at index " + str(2))
#check fourth character of word
if word[3]==letter:
    count+=1
    print(letter + " found at index " + str(3))
#check fifth character of word
if word[4]==letter:
    count+=1
    print(letter + " found at index " + str(4))

#print how many instances of letter were found in word
if count==0:
    print("No instances of " + letter + " found in " + word)
if count==1:
    print("1 instance of " + letter + " found in " + word)
if count==2:
    print("2 instances of " + letter + " found in " + word)


