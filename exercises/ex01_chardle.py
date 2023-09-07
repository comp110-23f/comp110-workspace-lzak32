"""Ex01 - Chardle. Working towards wordle"""
__author__ = "730679428"

word: str = input("Enter a 5-character word: ")
if len(word)!=5:
    print("Error: Word must contain 5 characters")
    exit()
letter: str = input("Enter a single character: ")
if len(letter)!=1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + letter + " in " + word)

count=0
if word[0]==letter:
    count+=1
    print(letter + " found at index " + str(0))
if word[1]==letter:
    count+=1
    print(letter + " found at index " + str(1))
if word[2]==letter:
    count+=1
    print(letter + " found at index " + str(2))
if word[3]==letter:
    count+=1
    print(letter + " found at index " + str(3))
if word[4]==letter:
    count+=1
    print(letter + " found at index " + str(4))

if count==0:
    print("No instances of " + letter + " found in " + word)
if count==1:
    print("1 instance of " + letter + " found in " + word)
if count==2:
    print("2 instances of " + letter + " found in " + word)

exit()

