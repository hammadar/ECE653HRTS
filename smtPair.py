import random

class smtPair:
    lhs = None
    left_neg = None
    rhs = None
    right_neg = None
    third = None
    operation = None

    def __init__(self, type="Boolean"):
        self.type=type

    def setLHS(self, lhs):
        self.lhs = lhs

    def setRHS(self, rhs):
        self.rhs = rhs

    '''def setThird(self, third):
        if self.type == "Boolean":
            raise Exception("Cannot add third variable with type {}\n")
            return
        self.third = third'''

    def setOperation(self, operation):
        self.operation = operation
        print("operation=",operation)

    def outputPair(self):

        expressionToReturn = "(" + self.operation.__str__() + " "

        if self.type == "Boolean":
            negation = "not"
        else:
            negation = "bvnot"

        if (isinstance(self.lhs, smtPair)):
            expressionToReturn += self.lhs.outputPair()
        else:
            if not self.left_neg:
                expressionToReturn += self.lhs.__str__()
            else:
                expressionToReturn += "(" + negation + " " + self.lhs.__str__() + ")"

        expressionToReturn += " "

        if (isinstance(self.rhs, smtPair)):
            expressionToReturn += self.rhs.outputPair()
        else:
            if not self.right_neg:
                expressionToReturn += self.rhs.__str__()
            else:
                expressionToReturn += "(" + negation + " " + self.rhs.__str__() + ")"

        expressionToReturn += ")"
        return expressionToReturn



