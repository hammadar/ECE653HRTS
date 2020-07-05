import Boolean
import BV
import smtAssertion
import sys
import random
import copy

class InputGenerator:
    def __init__(self, type):
        self.allowableLiterals = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.type = type
        self.setupConstructs()
        self.literals = []
        self.constructs = []
        self.assertions = []

    def setupConstructs(self):
        if self.type == "Boolean":
            BoolConstruct = Boolean.BooleanConstruct()
            self.allowableConstructs = BoolConstruct.allowableConstructs
            self.constructClass = BoolConstruct
        elif self.type == "BV":
            BVConstruct = BV.BVConstruct()
            self.allowableConstructs = BVConstruct.allowableConstructs
            self.constructClass = BVConstruct
        self.logic = self.constructClass.logic()

    def generateLiterals(self):
        literals_sample_size = random.randrange(2,25)
        if self.type == "Boolean":
            for literal in random.sample(self.allowableLiterals, literals_sample_size):
                self.literals.append(Boolean.BooleanVariable(literal))
        elif self.type == "BV":
            for literal in random.sample(self.allowableLiterals, literals_sample_size):
                self.literals.append(BV.BVVariable(literal, 32))

    def generateAssertions(self):
        assertion = smtAssertion.smtAssertion(self.literals, self.allowableConstructs, self.type)
        self.assertion = assertion


    def declareLiterals(self):
        for literal in self.literals:
            sys.stdout.write(literal.gen())

    def outputAssertions(self, num):
        for i in range(random.randrange(1,num)):
            bvBinaryPredicate=random.choice([False, True])
            self.assertion.generatePairs(bvBinaryPredicate)
            sys.stdout.write(self.assertion.outputAssertion(bvBinaryPredicate))
            self.assertions.append(copy.copy(self.assertion)) #store assertions with generated pairs for later mutation
            self.assertion.resetPairs()

    def mutateAssertions(self, operator):
        for i in range(len(self.assertions)):
            self.assertions[i].mutate_operator(operator)
        for assertion in self.assertions:
            sys.stdout.write(assertion.outputAssertion(False))




    def setLogic(self):
        sys.stdout.write(self.logic)

    def generateFile(self, num):
        self.generateLiterals()
        self.setupConstructs()
        self.setLogic()
        self.generateAssertions()
        self.declareLiterals()
        self.outputAssertions(num)
        sys.stdout.write("(check-sat)\n")

inputGenerator = InputGenerator("BV")
# inputGenerator = InputGenerator("Boolean")
inputGenerator.generateFile(5)
# inputGenerator.mutateAssertions("and")