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
letter = ["i", "d", "n", "a", "l", "s", "b", "c", "k", "f", "t", "m", "z", "u"]
wordChoice = random.choice(word)
for x in word:
  if x == random:
     print(x)
#the player has to guess a letter-sawyer(LOOP)
for letter in word:
      print(input("guess a letter:"))
      if letter in word:
          print("this is right")
      else:
          print("this is incorrect try again")
notletter = ["e", "h", "j", "o", "p", "y", "w", "q",]
#if its correct the letter will print and they will play again-sawyer(CONDITONAL)
for letter in wordChoice:
   print("it is in the word")
#if its wrong then its a x will print on the screen and they have to guess again-sawyer(CONDITONAL))(a function will be added)
else:
   print("THIS IS INCORRECT")
#if its wrong then its a x will print on the screen and they have to guess again-sawyer(CONDITONAL))(a function will be added)
#if player 1 gets it wrong six times they die - jayda(CONDITIONALS)
guess = 6
if guess <= 6:
    print("you guess 6 words 6 times\n")
#if the player gets it all right they win - jayda(VARIABLE)(Add a function)
win = input("you have won")
print("you won the game\n")
#a play agian option is printed on the screen- jayda(VARIABLE)
play = ("you can play again")
print("go play again\n")

 



