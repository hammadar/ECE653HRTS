from abc import ABC, abstractmethod
import TheoryInterface as tI

class BVConstruct(tI.Construct):
    def __init__(self, construct):
        self.allowableConstructs = ["concat", "_ extract", "bvnot", "bvneg", "bvand", "bvor", "bvadd", "bvmul", "bvudiv", "bvurem", "bvshl", "bvlshr"]


    def setConstruct(self, construct):
        if construct in self.allowableConstructs:
            self.construct = construct
        else:
            raise Exception("Incorrect construct for type BV.\n")

    def theory(self):
        return "FixedSizeBitVectors"

    def sort(self):
        return "_ BitVec"

    def logic(self):
        return "(set-logic QF_BV)\n"

    def __str__(self):
        return self.construct

class BVVariable(tI.Variable):
    def __init__(self, name, size):
        for character in name:
            if ord(character) not in range(33, 127):
                raise Exception("Illegal literal name.\n")
            try:
                size = int(size)
                self.size = size
            except:
                raise Exception("Illegal size input for BV\n")
        self.name = name

    def theory(self):
        return "FixedSizeBitVectors"

    def sort(self):
        return "_ Bitvec"

    def gen(self):
        return "declare-fun " + self.name + " () (" + BVConstruct.sort() + " " + str(self.size) + "))\n"