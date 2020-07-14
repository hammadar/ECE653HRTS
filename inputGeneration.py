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
            self.arity = BoolConstruct.arity()
        elif self.type == "BV":
            BVConstruct = BV.BVConstruct()
            self.allowableConstructs = BVConstruct.allowableConstructs
            self.constructClass = BVConstruct
            self.arity = BVConstruct.arity()
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
        f = open("mutatedAssertions", "a")
        for literal in self.literals:
            generatedLiteral = literal.gen()
            sys.stdout.write(generatedLiteral)
            f.write(generatedLiteral)
        f.close()

    def outputAssertions(self, num):
        for i in range(random.randrange(1,num)):
            bvBinaryPredicate=random.choice([False, True])
            self.assertion.generatePairs(bvBinaryPredicate, depth=num, arity=self.arity)
            sys.stdout.write(self.assertion.outputAssertion(bvBinaryPredicate))
            self.assertions.append(copy.copy(self.assertion)) #store assertions with generated pairs for later mutation
            self.assertion.resetPairs()

    def mutateAssertions(self, operator):
        f = open("mutatedAssertions", "a")
        for i in range(len(self.assertions)):
            self.assertions[i].mutate_operator(operator)
        for assertion in self.assertions:
            if assertion.smtPairs[0].operation in self.allowableConstructs[1]:
                bvPredicate = True
            else:
                bvPredicate = False
            mutatedAssertion = assertion.outputAssertion(bvPredicate,regenerate=False)
            sys.stdout.write(mutatedAssertion)
            f.write(mutatedAssertion)
        f.close()

    def setLogic(self):
        f = open("mutatedAssertions", "w")
        sys.stdout.write(self.logic)
        f.write(self.logic)
        f.close()

    def generateFile(self, num):
        self.generateLiterals()
        self.setupConstructs()
        self.setLogic()
        self.generateAssertions()
        self.declareLiterals()
        self.outputAssertions(num)
        sys.stdout.write("(check-sat)\n")



inputGenerator = InputGenerator("BV")
#inputGenerator = InputGenerator("Boolean")
inputGenerator.generateFile(5)
inputGenerator.mutateAssertions("bvand")

f = open("mutatedAssertions", "a")
f.write("(check-sat)\n")
f.close()

'''TS - combine bitwise and arithmetic operation mutation into one level. Include all references
HR - aridity (number of inputs required for each oeprator). Add aridity attribute in interface, expand to BV and Boolean, then accomodate when generating assert statement
TS - flag for chainability (undetermined number of args for an operator)
HR - change mutate to only mutate one operator per assert statement. Will require smtAssertion traversal function. 
TS - change mutate to regenerate new complete file'''
