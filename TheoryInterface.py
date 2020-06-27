from abc import ABC, abstractmethod

class Construct(ABC):  ##derived class BV_ADD, FORALL, AND, ITE, etc.

    def __init__(self, construct): pass


    def theory(self):   pass  # theory construct came from.

    def sort(self):     pass  # return type of construct.

    def logic(self):    pass #return type of logic

    def setConstruct(self, construct):  pass

    def __str__(self):  pass  # smt-lib repr


class Variable(ABC):  ##derived literal class create BV, string, float, etc.
    def __init__(self, name): pass

    def theory(self):   pass  # theory construct came from.

    def sort(self):     pass  # return type of construct.

    def gen(self):      pass

    def value(self):    pass

    def __str__(self):  pass  # smt-lib repr

#add Literal Class

class ASTNode(ABC):  ##AST node class,
    def __init__(self): pass

        #self.val = None  # A construct
        #self.children = []  # list of child nodes, [] if leaf


def __str__(self):  pass


class Benchmark(ABC):  ##return type of fuzzer.gen, fuzzer.mutate
    def __init__(self, logic):
        self.logic = None  # i.e, (set-logic LOGIC)
        self.assertions = []  # List of asserting ASTNodes

    def __str__(self):          pass


class Fuzzer(ABC):
    def __init__(self, logic, constructs): pass  ##generates well formed formula over the logic and constructs.

    def gen(self, n_assert=5, depth=5): pass

    def mutate(self, input, construct): pass