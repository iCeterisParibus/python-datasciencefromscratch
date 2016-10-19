# occasionally we'll want to partially apply functions to create new functions

# example:

def exp(base, power):
    return base ** power

print '-' * 100

print """\nTypical function creation:

We wanna build a function called 'exp()' which takes two arguments: 'base' and 'power'
and returns 'base ** power' (base ^ power):

    def exp(base, power):
        return base ** power

Now that the function is created, if we pass base = 2 and power = 3

    print exp(2, 3)   # %d

This is what we would expect 2^3 to equal. Yay!\n""" % exp(2, 3)

print '-' * 100

print """\nUsing 'partial' function from 'functools' method:

Suppose you wanna make a function 'two_to_the' which takes only one
input 'power' and returns 'exp(2, power)'

One option: is to build an entirely new function specifically for this:\n
      def two_to_the(power):
          return exp(2, power)

But, this can get combersome when you have to do this over-and-over again.\n"""

def two_to_the(power):
    return exp(2, power)
print """Using the above function:\n
      print two_to_the(3)\t # %d\n\n""" % two_to_the(3)

print """A different approach: Use 'functools.partial' as follows:\n
      from functools import partial
      two_to_the = partial(exp, 2)\n"""

from functools import partial
two_to_the = partial(exp, 2)
print """This is the example using:\n
      from functools import partial
      two_to_the = partial(exp, 2)

      print two_to_the(3)\t # %d\n""" % two_to_the(3)

print '-' * 100

print """\nUsing 'map', 'reduce', 'filter' functions\n
Occasionally we'll use 'map', 'reduce', and 'filter' which provided functional
alternatives to list comprehension"""

def double(x):
    return 2 * x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs]
twice_xsa = map(double, xs)
list_doubler = partial(map, double)
twice_xsb = list_doubler(xs)

print """\nSay we have a list and we would like to double every value within the
list without having to build a 'for-loop' to increment through each value one-at-a-time.

\nWe can build our function 'double' which returns the input * 2:

    def double(x):
        return 2 * x

\nAs mentioned, one option is to apply this function to every element in the list
would be to build a 'for-loop' that would filter through our list, but
we're lazy (I meant efficient). So here are three different ways to do the same thing:

    xs = [1, 2, 3, 4]

    twice_xs = [double(x) for x in xs]  # build the for loop directly in a list

    twice_xsa = map(double, xs)         # use 'map' to \"map\" every element in xs to 'double()'

    list_doubler = partial(map, double) # build a 'list_doubler'; use 'partial' w/ 'map' and 'double'
    twice_xsb = list_doubler(xs)        # pass the list through our 'list_doubler' function

\nThe beauty the last example creating 'list_doubler' using 'partial(map, double)'
is that now we don't have to hardcode every instance of doubling a list. We simply
pass the list we want doubled to list_doubler and assign it to a new list. Brilliant!

    twice_xs = [double(x) for x in xs]      # %s

    twice_xsa = map(double, xs)'            # %s

    twice_xsb = list_doubler(xs)            # %s\n""" % (twice_xs, twice_xsa, twice_xsb)

print "See, I told you they would all do the same thing!\n"

print '-' * 100


print """\nUsing 'filter' function:

Similarly, 'filter' does the work of the list comprehension 'if':"""

def is_even(x):
    """True if x is even, False if x is odd"""
    return x % 2 == 0

x_evens = [x for x in xs if is_even(x)]
x_evensa = filter(is_even, xs)
list_evener = partial(filter, is_even)
x_evensb = list_evener(xs)

print """\nAs an example, lets build a function 'is_even' which takes in a single
input and returns a Boolean result to validate if a number is even (x %% 2 == 0):

    def is_even(x):
        \"\"\"True if x is even, False if x is odd\"\"\"
        return x %% 2 == 0

\nNow, we could build a 'for-loop' which cycles through each value in xs, adds the
actual value of the item in list xs if the returned value from is_even() is 'True'

    x_evens = [x for x in xs if is_even(x)] # see desc. above, too long for comment

    x_evensa = filter(is_even, xs)          # map ea. value in xs to is_even(); keep only 'True'

    list_evener = partial(filter, is_even)  # create funct. using partial to check evenness
    x_evensb = list_evener(xs)              # run list xs through 'list_evener' function

\nAgain, the last example gives us a reusable function which we can then pass any
list we desire without having to hardcode a 'for-loop' for each instance

    x_evens = [x for x in xs if is_even(x)]     # %r

    x_evensa = filter(is_even, xs)              # %r

    x_evensb = list_evener(xs)                  # %r

Three of a kind! Boom!\n""" % (x_evens, x_evensa, x_evensb)

print '-' * 100

print """\nMapping to multiple list at one time:

\nIf you provide multiple lists within the arguments, You can use 'map' with
multiple argument functions:"""

def multiply(x, y): return x * y
products = map(multiply, [1, 2], [4, 5])

print """\nWe'll start with creating a 'multiply' function which takes two arguments
and returns the product. Then we use 'map()' with the multiply function and two
separate lists to get the product (element-wise) of the two lists:

    def multiply(x, y): return x * y
    products = map(multiply, [1, 2], [4, 5])

The mapping with take the first element in the first list and the first element
in the second list and map them to multiply. Then the second elements of each list,
and so on until every element in both lists have been mapped. NOTE: the lists must
have equivalent cardinality! (same number of elements)

    print products      # %s\n""" % products

print '-' * 100

print """\nUsing 'reduce' to combine all elements into one single element

\nThe 'reduce' function combines the first two elements of a list, then combines
those with the third, then the fourth, and so on:"""

x_product = reduce(multiply, xs)
list_product = partial(reduce, multiply)
x_producta = list_product(xs)

print """\nWe can 'reduce' a list two different ways:

one way is to hardcode the specific list we want to reduce. The second would be
to use the 'partial' function to build a function that we can reuse:

    x_product = reduce(multiply, xs)            # specificaly 'reduce' list xs

    list_product = partial(reduce, multiply)    # build a function using 'reduce' and 'multiply()'
    x_producta = list_product(xs)               # pass list xs through list_product function

Both of these will produce the same result, but the latter will allow for more
freedom of use throughout your code.

    print x_product     # %s

    print x_producta    # %s

I love it when everything works like you expected!\n""" % (x_product, x_producta)

print '-' * 100
