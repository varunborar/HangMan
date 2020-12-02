from WordList import WordList
from gameScreen import createLevel
from os import system
from time import sleep


def clearScreen():
    _ = system('cls')


def playLevel(score, word, levelNumber):
    level = createLevel(word)
    gameOver = False
    while not gameOver:
        clearScreen()
        print(f"\t\t\t\t\t Level {levelNumber}")
        print(f"Score: {score} \t\t\t\t\t\t\t\t Guess Left: {level.guessCount}")
        level.generateScreen()
        guess = input("\nEnter your guess: ").upper()
        level.takeGuess(guess)

        if level.guessCount <= 0:
            print(f"The word was {word}")
            gameOver = True
        elif level.gameComplete():
            level.generateScreen()
            score = score + level.calcScore()
            print("\nCongratulations! You guessed it right")
            sleep(1)
            return False, score
    return True, score


if __name__ == "__main__":
    clearScreen()
    userName = input("What should i call you ? ")
    clearScreen()
    userDifficulty = int(input(
        "What difficulty you want to play \n1. Easy \n2. Medium \n3. Difficult \nChoose (1/2/3): "))
    userScore = 0
    level = 1
    newWord = WordList()
    gameOver = False
    while not gameOver:
        word = ""
        if userDifficulty == 1:
            word = newWord.selectEasy()

        elif userDifficulty == 2:
            word = newWord.selectMed()

        elif userDifficulty == 3:
            word = newWord.selectDif()

        gameOver, userScore = playLevel(userScore, word, level)
        if not gameOver:
            level += 1

    print(f"Congrats {userName}! You guessed {level} words and you scored {userScore}")
