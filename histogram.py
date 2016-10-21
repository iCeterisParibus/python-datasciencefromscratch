from collections import Counter
from matplotlib import pyplot as plt
import random

# populate our data with 100 obsv of values between 0 and 100
num_observations = random.randrange(200, 300)

num_friends = [random.choice(range(100))
               for _ in range(num_observations)]

# build histogram of num_friends data
friends_count = Counter(num_friends)
xs = range(101)
ys = [friends_count[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 10])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_users = len(num_friends)

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value_verify = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

print """
Total number of users: %s
Largest number of friends: %s
Smallest number of friends: %s (double check: %s)
Second smallest number of friends: %s""" % (
    num_users, largest_value, smallest_value, smallest_value_verify, second_smallest_value)
