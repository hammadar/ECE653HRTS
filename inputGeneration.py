import Boolean
import smtAssertion
import sys
import random

literals = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
constructs = ["=>", "and", "or", "xor"]
logic = ""
booleanLiterals = []
booleanConstructs = []

for literal in literals:
    booleanLiterals.append(Boolean.BooleanVariable(literal)) #randomise picking of literals

for construct in constructs:
    booleanConstructs.append(Boolean.BooleanConstruct(construct))

sys.stdout.write(booleanConstructs[0].logic())

assertion = smtAssertion.smtAssertion(booleanLiterals,booleanConstructs)

for booleanLiteral in booleanLiterals:
    sys.stdout.write(booleanLiteral.gen())

for i in range(random.randrange(1,25)):
    assertion.generatePairs()
    sys.stdout.write(assertion.outputAssertion())

#sys.stdout.write(assertion.outputAssertion())
sys.stdout.write("(check-sat)")

#useful for other theories like BV, strings etc