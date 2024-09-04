# Cybbbber
def repeat_center(string: str, number: int) -> str:
    MIDDLE = len(string) // 2
    MIDDLE_LETTER = string[MIDDLE]
    return string[0:MIDDLE] + MIDDLE_LETTER*number + string[MIDDLE+1:]


x = "Cyber"
n = 4
# print(repeat_center(x, n))
# print(repeat_center("Hello", 3))
# print(repeat_center("World", 5))
# =================================================


def repeat_half_n_times(sentence: str, n: int) -> str:
    MIDDLE = len(sentence) // 2
    first = sentence[0:MIDDLE]
    last = sentence[MIDDLE:]
    return first*n + last*n

# result = repeat_half_n_times("Hello world", 4)
# print(result)
# =================================================
# test@gmail.com   ==   te*******l.com


def encrypt_email(email: str) -> str:
    index_of_at = email.index("@")
    index_of_last_dot = email.rindex(".")

    first_part = email[:index_of_at-2]
    last_part = email[index_of_last_dot-1:]
    len_of_hidden_part = len(email) - len(first_part+last_part)
    return first_part + ("*"*len_of_hidden_part) + last_part


# print(encrypt_email("alisherxujanov163@gmail.com"))
# print(encrypt_email("test@mail.com"))
# =================================================
# "This is test universe" == >  "uuuuuThis is test universeuuuuu"
def repeat_first_letter_of_last_word(sentence: str) -> str:
    splitted_words = sentence.split(" ")
    fst_letter_of_last_word = splitted_words[-1][0]
    return fst_letter_of_last_word*5 + sentence + fst_letter_of_last_word*5

# r = repeat_first_letter_of_last_word("This is test universe")
# print(r)

# =================================================
def change_vowels_into_symbols(sentence:str, symbol:str="$") -> str:
    vowels = "auioe"
    result = ""
    for letter in sentence:
        if letter.lower() in vowels:
            result += symbol
        else:
            result += letter
    return result

text = "This is test text of vowels"
text2 = "Hello world"
text3 = "Cyber Academy of Python"
# print(change_vowels_into_symbols(text))
# print(change_vowels_into_symbols(text2))
# print(change_vowels_into_symbols(text3))

# =================================================
text = "This is test text of universe"
def change_last_letter_to_upper(sentence:str) -> str:
    ...


# =================================================
def factorial(num:int) -> int:
    if num == 1:
        return 1 
    return num * factorial(num-1)
    # 5 * 4 * 3 * 2 * 1

# print(factorial(5))  # 120
# print(factorial(10)) # 3628800

# =================================================
# HOMEWORK
# 1. FIBONACCI with recursion and for loop
# 0, 1
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
# def fibonacci(n:int) -> int:
#     """Upto n-th element"""
#     pass

# fibonacci(50)  # 1, 2, 3, 5, 8, 13, 21, 34
# fibonacci(100) # 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/
# 2. 
#         -- 5 --
#    *             *
#    **           **
#    ***         ***
#    ****       ****
#    *****     *****
# --------------------------
#    *****     *****
#    ****       ****
#    ***         ***
#    **           **
#    *             *
# --------------------------
# =/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/=/
# 3. You have a text that can contain same latters in one place. 
#    ex: 
#       "Hello world"  => ll
#       "moon"         => oo
#       "Cyber"        => ""
# 