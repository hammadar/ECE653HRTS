import random

class smtPair:
    lhs = None
    rhs = None
    operation = None

    def __init__(self):
        pass

    def setLHS(self, lhs):
        self.lhs = lhs

    def setRHS(self, rhs):
        self.rhs = rhs

    def setOperation(self, operation):
        self.operation = operation

    def outputPair(self):
        expressionToReturn = "(" + self.operation.__str__() + " "
        left_neg = random.choice([False,True])
        right_neg = random.choice([False, True])

        if (isinstance(self.lhs, smtPair)):
            expressionToReturn += self.lhs.outputPair()
        else:
            if not left_neg:
                expressionToReturn += self.lhs.__str__()
            else:
                expressionToReturn += "(not " + self.lhs.__str__() + ")"

        expressionToReturn += " "

        if (isinstance(self.rhs, smtPair)):
            expressionToReturn += self.rhs.outputPair()
        else:
            if not right_neg:
                expressionToReturn += self.rhs.__str__()
            else:
                expressionToReturn += "(not " + self.rhs.__str__() + ")"

        expressionToReturn += ")"
        return expressionToReturn