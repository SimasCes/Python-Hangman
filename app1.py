# All the characters allowed to be used
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', "'"]

# Set up some arrays which will store the secret word,
# Correct letters you guessed (in the correct spaces), and the incorrect letters
full_word = []
correct_guesses = []
incorrect_guesses = []

# The secret word is set, and is made sure it is lower case
secret_word = input("Secret word: ").lower()


# Used to check if the correct alphabet characters are being used
# secret_words (instead of word) is used to not interfere with outer scope (shows a caution without this)
def check_if_secret_word_is_good(secret_words):
    correct_word = False
    # Will run until a correct secret_word is set
    while not correct_word:
        correct_count = 0
        # Checks each character of the secret_word to each character of the alphabet
        for x in range(0, len(secret_words)):
            for y in range(0, len(alphabet)):
                if alphabet[y] == secret_words[x]:
                    correct_count += 1
        # If the characters in the secret_word are all in the
        # alphabet (no numbers or odd strings like ^) then this statement will be true
        if correct_count == len(secret_words):
            correct_word = True
            # Remove the space so you cannot guess it again as it will be shown
            # to the guesser (so space will show up in the word without having to guess it)
            alphabet.remove(' ')
        # Else you will have to re-type the secret_word
        else:
            print("Sorry you used characters that are not in this list: ")
            print(alphabet)
            print("Please try again")
            secret_words = input("Secret word: ").lower()


# Calls the function
check_if_secret_word_is_good(secret_word)

# This 'clears' the interpreter console (prints 100 spaces)
# It means you cannot see the secret_word, unless you scroll to the top
print("\n" * 100)


# A new array is filled with "_" (the amount of times that there are letters)
# So "hi" = ['_', '_']
def check_special_char():
    i = 0
    for x in secret_word:
        correct_guesses.append("_")
        # Any spaces used in the word will be shown as ' ' instead of '_'
        if x == " ":
            correct_guesses[i] = " "
        # Any apostrophes used in the word will be shown as "'" instead of '_'
        if x == "'":
            correct_guesses[i] = "'"

        # Each letter of the secret word gets put into an array so "hi" = ['h', 'i']
        full_word.append(x)

        i += 1


# Calls the function
check_special_char()

# To show how many letters you have to guess
print(correct_guesses)


# Function that checks if you got a correct guess
def playing(total_guesses):
    # user will guess a letter (and makes sure the letter is lower case
    guess = input("Guess a letter: ").lower()

    # Used to keep track if the guess is correct
    good_guess = 0
    # Will check each letter to each character in the alphabet
    for x in range(0, len(alphabet)):
        if alphabet[x] == guess:
            good_guess += 1
    # If the guess is not a one string letter (available in the alphabet),
    # it will make you guess again
    if good_guess == 0:
        while good_guess == 0:
            print("Sorry you can guess from these characters: ")
            print(alphabet)
            guess = input("Guess a letter: ").lower()
            # The code is repeated from above so the loop can keep checking if
            # the user tries to re-enter the same letter multiple times
            for x in range(0, len(alphabet)):
                if alphabet[x] == guess:
                    good_guess += 1
    # When the guess is correct (matches a letter in the alphabet), that letter will be
    # removed from the alphabet (so it cannot be guessed again) and the user will be
    # able to guess another letter
    if good_guess > 0:
        alphabet.remove(guess)

    # The above code also stops any strings of length 2+ or 0 to be used, so you don't need
    # more statements to check if the guess you used is within the correct scope

    j = 0
    count = 0
    # needed so you do not get an extra life with every double (or more) letter
    count2 = 0
    for letter in secret_word:
        # If the letter guessed is correct, the correct_guesses array will show where
        # the guessed letter appears
        if letter == guess:
            correct_guesses[j] = guess
            # Count is updated to check if the incorrect_guesses array needs to be filled
            # if the guessed letter is correct, it will not appear in this array
            count += 1
            count2 += 1
            total_guesses += 1
        j += 1

    # If there are multiple letters in the word, this will take away the extra goes given
    # So for the word hello, you will have 7 tries if you guess 'l' instead of 8
    if count2 >= 2:
        total_guesses -= (count2 - 1)

    # If the letter does not appear in the word, it will appear in the wrong guess array
    # and tell the player the wrong guesses they have already made
    if count == 0:
        incorrect_guesses.append(guess)

    # Each time a guess is made the correct and incorrect letters will be displayed to the screen
    print()
    print("Correct guesses: ", correct_guesses)
    print()
    print("Incorrect letters guessed: ", incorrect_guesses)
    print()

    # Returns total_guesses, so if a letter is guessed correctly your guesses will not go down
    return total_guesses


# Function for if you will win or loose
def win_or_loose():
    # You have the amount of guesses the word is + 2, so for the word 'tree' you have 6 guesses
    total_guesses = 7
    i = 0
    while i < total_guesses:
        print("You have: ", total_guesses, " guesses left")

        # Calls the function to guess the letters
        total_guesses = playing(total_guesses)

        # If the word is guessed correctly you win, and the secret word is printed
        if full_word == correct_guesses:
            print(" ")
            print("You won! The secret word was:", secret_word)
            break
        # To take down the amount of guesses you have after each guess
        total_guesses -= 1

    # If you did not guess the word you loose, and the secret word is printed
    if full_word != correct_guesses:
        print(" ")
        print("Sorry you didn't guess the word, the word was:", secret_word)


# Calls the function
win_or_loose()
