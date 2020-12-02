import math
import random

class createLevel:

    def __init__(self, word):
        self.gameDetails(word)
        self.visiblilty = [False for _ in range(self.length)]
        for i in range(self.visibleLetter):
            self.visiblilty[random.randint(0,self.length-1)] = True
        for i in range(self.length):
            if self.word[i] == " ":
                self.visiblilty[i] = True

    
    def gameDetails(self, word):
        self.length = len(word)
        self.visibleLetter = math.floor(self.length/2)
        self.score = self.length*10
        self.word = word
        self.guessCount = math.ceil(self.length/2)

    def generateScreen(self):
        for x in range(len(self.word)):
            if self.visiblilty[x]:
                print(" " + self.word[x] + " ", end="")
            else:
                print(" _ ",end="")
    
    def takeGuess(self, guess):
        flag = False
        for x in range(len(self.word)):
            if self.word[x] == guess:
                self.visiblilty[x] = True
                flag = True
            else:
                pass
        if not flag:
            self.guessCount -= 1
        return flag
    
    def gameComplete(self):
        for x in self.visiblilty:
            if not x:
                return False
        return True
    
    def calcScore(self):
        finalscore = self.score + (self.guessCount-1)*5
        return finalscore
        
