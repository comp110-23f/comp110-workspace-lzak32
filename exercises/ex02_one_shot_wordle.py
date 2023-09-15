"""One shot wordle, another step closer to wordle."""
__author__ = "730679428"

# initialize word to guess
secret_word: str = "python"

# have user guess until they return a guess with a length of the secret word
user_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

# initialize variables for each emoji
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# initialize index to 0 and emoji output to an empty string
index: int = 0
emoji_output: str = ""

# perform this to analyze each character in the secret word and user guess
while index < len(secret_word):
    # if the character of the secret word and character of the user guess match, put green box
    if secret_word[index] == user_guess[index]:
        emoji_output += GREEN_BOX
    # if the characters don't match, check if the character of user guess is found elsewhere in the secret word
    else:
        # initialize index_check to 0 and letter in word to False
        index_check: int = 0
        letter_in_word: bool = False
        # for each character in secret_word, check if it equal to the character of user guess. If it is, set letter in word to False
        # and add a yellow box in the user's guess place
        while index_check < len(secret_word):
            if user_guess[index] == secret_word[index_check]:
                emoji_output += YELLOW_BOX
                letter_in_word = True
            # iterate to next index
            index_check += 1
        # if the user guess letter did not exist at all in the secret word, add a white box
        if letter_in_word is False:
            emoji_output += WHITE_BOX
    # go to next character of secret word and user guess
    index += 1

print(emoji_output)

if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")