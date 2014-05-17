import random ##imports the random library so i can have the computer pick a random word




computerBank = ["responsible" , "easy" , "duck" , "function" , "terrible"]
computerWord = random.choice(computerBank)
count_timer = 1
word = []
incorrectGuesses = []





lives = 0
noOfGuesses = input("How Smart are you feeling? Would you like to play Easy, or Hard? ")

noOfGuesses_upper = str(noOfGuesses.upper())
print(noOfGuesses_upper)
if noOfGuesses_upper == "EASY":
    lives = 8
    print("Very Well. You now have " , lives , " lives")
    print("So as not to be mean, this word has " + str(len(computerWord)) + " letters.") 


    
    ##blank array, contains database of the word the user has guessed thus far.





    userGuess = input("Pick a letter please ")
    if (userGuess in computerWord):
        print("Correct!")
        print("You still have " , lives , "left")
        print("this letter is in the number" , computerWord.index(userGuess),"space")
        word.append(userGuess)
        print("So far you have", word)
        print()
    elif len(str(userGuess)) > int(1):
        print("One letter at a time please")
    elif not(userGuess.isalpha()):
        print("Only letters please")
        
    else:
        print("Too bad, please choose again. You are penalized a life.")
        lives -=1
        print("You have",lives,"left.")
        print(lives)
        incorrectGuesses.append(userGuess)
        print()


    while len(word) != len(computerWord):
        userGuess = input("Pick a letter please ")
        userGuess_lower = userGuess.lower()
        if (userGuess in word):
            print("You have already picked", userGuess, "Please choose again.")
        elif not(userGuess.isalpha()):
            print("Only letters please")
        elif (userGuess in incorrectGuesses):
            print("You have already picked", userGuess, "Please choose again.")
            ## First 2 checks so the user can't enter the same letters over and over
        elif len(str(userGuess)) > int(1):
            print("One letter at a time please")
        elif (userGuess in computerWord):
            print("Correct!")
            print("You still have " , lives , "left")
            print("this letter is in the number" , computerWord.index(userGuess),"space")
            word.append(userGuess)
            print(word)
            print()
        else:
            print("Too bad, please choose again. You are penalized a life.")
            lives -=1
            print("You have",lives,"left.")
            incorrectGuesses.append(userGuess)
            print()
            if lives <1:
                print("Game over! Better luck next time!")
                print("The word was", computerWord)
                break;
        
    else:
        print("Yes! The word is", computerWord, "You Win!")

elif noOfGuesses_upper == "HARD":
    lives = 5
    print("Very Well. You now have " , lives , " lives")
    print("So as not to be mean, this word has " + str(len(computerWord)) + " letters.") 


    
    ##blank array, contains database of the word the user has guessed thus far.





    userGuess = input("Pick a letter please ")
    if (userGuess in computerWord):
        print("Correct!")
        print("You still have " , lives , "left")
        print("this letter is in the number" , computerWord.index(userGuess),"space")
        word.append(userGuess)
        print("So far you have", word)
        print()
    elif len(str(userGuess)) > int(1):
        print("One letter at a time please")
    elif not(userGuess.isalpha()):
        print("Only letters please")
        
    else:
        print("Too bad, please choose again. You are penalized a life.")
        lives -=1
        print("You have",lives,"left.")
        print(lives)
        incorrectGuesses.append(userGuess)
        print()


    while len(word) != len(computerWord):
        userGuess = input("Pick a letter please ")
        userGuess_lower = userGuess.lower()
        if (userGuess in word):
            print("You have already picked", userGuess, "Please choose again.")
        elif not(userGuess.isalpha()):
            print("Only letters please")
        elif (userGuess in incorrectGuesses):
            print("You have already picked", userGuess, "Please choose again.")
            ## First 2 checks so the user can't enter the same letters over and over
        elif len(str(userGuess)) > int(1):
            print("One letter at a time please")
        elif (userGuess in computerWord):
            print("Correct!")
            print("You still have " , lives , "left")
            print("this letter is in the number" , computerWord.index(userGuess),"space")
            word.append(userGuess)
            print(word)
            print()
        else:
            print("Too bad, please choose again. You are penalized a life.")
            lives -=1
            print("You have",lives,"left.")
            incorrectGuesses.append(userGuess)
            print()
            if lives <1:
                print("Game over! Better luck next time!")
                print("The word was", computerWord)
                break;
        
    else:
        print("Yes! The word is", computerWord, "You Win!")
elif not(noOfGuesses_upper.isalpha()):
    lives = 5
    print("Run me again when you want to play")
else:
    print("Run me again when you want to play")


    
    


















