from matplotlib import pyplot as plt

mentions = [500, 505]
years = [2013, 2014]

plt.bar([2012.6, 2013.6], mentions, 0.8)
plt.xticks(years)
plt.ylabel("# of times I heard someone say 'Data Science'")

# if you don't do this, matplotlib will label the x-axis
# and then add a +2.013e3 off in the corner
plt.ticklabel_format(useOffset=False)

# misleading y-axis only shows the part above 500
plt.axis([2012.5, 2014.5, 499, 506])
plt.title("Look at the 'Huge' increase!")
# plt.show()

# more sensible axis would be
plt.axis([2012.5, 2014.5, 0, 550])
plt.title("Not so huge anymore")
plt.show()
