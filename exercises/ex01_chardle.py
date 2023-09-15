"""Ex01 - Chardle. Working towards wordle!"""
__author__ = "730679428"

# ask user for the word
user_inputted_word: str = input("Enter a 5-character word: ")
# throw an error if the user-inputted word is not 5 character
if len(user_inputted_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
# ask user for letter
user_inputted_letter: str = input("Enter a single character: ")
# throw an error if user-inputted letter is more than one character
if len(user_inputted_letter) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for " + user_inputted_letter + " in " + user_inputted_word)

# initialize count
count = 0
# check first character of word
if user_inputted_word[0] == user_inputted_letter:
    count += 1
    print(user_inputted_letter + " found at index " + str(0))
# check second character of word
if user_inputted_word[1] == user_inputted_letter:
    count += 1
    print(user_inputted_letter + " found at index " + str(1))
# check third character of word
if user_inputted_word[2] == user_inputted_letter:
    count += 1
    print(user_inputted_letter + " found at index " + str(2))
# check fourth character of word
if user_inputted_word[3] == user_inputted_letter:
    count += 1
    print(user_inputted_letter + " found at index " + str(3))
# check fifth character of word
if user_inputted_word[4] == user_inputted_letter:
    count += 1
    print(user_inputted_letter + " found at index " + str(4))

# print how many instances of letter were found in word
if count == 0:
    print("No instances of " + user_inputted_letter + " found in " + user_inputted_word)
if count == 1:
    print("1 instance of " + user_inputted_letter + " found in " + user_inputted_word)
if count == 2:
    print("2 instances of " + user_inputted_letter + " found in " + user_inputted_word)
if count == 3:
    print("3 instances of " + user_inputted_letter + " found in " + user_inputted_word)
if count == 4:
    print("4 instances of " + user_inputted_letter + " found in " + user_inputted_word)
if count == 5:
    print("5 instances of " + user_inputted_letter + " found in " + user_inputted_word)