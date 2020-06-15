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
