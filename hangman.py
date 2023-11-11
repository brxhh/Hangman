import random
from words import words
from hangman_visual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    used_letters = set()
    lives = 7

    while word_letters and lives > 0:
        print(f'You have {lives} lives left and you have used these letters: {" ".join(used_letters)}')

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter.isalpha() and user_letter not in used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1
                print(f'\nYour letter, {user_letter}, is not in the word.')

        elif user_letter in used_letters:
            print(f'\nYou have already used the letter {user_letter}. Guess another letter.')

        else:
            print('\nThat is not a valid letter. Please enter a letter.')

    if lives == 0:
        print(lives_visual_dict[lives])
        print(f'You ran out of lives. The word was {word}. Better luck next time!')
    else:
        print(f'Congratulations! You guessed the word {word}!')


if __name__ == '__main__':
    hangman()