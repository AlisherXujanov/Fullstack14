# Поле Чудес  |  Mystery Word

# [10 random english words with their meanings and definitions]
# get 1 random word from these words and show the user its definition
# ask a user to guess a letter
# The user has initially 5 lives
# If the letter that user guessed is right and exists in the word
#     Show the word with the letter that user guessed
# ex:   word==banana,    guess==a,    output==_a_a_a
# If the letter that user guessed is wrong
#     Subtract 1 from lives

# So on, until the user finds the word or loses all the lives!
import random

QUESTIONS = {
    "question1": {
        "text": "Apple",
        "explanation": "Round and sweet fruit"
    },
    "question2": {
        "text": "Phone",
        "explanation": "A device to make calls"
    },
    "question3": {
        "text": "Laptop",
        "explanation": "A portable computer"
    }
}

KEY = random.choice(list(QUESTIONS.keys()))
QUESTION = QUESTIONS[KEY] # {...}

TEXT = QUESTION['text']
EXPLANATION = QUESTION['explanation']

lives = 5
found_letters_pool = ""



def show_text(text:str) -> None:
    print("===========================================================")
    print("===========================================================")
    print("-------------------------------------")
    print(text)
    print("-------------------------------------")


HIDDEN_TEXT = "_" * len(TEXT) 


while lives > 0:
    if "_" not in HIDDEN_TEXT:
        show_text(f"Congratulations! You found the word: {TEXT}")
        break
    
    letter = input(f"""
EXPLANATION: {EXPLANATION}
-----------------------------                   
WORD: {HIDDEN_TEXT}
-----------------------------
YOU HAVE {lives} LIVES
-----------------------------
Pick a letter: """).lower()

    if letter in found_letters_pool:
        show_text("You already guessed this letter!")
        continue
    else:
        found_letters_pool += letter


    if letter.isalpha() and len(letter) == 1:
        if letter in TEXT.lower():
            show_text("CORRECT! Continue...")
            new_text = ""
            for i in range(len(TEXT)):
                # -----------------------
                # "Apple"  => p
                # "_pp__"

                # "Apple"  => e
                # "_pp_e"
                # -----------------------
                if letter == TEXT[i].lower():
                    new_text += TEXT[i]
                else:
                    new_text += HIDDEN_TEXT[i]
            HIDDEN_TEXT = new_text
        else:
            show_text("Wrong! Try again!")
            lives -= 1
    elif letter.isalpha() and len(letter) > len(TEXT):
        if letter == TEXT.lower():
            show_text(f"Congratulations! You found the word: {TEXT}")
            break
    else:
        print("Wrong!")
        show_text("Please enter a valid letter!")
        continue
        
        
if lives == 0:
    show_text("GAME OVER! You lost all your lives!")
    print(f"The word was: {TEXT}")


# ''.isnumeric()
# ''.isdigit()
# ''.isalpha()
# ''.isalnum()

