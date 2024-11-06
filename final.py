#When game starts a random word is generated-Kathryn(function)

print("Welcome to Brainrot Hangman!")
import random 
 #then a hangman board is printed on the screen-kahtryn(VARIABLE)
print("  ___________")
print("  |")
print("  |")
print("  |")
print("  |")
print("  |")
print("_____________")
#the slots for the word will apper-kathryn(CONDITIONAL)
wordchoice = ['nails','sigma','bussin','skibidi','big back' , 'rizz' , 'fanum tax'] 
def game(wordchoice):
   pass
wordChoice = random.choice(wordchoice)
word = game

#the player has to guess a letter-sawyer(LOOP)
correctLetter = ["i", "d", "r", "n", "a", "l", "s", "b", "c", "k", "f", "t", "m", "z", "u"]
notLetter = ["e", "h", "j", "o", "p", "y", "w", "q"]
guess = 6
for correctLetter in wordchoice:
   theGuess = input("guess a letter:")

#if its correct the letter will print and they will play again-sawyer(CONDITONAL)
   if theGuess in correctLetter:
      print("this is right")
#if its wrong then its a x will print on the screen and they have to guess again-sawyer(CONDITONAL))(a function will be added)
   else:
      print("x\n", "this is incorrect try again")
#if player 1 gets it wrong six times they die - jayda(CONDITIONALS)
if guess<= 5:
    print("you have used up all your guess\n")
#if the player gets it all right they win - jayda(VARIABLE)(Add a function)
wordGuess = input("final guess is to guess a word:")
if wordGuess is wordchoice:
   print("you have won the game")
else:
   print("you got it wrong")

#a play agian option is printed on the screen- jayda(VARIABLE)
inp = input("do you want to play again:")
if inp == "yes":
   print("please rerun")
else:
   print("please leave")