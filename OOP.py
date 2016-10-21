# This script is on the crash course topic of Object-Oriented Programming
# as discussed in "Data Science from Scrath" by Joel Grus

# This is the example provided by Joel of constructing our own version of the
# set() function already provided in Python.
class Set:

    def __init__(self, values = None):
        """This is the constructor. It gets called when you ccreate a new Set such as:
        s1 = Set([])    or   s2 = Set([1, 2, 3])"""
        self.dict = {}

        if values is not None:
            for value in values:
                self.add(value)

    def __repr__(self):
        """string representation of a Set object. If you type it at the Python
        prompt or pass it to str()"""
        return "Set: " + str(self.dict.keys())

    # we'll represent membership by being a key in self.dict with value 'True'
    def add(self, value):
        self.dict[value] = True

    # value is in the set if it's a key in the dictionary
    def contains(self, value):
        return value in self.dict

    def remove(self, value):
        del self.dict[value]

print '-' * 100

print """\nObject-Oreinted Programming in Python:

\nPython, similar to many languages, allows you to build 'classes' which can be
used to clean up your scripts/programs. Classes allow you to group together sets
of functions and data which can later be assigned to a new classname without having
any effect on the class itself. In other words, you can make hunderds of variations
of the class on an as needed basis and never have to worry about breaking the
original class. Yay for efficient idoit-proofing!

To best explain how a class works, we build a class named 'Set' (classes use
PascalCase) which will operate similarly to the python function set().

    class Set:

        def __init__(self, values = None):
            \"\"\"This is the constructor. It gets called when you ccreate a new Set such as:
            s1 = Set([])    or   s2 = Set([1, 2, 3])\"\"\"

            self.dict = {}

            if values is not None:
                for value in values:
                    self.add(value)

        def __repr__(self):
            \"\"\"string representation of a Set object. If you type it at the Python
            prompt or pass it to str()\"\"\"
            return "Set: " + str(self.dict.keys())

        # we'll represent membership by being a key in self.dict with value 'True'
        def add(self, value):
            self.dict[value] = True

        # value is in the set if it's a key in the dictionary
        def contains(self, value):
            return value in self.dict

        def remove(self, value):
            del self.dict[value]

Don't stress over the details too much. The general idea is that we built a class
which we can now assign to a classname and then use all the funtions we included
in the class to manipulate the list, technically set, of values provided in the Set.\n"""

print '-' * 100

# Example provided by Joel to show how the entire Set() class created works
s = Set([1, 2, 3])
s.add(4)
# print s.contains(4)
s.remove(3)
# print s.contains(3)

print """\nHere is an example of what our Set() class can do:

    s = Set([1, 2, 3])      # a new iteration of 'Set()' named 's' is created with 3 elements
    s.add(4)                # using the add object, '4' is added to the Set
    print s.contains(4)     # returns '%s'
    s.remove(3)             # using the remove object, '3' is deleted from the set
    print s.contains(3)     # returns '%s'

See, this works the same as 'set()' in a simple form.\n""" % (s.contains(4), s.contains(3))

print '-' * 100
