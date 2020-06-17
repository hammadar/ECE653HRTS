import Boolean
import smtAssertion
import sys

literals = ["a", "b", "c", "d", "e", "f", "g", "h"]
constructs = ["true", "false", "not", "=>", "and", "or", "xor", "par (A)"]
booleanLiterals = []
booleanConstructs = []

for literal in literals:
    booleanLiterals.append(Boolean.BooleanLiteral(literal))

for construct in constructs:
    booleanConstructs.append(Boolean.BooleanConstruct(construct))

assertion = smtAssertion.smtAssertion(booleanLiterals,booleanConstructs)

for booleanLiteral in booleanLiterals:
    sys.stdout.write(booleanLiteral.gen())

sys.stdout.write(assertion.outputAssertion())

#useful for other theories like BV, strings etc