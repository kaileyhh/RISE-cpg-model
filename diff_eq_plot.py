from imports import *

c = constants()

t1 = np.array([101481, 113740, 123684, 120589, 124019, 124095, 122019, 121988, 121984, 123926, 123944])
t2 = np.array([64674, 100779, 127328, 123572, 123687, 122619, 122643, 122647, 122639, 123485, 128260])

t1 = t1 * c.scale
t2 = t2 * c.scale

plt.figure()

plt.plot(t1-t2, linewidth=0.5, color="black")
plt.title("Difference in Bursting Times of Coupled HR Neurons")
plt.xlabel("burst number")
plt.ylabel("difference in ms")
plt.savefig("difference.png", dpi = 300)
plt.show()