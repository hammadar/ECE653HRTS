import Boolean
import smtPair
import sys
import random

class smtAssertion:

    smtBooleans = []
    operations = []
    smtPairs = smtPair.smtPair

    def __init__(self, smtBooleans,smtConstructs, type):

        if smtBooleans is None:
            sys.stderr.write("Error in inputs\n")
            return

        self.smtBooleans = smtBooleans
        self.operations=smtConstructs
        self.type = type
        self.generatePairs()
        

    def generatePairs(self):
        numPairs = random.choice(range(1,2))
        self.smtPairs = self.generateNewPairs(0, numPairs)


    def outputAssertion(self):
        if self.type == "Boolean":
            assertion = "(assert "
            assertion += self.smtPairs.outputPair()
            assertion += ")\n"
        elif self.type == "BV":
            assertion = "(assert (= "
            assertion += self.smtPairs.outputPair()
            assertion += ""
            self.generatePairs()
            assertion += self.smtPairs.outputPair()
            assertion += "))\n"

        return assertion

    def generateNewPairs(self,i, numPairs):
        left = random.choice([False, True])
        pair = smtPair.smtPair(self.type)
        innerPair = smtPair.smtPair(self.type)

        if (left):
            innerPair.setLHS(random.choice(self.smtBooleans)) #incorporate negation
            innerPair.setRHS(random.choice(self.smtBooleans))
            innerPair.setOperation(random.choice(self.operations))
            pair.setLHS(innerPair)
            pair.setOperation(random.choice(self.operations))
            if i == (numPairs-1):
                pair.setRHS(random.choice(self.smtBooleans))
            else:
                pair.setRHS(self.generateNewPairs(i+1, numPairs))
            return pair
        else:
            pair.setLHS(random.choice(self.smtBooleans))
            pair.setOperation(random.choice(self.operations))
            pair.setRHS(random.choice(self.smtBooleans))
            if i == (numPairs-1):
                pair.setRHS(random.choice(self.smtBooleans))
            else:
                pair.setRHS(self.generateNewPairs(i+1, numPairs))
            return pair




