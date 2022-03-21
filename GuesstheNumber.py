import random

def startGame():
  number = random.randrange(1, 1000)
  guess = int(input("Guess a number between 1 and 1000 with the fewest guesses: "))
  guessCount = 1

  while guess != number:
          if guess < number:
              print("Too low.  Try again.")
              guess = int(input("\nGuess a number between 1 and 1000 with the fewest guesses: "))
              guessCount = guessCount + 1
          else:
              print("Too high.  Try again.")
              guess = int(input("\nGuess a number between 1 and 1000 with the fewest guesses: "))
              guessCount = guessCount + 1

  print("Congratulations.  You guessed the number!")
  print("Your Number of Guesses: ", guessCount)
  print("Play again? ")

  repeatGame()

def repeatGame():
  Restart = input("Yes or No: ")
  if Restart == "Yes":
    startGame()
  elif Restart == "No":
    print("Have a good day!")
    exit()

startGame()