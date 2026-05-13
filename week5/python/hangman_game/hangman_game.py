import random


possible_words = ["hello","kodcode","start","python","game"]
chosen_word = []
lives = 10
guessed_letters = set()
guessed_word = []

def initialize(all_words,c_word,g_word):
    g_word = all_words[random.randint(0,len(all_words))]


def game_over(secret_word,g_word,lives_count):
    return secret_word == g_word or lives_count == 0


def show_data(lives_count,g_word,g_letters):
    print(f"You have {lives_count} lives left")
    print(g_word)
    print(g_letters)
    return

def returns_letter():
    while True:
        letter = input("Choose a letter: ").lower()
        if not letter.isalpha():
            print("It's must be a letter")
            continue
        return letter


def correct_guess(chosen_letter,g_word,c_word):
    global lives
    if chosen_letter == c_word:
        update_guesses_word(chosen_letter,g_word,c_word)
    else:
        lives -= 1
        guessed_letters.add(chosen_letter)


def update_guesses_word(letter,word,c_word):
    for i,char in enumerate(c_word):
        if letter == char:
            word[i] = char
    return



def main():
    while not game_over(chosen_word,guessed_word,lives):
        show_data(lives,guessed_word,guessed_letters)
        if lives:
            print("Well done! You won")
        else:
            print("You lost! Maybe next time")


main()