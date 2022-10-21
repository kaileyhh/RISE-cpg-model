from imports import *
from HRneuronseg import *
from synapseseg import *
from HRneuron import *

neuron1 = HRneuron(1)
neuron2 = HRneuronseg(2)


synapse = synapseseg([neuron1])


average_y1 = []
average_y2 = []
average_y3 = []

time_vec = np.arange(0, c.ms, c.scale)

a = []
"""
for j in range(400):
    neuron1.set_current(j * 0.01 + 1)
    print(neuron1.current)
    # neuron2.set_current(j * 0.1 + 1)
    # neuron3.set_conductance(j * 0.1)
    # print(neuron1.g)
    for i in range(c.iterations):
        neuron1.calculate_x(i)
        neuron1.calculate_y(i)
        neuron1.calculate_z(i)


    x_y1 = neuron1.xarr[np.where(np.logical_and(neuron1.yarr < -2.4999, neuron1.yarr > -2.5001))]
    temp_vec = np.zeros(len(x_y1))
    temp_vec = temp_vec + j * 0.01 + 1
    plt.scatter(temp_vec, x_y1, s=0.05, color="black")
    a.append(x_y1)
    # average_y3.append(neuron3.yarr)
    # plt.figure()
    # plt.plot(time_vec, neuron1.xarr)
    # plt.show()
    print(float(j/400))
"""

neuron1.set_current(3.15)
print(neuron1.current)

for i in range(c.iterations):
    neuron1.calculate_x(i)
    neuron1.calculate_y(i)
    neuron1.calculate_z(i)






temp = np.zeros(c.iterations)
temp -= 2.5

plt.plot(neuron1.xarr[100000:], neuron1.yarr[100000:],
         linewidth=0.5, color="black")
# plt.plot(temp[100000:], linewidth=0.5, color=c.l_blue)
plt.axhline(y=-2.5, linewidth=0.5, color=c.l_blue, label="y = -2.5")
# plt.plot(temp_vec, average_y2, linewidth=0.5, color="green", label = "neuron 2")
# plt.plot(temp_vec, average_y3, linewidth=0.5, color="blue", label = "neuron 2")
# plt.legend()
plt.legend()
plt.title("Phase Portrait of I = 3.15 (Poincare section at y = −2.5)")

# plt.title("Bifurcation of Membrane Potential (Poincare section at y = −2.5)")

plt.ylabel("conductance")
plt.xlabel("membrane potential")

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
