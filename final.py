#When game starts a random word is generated-Kathryn(function)

print("Welcome to Hangman!")
import random 
wordcheck =""
win=0 
things_left = 6

def game():
    global things_left

    global guessuedLetters
    global choseWord
    print("a new word was chosen") 
    #then a hangman board is printed on the screen-kahtryn(VARIABLE) 
    print("  ___________")  
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print("  |")
    print("_____________")
#the slots for the word will apper-kathryn(CONDITIONAL)
words = ["Rose", "sigmas", "bussin", "Lavender", "tulip", "risk"] 
word = game
guessuedLetters = []
choseWord = random.choice(words)
wordcheck = ""
def things():
    global things_left

    global guessuedLetters
    global choseWord
    print("a new word was chose")
    
    
    
    
    guessuedLetters = []
    choseWord = random.choice(words)
    wordcheck = ""
    things_left = 6
    things()
def restart():
    blank = ""
    answer = input("Restart (y/n):")
    if answer == "y":
        restart()
    elif answer == "n":
        exit()
    restart()



 

#the player has to guess a letter-sawyer(LOOP)
correctLetter = ["i", "d", "r", "n", "a", "l", "s", "b", "c", "k", "f", "t", "m", "z", "u"]
notLetter = ["e", "h", "j", "o", "p", "y", "w", "q"]
guess = 6
# for correctLetter in words:
#kathryns code
# blank = ""
# for letter in choseWord:
#     blank += "_ "
choseLetters = list(choseWord)
# print(blank)
# for letter in choseLetters:
#     theGuess = input("guess a letter:")
#     # print (blank)
#     if theGuess in choseLetters:
#         new_blank = [letter if theGuess == letter else '_' for letter in choseLetters]
#         print(" ".join(new_blank))
#     else:
#         print("bad guess try again")
#         update_display = 0

current_guess = ["_" for letter in choseLetters]
print(" ".join(current_guess))

wrong_guess = 0
while wrong_guess <6:
    theGuess = input("Choose a letter bro/sis: ")
    if theGuess not in choseLetters:
        print("The letter you picket is WRONG...try again")
        if wrong_guess==5:
            print("You've failed too many times! Please Leave! NOW")
        wrong_guess+=1

    else:
        for i,letter in enumerate(choseLetters):
            if letter == theGuess:
                current_guess[i]=letter
        print(" ".join(current_guess))
        if "".join(current_guess)==choseWord:
            print("NAILD IT!")   

    
 

#if its correct the letter will print and they will play again-sawyer(CONDITONAL) 
if theGuess in choseWord:   
      print("this is right") 
#its wrong then its a x will print on the screen and they have to guess again-sawyer(CONDITONAL))(a function will be added)

else:
       print("x\n", "this is incorrect try again")
#if player 1 gets it wrong six times they die - jayda(CONDITIONALS)
if guess<= 6:
    print("you have used up all your guess\n")
#if the player gets it all right they win - jayda(VARIABLE)(Add a function)
wordGuess = input("final guess is to guess a word:")
if wordGuess == choseWord:
   print("you have won the game")
else:
   print("you got it wrong")
answer = input("Restart (y/n):")
#a play agian option is printed on the screen- jayda(VARIABLE)
if answer == "y":
   print("rerun to replay")
else:
   print("please leave")

