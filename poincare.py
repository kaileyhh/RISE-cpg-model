from imports import *

c = constants()

xarr = np.load("1.npy")
yarr = np.load("2.npy")

print(len(xarr))
plot_array = []

for i in range(len(xarr)):
    plot_array.append(xarr[i][np.where(np.logical_and(yarr[i] < -2.4999, yarr[i] > -2.5001))])

# print(plot_array)

plt.figure()
plt.plot(np.arange(0, c.ms, c.scale), xarr[4])

# for i in range(len(plot_array)):
#     # print(float(i/len(average_y1)))
#     temp_vec = np.zeros(len(plot_array[i]))
#     temp_vec = temp_vec + i * 0.1 + 1
#     plt.scatter(temp_vec, plot_array[i], s=0.5, color="black")


# plt.plot(temp_vec, plot_array, linewidth=0.5, color="black", label = "neuron 1")
# plt.legend()

plt.title("Bifurcation of Membrane Potential (Poincare section at y = −2.5)")

plt.ylabel("membrane potential")
plt.xlabel("conductance")

plt.savefig("poincare", dpi=300)
# print("HI")
plt.show()