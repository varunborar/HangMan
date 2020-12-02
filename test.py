from WordList import WordList
from os import system

newWord = WordList()


def clearScreen():
    _ = system('cls')


while True:
    print("\t\t\t\t\t\t\tWord Database")
    print("Select difficulty \n1. Easy \n2. Medium \n3. Difficult \n4. Exit \nChoose (1/2/3/4):")
    userDifficulty = int(input())
    word = input("Enter word: ").upper()
    if userDifficulty == 1:
        newWord.addEasy(word + "\n")

    elif userDifficulty == 2:
        newWord.addMed(word + "\n")

    elif userDifficulty == 3:
        newWord.addDif(word + "\n")  
    else:
        break
