import random




def initialize_chosen_word(all_words):
    return random.choice(all_words)


def initialize_guessed_word(c_word):
    return "_" * len(c_word)





def game_over(c_word,g_word,lives_count):
    return c_word == g_word or lives_count == 0


def show_data(lives_count,g_word,g_letters):
    print(f"You have {lives_count} lives left")
    print(g_word)
    if g_letters:
        print(f"The list of letters you tried is: {g_letters}")
    return

def returns_letter():
    while True:
        letter = input("Choose a letter: ").lower()
        if not letter.isalpha() or not len(letter) == 1:
            print("It's must be a letter")
            continue
        return letter


def correct_guess(chosen_letter,g_word,c_word):
    global lives
    if chosen_letter in c_word:
        update_guesses_word(chosen_letter,g_word,c_word)
    else:
        lives -= 1
        guessed_letters.add(chosen_letter)


def update_guesses_word(letter,g_word,c_word):
    for i,char in enumerate(c_word):
        if letter == char:
            g_word[i] = char
    return



def main():
    chosen_word = list(initialize_chosen_word(possible_words))
    guessed_word = list(initialize_guessed_word(chosen_word))
    while not game_over(chosen_word,guessed_word,lives):
        show_data(lives,guessed_word,guessed_letters)
        letter = returns_letter()
        correct_guess(letter,guessed_word,chosen_word)
    if lives:
        print("Well done! You won")
    else:
        print("You lost! Maybe next time")


possible_words = ["hello","kodcode","start","python","game"]
lives = 10
guessed_letters = set()


main()