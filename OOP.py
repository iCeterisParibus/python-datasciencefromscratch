# This is the example regarding object-oriented programming
# this is an example of how to create a version of the set() function

class Set:

    def __init__(self, values = None):
        """ This is the constructor. It gets called when you create a new Set
        such as s1 = Set() or s2 = Set([1, 2, 3, 4])"""

        self.dict = {}

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """ string representation of a Set object. If you type it at the Python
        prompt or pass it to str()"""

        return "Set: " + str(self.dict.keys())

    # we'll represent membership by being a key in self.dict with value True
    def add(self, value):
        self.dict[value] = True

    # value is in the set if it's a key in the dictionary
    def contains(set, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

s = Set([1, 2, 3])
s.add(4)
print s.contains(4)
s.remove(3)
print s.contains(3)
