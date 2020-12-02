from WordList import WordList
from gameScreen import createLevel

newWord = WordList()

selectedWord = newWord.selectEasy()
level = createLevel(selectedWord)
n = level.guessCount

while n > 0:
    level.generateScreen()
    guess = input().upper()
    if not level.takeGuess(guess):
        n = n - 1
    if level.gameComplete():
        level.generateScreen()
        print("\nYou Won!")
        print(f"Your score is {level.calcScore()}")
        break

    

