#this will be a hangman game focused on marine animals
print ("welcome to hangman if you love marine life this will be a fun guessing game")
word = "fish"
attempts_remaining = 5
print("the word has", len(word), "letters. ")
while attempts_remaining > 0:
    guess= input("Guess a letter: ")
    if guess =="f":
        print("f___")
    elif guess=="i":
        print("_i__")
    elif guess =="s":
        print("__s_")
    elif guess =="h":
        print("___h")
    else:
        attempts_remaining = attempts_remaining - 1
        print("wrong letter, try again!")
        print("Attempts remaining:", attempts_remaining)
    if guess == word:
        print("Congrats you did it!")
        break
if attempts_remaining==0:
    print("GG the word was", word)
