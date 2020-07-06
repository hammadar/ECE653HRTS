import Boolean
import BV
import smtPair
import sys
import random

class smtAssertion:

    smtBooleans = []
    operations = []
    smtPairs = [None] * 2
    depth = [None] * 2

    def __init__(self, smtBooleans,smtConstructs, type, depth=2):

        if smtBooleans is None:
            sys.stderr.write("Error in inputs\n")
            return

        self.smtBooleans = smtBooleans
        self.operations=smtConstructs
        self.type = type
        self.generatePairs(bvBinaryPredicate=False,k=0,depth=depth)
        

    def generatePairs(self, bvBinaryPredicate, k=0,depth=2): #k is necessary since the BV version requires two statements to compare
        numPairs = random.choice(range(1,depth))
        self.smtPairs[k] = self.generateNewPairs(0, numPairs, bvBinaryPredicate)
        self.depth[k]= numPairs


    def outputAssertion(self,bvBinaryPredicate, regenerate=True): #added regenerate to differentiate cases where you're reproducing the assertion to mutate
        
        if self.type == "Boolean":
            assertion = "(assert "
            assertion += self.smtPairs[0].outputPair()
            assertion += ")\n"
        elif self.type == "BV":
            if(bvBinaryPredicate == True):
                assertion = "(assert "
                regenerate = False
            else:
                assertion = "(assert (= "
            assertion += self.smtPairs[0].outputPair()
            assertion += " " #might need to remove - HR
            if regenerate: #for case of BV where you need to compare two statements
                self.generatePairs(bvBinaryPredicate,k=1)
            if(bvBinaryPredicate == False):
                assertion += self.smtPairs[1].outputPair()
                assertion += "))\n"
            else:
                assertion += ")\n"

        return assertion

    def generateNewPairs(self, i, numPairs, bvBinaryPredicate):
        left = random.choice([False, True])
        pair = smtPair.smtPair(self.type)
        innerPair = smtPair.smtPair(self.type)

        if (left):
            innerPair.setLHS(random.choice(self.smtBooleans)) #incorporate negation
            innerPair.left_neg = random.choice([True, False])
            innerPair.setRHS(random.choice(self.smtBooleans))
            innerPair.right_neg = random.choice([True, False])

            if(self.type == "Boolean"):
                innerPair.setOperation(random.choice(self.operations))
                pair.setLHS(innerPair)
                pair.setOperation(random.choice(self.operations))
                pair.left_neg = random.choice([True, False])
            else:
                innerPair.setOperation(random.choice(self.operations[random.getrandbits(1)]))
                pair.setLHS(innerPair)
                if (bvBinaryPredicate == True):
                    pair.setOperation(random.choice(self.operations[2]))
                else:
                    pair.setOperation(random.choice(self.operations[random.getrandbits(1)]))
                pair.left_neg = random.choice([True, False])
            
            if i == (numPairs-1):
                pair.setRHS(random.choice(self.smtBooleans))
                pair.right_neg = random.choice([True, False])
            else:
                pair.setRHS(self.generateNewPairs(i+1, numPairs, bvBinaryPredicate))
                pair.right_neg = random.choice([True, False])
            return pair
        else:
            pair.setLHS(random.choice(self.smtBooleans))
            pair.left_neg = random.choice([True, False])
            if(self.type == "Boolean"):
                pair.setOperation(random.choice(self.operations))
            else:
                if (bvBinaryPredicate == True):
                    pair.setOperation(random.choice(self.operations[2]))
                else:
                    pair.setOperation(random.choice(self.operations[random.getrandbits(1)]))
            pair.setRHS(random.choice(self.smtBooleans))
            pair.right_neg = random.choice([True, False])
            if i == (numPairs-1):
                pair.setRHS(random.choice(self.smtBooleans))
                pair.right_neg = random.choice([True, False])
            else:
                pair.setRHS(self.generateNewPairs(i+1, numPairs, bvBinaryPredicate))
                pair.right_neg = random.choice([True, False])
            return pair

    def mutate_operator(self, operator):
        if self.type == "Boolean":
            booleanConstruct = Boolean.BooleanConstruct()
            if operator not in booleanConstruct.allowableConstructs[:]:
                raise Exception("Illegal operator for type Boolean\n")
                return
            self.smtPairs[0] = self.boolean_mutate(self.smtPairs[0], operator) #booleans don't need a comparator, so only work on level 0



        elif self.type == "BV":
            bVConstruct = BV.BVConstruct()
            #allowablestuff = bVConstruct.allowableConstructs[:]
            if not any(operator in subl for subl in bVConstruct.allowableConstructs):
                raise Exception("Illegal operator for type BV\n")
                return
            allowableConstructs = bVConstruct.allowableConstructs
            for i in range(len(self.smtPairs)):
                self.smtPairs[i] = self.bV_mutate(self.smtPairs[i], operator, allowableConstructs)





    def boolean_mutate(self, pair, operator):
        mutate = random.choice([False, True])
        if mutate:
            pair.operation = operator
        if isinstance(pair.lhs, smtPair.smtPair):
            pair.lhs =  self.boolean_mutate(pair.lhs, operator)
        if isinstance(pair.rhs, smtPair.smtPair):
            pair.rhs = self.boolean_mutate(pair.rhs, operator)
        return pair

    def bV_mutate(self, pair, operator, allowableConstructs):
        mutate = random.choice([False, True])
        if mutate:
            if operator in allowableConstructs[0] and pair.operation in allowableConstructs[0]:
                pair.operation = operator
            elif operator in allowableConstructs[1] and pair.operation in allowableConstructs[1]:
                pair.operation = operator

        if isinstance(pair.lhs, smtPair.smtPair):
            pair.lhs =  self.bV_mutate(pair.lhs, operator, allowableConstructs)
        if isinstance(pair.rhs, smtPair.smtPair):
            pair.rhs =  self.bV_mutate(pair.rhs, operator, allowableConstructs)

        return pair

    def resetPairs(self):
        self.smtPairs = [None]*2
        self.depth = [None]*2



