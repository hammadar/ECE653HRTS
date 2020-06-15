from abc import ABC, abstractmethod
import TheoryInterface as tI

class BooleanConstruct(tI.Construct):
    def __init__(self, construct):
        self.allowableConstructs = ["true", "false", "not", "=>", "and", "or", "xor", "par (A)"]

        if construct in self.allowableConstructs:
            self.construct = construct
        else:
            raise Exception("Incorrect construct for type Bool\n")

    def theory(self):
        return "Core"

    def sort(self):
        return "Bool"

    def __str__(self):
        return str(self.construct) + " "

class BooleanLiteral(tI.Literal):
    def __init__(self, name):
        for character in name:
            if ord(character) not in range(33, 127):
                raise Exception("Illegal literal name.\n")
        self.name = name
        self.con

    def theory(self):
        return "Core"

    def sort(self):
        return "Bool"

    def gen(self):
        return "(declare-fun " + self.name + " () Bool)\n"

    def __str__(self, negation=False):
        if (not negation):
            return self.name
        return "not " + self.name

