import random

class WordList:

    easy = []
    med = []
    dif = []

    def __init__(self):
        self.load()

    def load(self):
        easyFile = open("easy.txt", 'r')
        for word in easyFile:
            self.easy.append(word)
        easyFile.close()
        
        medFile = open("med.txt", 'r')
        for word in medFile:
            self.med.append(word)
        medFile.close()

        difFile = open("diff.txt", 'r')
        for word in difFile:
            self.dif.append(word)
        difFile.close()

    def addEasy(self,Ez):
        easy = open("easy.txt", 'a+')
        easy.write(Ez.upper())
        easy.close()
        self.load()

    
    def addMed(self, Med):
        med = open("med.txt", 'a+')
        med.write(Med.upper())
        med.close()
        self.load()
    
    def addDif(self, Dif):
        dif = open("diff.txt", 'a+')
        dif.write(Dif.upper())
        dif.close()
        self.load()

    def selectEasy(self):   
        randEasy = self.easy[random.randint(0, len(self.easy) - 1)]
        randEasy = randEasy.replace("\n", "")
        return randEasy

    def selectMed(self):    
        randMed = self.med[random.randint(0, len(self.med) - 1)]
        randMed = randMed.replace("\n", "")
        return randMed
      
    def selectDif(self):
        randDif = self.dif[random.randint(0, len(self.dif) - 1)]
        randDif = randDif.replace("\n", "")
        return randDif
     

