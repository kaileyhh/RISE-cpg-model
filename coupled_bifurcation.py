from imports import *
from HRneuronseg import *
from synapseseg import *

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)
# neuron3 = HRneuronseg(3)


synapse = synapseseg([neuron1])

# synapse.attach_neurons(neuron1, neuron2)
# synapse.attach_neurons(neuron2, neuron1)


average_y1 = []
average_y2 = []

# average_y1 = np.load("1.npy")
# average_y2 = np.load("2.npy")
# average_y3 = np.load("3.npy")


# average_y1 = np.concatenate((np.load("0_1_1.npy"),np.load("1_2_1.npy"),np.load("2_3_1.npy"),np.load("3_4_1.npy")))
# average_y2 = np.concatenate((np.load("0_1_2.npy"),np.load("1_2_2.npy"),np.load("2_3_2.npy"),np.load("3_4_2.npy")))
# average_y3 = np.concatenate((np.load("0_1_3.npy"),np.load("1_2_3.npy"),np.load("2_3_3.npy"),np.load("3_4_3.npy")))



# a = np.load("0_1_1.npy")
# print(a)


neuron1.set_current(2.0)
# neuron2.set_current(2.0)
# neuron3.set_conductance(j * 0.1)
# print(neuron1.g)
# for i in range(c.iterations):
#     synapse.calculate_all(i)

# # x_y1 = neuron1.xarr[np.where(np.logical_and(neuron1.yarr < -2.4995, neuron1.yarr > -2.5005))]
# # print(len(x_y1))


for j in range(40):
    neuron1.set_current(j * 0.1 + 1)
    # neuron2.set_current(j * 0.1 + 1)
    # neuron3.set_conductance(j * 0.1)
    # print(neuron1.g)
    for i in range(c.iterations):
        synapse.calculate_all(i)


    average_y1.append(neuron1.xarr)
    average_y2.append(neuron1.yarr)
    # average_y3.append(neuron3.yarr)
    print(float(j/40))

np.save("1.npy", average_y1)
np.save("2.npy", average_y2)
# np.save("3.npy", average_y3)


# average_y2 = np.transpose(average_y2)
# average_y2 = average_y2[1000:500000]
# print(average_y2[:][5])
# print(len(average_y2[0]))
# average_y2 = np.transpose(average_y2)


# print("DONE :D")
plt.figure()

# average_y1 = np.load("1.npy")
# average_y2 = np.load("2.npy")
# average_y3 = np.load("3.npy")
# plt.scatter(np.zeros(500000), average_y2[5], s=1, color="black")

#x_y1 = neuron1.xarr[np.where(np.logical_and(neuron1.yarr < -2.4999, neuron1.yarr > -2.5001))]
#print(len(x_y1))

average_y1 = np.load("1.npy")


for i in range(len(average_y1)):
    # print(float(i/len(average_y1)))
    temp_vec = np.zeros(len(average_y1[i]))
    temp_vec = temp_vec + i * 0.1
    plt.scatter(temp_vec, average_y1[i], s=0.5, color="black")


# plt.plot(temp_vec, average_y1, linewidth=0.5, color="red", label = "neuron 1")
# plt.plot(temp_vec, average_y2, linewidth=0.5, color="green", label = "neuron 2")
# plt.plot(temp_vec, average_y3, linewidth=0.5, color="blue", label = "neuron 2")
# plt.legend()

plt.title("Bifurcation of Membrane Potential (Poincare section at y = −2.5)")

plt.ylabel("membrane potential")
plt.xlabel("conductance")

plt.savefig("x_vs_conductance", dpi=300)
print("HI")
plt.show()


# fig = plt.figure()
# ax1 = fig.add_subplot(221)
# ax2 = fig.add_subplot(222)
# ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)

# fig.suptitle("HR Neuron 2 inhibited by Neuron 1, conductance = " + str(c.g))


# # Y GRAPHS
# ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
# ax2.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color="green")
# ax3.plot(temp_vec, average_y1, linewidth=0.5, color="red")
# ax3.plot(temp_vec, average_y2, linewidth=0.5, color="green")
# ax3.plot(temp_vec, average_y3, linewidth=0.5, color="blue")
# ax4.plot(neuron1.time_vec, neuron3.xarr, linewidth=0.5, color="blue")


# ax1.title.set_text("Neuron 1 (I = " + str(neuron1.current) + " ), x0 = " + str(neuron1.xR))
# ax1.set_xlabel("time (ms)")
# ax1.set_ylabel("au")
# ax2.title.set_text("Neuron 2 (I = " + str(neuron2.current) + " ), x0 = " + str(neuron2.xR))
# ax2.set_xlabel("time (ms)")
# ax2.set_ylabel("au")
# ax2.title.set_text("Ion Transport Rate vs Coupling Force")
# ax2.set_xlabel("coupling force")
# ax2.set_ylabel("y")
# ax4.title.set_text("Neuron 3 (I = " + str(neuron3.current) + " ), x0 = " + str(neuron3.xR))
# ax4.set_xlabel("time (ms)")
# ax4.set_ylabel("au")
# # ax4.title.set_text("Neuron 3 (I = " + str(neuron3.current) + " ), x0 = " + str(neuron3.xR))
# # ax4.set_xlabel("time (ms)")
# # ax4.set_ylabel("au")

# plt.subplots_adjust(left=0.1,
#             bottom=0.1, 
#             right=0.9, 
#             top=0.9, 
#             wspace=0.4, 
#             hspace=0.4)
# # plt.savefig("coupled_phase_fast_spiking.png", dpi=300)
# plt.show()
