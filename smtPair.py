import random

class smtPair:
    lhs = None
    left_neg = None
    rhs = None
    right_neg = None
    extras = None
    extras_neg = None
    operation = None
    subNodes = None
    subNodes_neg = None

    def __init__(self, type="Boolean", arity = 2):
        self.type=type
        self.arity = arity

    def setLHS(self, lhs):
        self.lhs = lhs

    def setRHS(self, rhs):
        self.rhs = rhs

    def setExtras(self, extras):
        if self.type == "Boolean":
            raise Exception("Cannot add third variable with type {}\n".format(self.type))
            return
        elif self.type == "BV":
            self.extras = extras

    def setSubNodes(self, subnodes):
        if len(subnodes) != self.arity:
            raise Exception("Number of subnodes does not match current operator\n")
        self.subNodes = subnodes
        self.subNodes_neg = random.sample([True, False], len(subnodes))


    def setOperation(self, operation):
        self.operation = operation

    def outputPair(self):
        expressionToReturn = "(" + self.operation.__str__() + " "

        if self.type == "Boolean":
            negation = "not"
        else:
            negation = "bvnot"
        for i in range(len(self.subNodes)):
            subNode = self.subNodes[i]
            neg = self.subNodes_neg[i]

            if(isinstance(subNode, smtPair)):
                expressionToReturn += subNode.outputPair()
            else:
                if not neg:
                    expressionToReturn += subNode.__str__()
                else:
                    expressionToReturn += "(" + negation + " " + subNode.__str__() + ")"
        expressionToReturn += ")"
        return expressionToReturn



    '''def outputPair(self):

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

        if self.extras is not None:
            for i in range(len(self.extras)):
                if (isinstance(self.extras[i], smtPair)):
                    expressionToReturn += self.extras[i].outputPair()
                else:
                    if not self.extras_neg[i]:
                        expressionToReturn += self.extras[i].__str__()
                    else:
                        expressionToReturn += "(" + negation + " " + self.extras[i].__str__() + ")"

        expressionToReturn += ")"
        return expressionToReturn'''



