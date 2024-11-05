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
word = ['nails','sigma','bussin','skibidi','big back' , 'rizz' , 'fanum tax'] 

wordChoice = random.choice(word)
for x in word:
  if x == random:
     print(x)
#the player has to guess a letter-sawyer(LOOP)
correctLetter = ["i", "d", "n", "a", "l", "s", "b", "c", "k", "f", "t", "m", "z", "u"]
notletter = ["e", "h", "j", "o", "p", "y", "w", "q",]
guess = 5
finalGuess = 6
for letter in word:
  theGuess = [input("guess a letter:")]
  if theGuess == correctLetter:
    print("this is right")
  if theGuess != correctLetter:
    print("x\n", "this is incorrect try again")
if finalGuess == wordChoice:
   print("you got it")

#if its correct the letter will print and they will play again-sawyer(CONDITONAL)

#if its wrong then its a x will print on the screen and they have to guess again-sawyer(CONDITONAL))(a function will be added)

#if its wrong then its a x will print on the screen and they have to guess again-sawyer(CONDITONAL))(a function will be added)
#if player 1 gets it wrong six times they die - jayda(CONDITIONALS)
if guess and finalGuess<= 6:
    print("you have used up all your guess\n")
#if the player gets it all right they win - jayda(VARIABLE)(Add a function)
if word == wordChoice:
   print("you have won the game")

#a play agian option is printed on the screen- jayda(VARIABLE)
inp = [input("do you want to play again:")]
yes = [inp("yes")]
no = [inp("no")]
if yes:
   print("click run again")
else:
   print("get out of here")
 



