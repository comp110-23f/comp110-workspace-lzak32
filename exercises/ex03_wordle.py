"""Wordle final game (ex03)."""
__author__ = "730679428"

def contains_char(word: str, letter: str) -> bool:
    """returns a bool for if letter is in word."""
    # raise error if the letter arg is more than 1
    assert len(letter) == 1
    # initialize variables
    ind: int = 0
    in_word: bool = False
    # for each character in the word, check if the letter is in the word
    while ind < len(word) and not in_word:
        if letter == word[ind]:
            in_word = True
        ind += 1
    # return a bool that represents if the letter is in the word
    return in_word

def emojified(guess: str, word: str) -> str:
    """returns emoji string based on guess and word."""
    # return an error is the guess is different length than word
    assert (len(guess)==len(word))
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # initialize variables
    ind: int = 0
    emoji_str: str = ""
    # for every character in guess, assign a respective box emoji for its status (in word same place, in word, not in word)
    while ind < len(word):
        if guess[ind] == word[ind]:
            emoji_str += GREEN_BOX
        elif contains_char(word,guess[ind]):
            emoji_str += YELLOW_BOX
        else: 
            emoji_str += WHITE_BOX
        ind += 1
    # return the coded emoji string
    return emoji_str

def input_guess(expected_length: int) -> str:
    """asks user for guess until they input one of expected length"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    # ask user for guess of expected length until they correctly input one
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """main game loop."""
    # initialize game variables
    turn: int = 1
    word: str = "codes"
    guess: str = ""
    emoji: ""
    # while the user hasn't won or run out of turns, ask them for guess and print coded emojis for guess
    while guess != word and turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(word))
        emoji: str = emojified(guess,word)
        print(emoji)
        if guess == word:
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
    # print this if they lose
    if turn > 6:
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()
    





