
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

        if (isinstance(self.lhs, smtPair)):
            expressionToReturn += self.lhs.outputPair()
        else:
            expressionToReturn += self.lhs.__str__()

        expressionToReturn += " "

        if (isinstance(self.rhs, smtPair)):
            expressionToReturn += self.rhs.outputPair()
        else:
            expressionToReturn += self.rhs.__str__()

        expressionToReturn += ")"
        return expressionToReturn