import random

__upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
__lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz"
__symbol_list = """~`!@#$%^&*()_-+={[}]|\:;"'<,>.?/"""
__digit_list = "0123456789"

def __catchErrors(c:int, d:int,s:int):
    assert (c >= 0), "Character count cannot be lower than zero"
    
    assert (d >= 0), "Digit count cannot be lower than zero"
    
    assert (s >= 0), "Symbol count cannot be lower than zero"
    
    assert (c >= d+s), "You cannot use digits and symbols more than character count."

# This generates a new string from a given wordlist
def __generateStr(wordlist:str, targetCount:int) -> str:
    temp_word = ""
    for _ in range(targetCount):
        temp_word += wordlist[random.randint(0,len(wordlist)-1)]
    return temp_word

# Used this to randomize every aspect of selection in our sum word list (all digits, symbols, letters)
def __randomizeStr(wordlist:list) -> str:
    temp_word = ""
    while(len(wordlist) > 0):
        temp_rnd = random.randint(0,len(wordlist)-1)
        temp_word += wordlist[temp_rnd]
        del wordlist[temp_rnd]
    return temp_word

# Main generator function
def generatePassword(charCount:int,digitCount:int,symbolCount:int,allowUpper:bool) -> str:
        __catchErrors(charCount,digitCount,symbolCount)
        letterCount = charCount - (digitCount+symbolCount)
        letters = __generateStr(__upperCaseLetters+__lowerCaseLetters,letterCount) if allowUpper else __generateStr(__lowerCaseLetters,letterCount)
        symbols = __generateStr(__symbol_list,symbolCount)
        digits = __generateStr(__digit_list,digitCount)
        password =  __randomizeStr(list(letters+symbols+digits))
        return password