from imports import *
from HRneuronseg import *
from synapseseg import *

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)
# neuron3 = HRneuronseg(3)

neuron1.set_current(3.3)
neuron2.set_current(3.3)
# neuron3.set_current(2.0)

synapse = synapseseg([neuron1, neuron2])

synapse.attach_neurons(neuron1, neuron2)
synapse.attach_neurons(neuron2, neuron1)

# synapse.attach_neurons(neuron1, neuron3)
# synapse.attach_neurons(neuron3, neuron1)
# synapse.attach_neurons(neuron2, neuron3)
# synapse.attach_neurons(neuron3, neuron2)


for i in range(c.iterations):
    synapse.calculate_all(i)


fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

fig.suptitle("HR Neurons 2 inhibited by Neuron 1, conductance = " + str(c.g))



x_y1 = neuron1.xarr[np.where(np.logical_and(neuron1.yarr < -2.5,neuron1.yarr > -2.6))]
print(x_y1)
x_y2 = neuron1.xarr[np.where(np.logical_and(neuron2.yarr < -2.5,neuron1.yarr > -2.6))]


# Y GRAPHS
ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
ax2.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color="green")
# ax3.plot(neuron1.xarr, neuron1.yarr, linewidth=0.5, color="red")
# ax3.scatter(x_y1, linewidth=0.5, color="red")
# ax4.scatter(x_y2, linewidth=0.5, color="green")

# ax4.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
# ax4.plot(neuron2.time_vec, neuron2.xarr, linewidth=0.5, color="green")

# NORMAL GRAPHS
# ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
# ax2.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color="green")
# ax3.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
# ax3.plot(neuron2.time_vec, neuron2.xarr, linewidth=0.5, color="green")
# ax3.plot(neuron2.time_vec, neuron3.xarr, linewidth=0.5, color="blue")
# ax4.plot(neuron1.time_vec, neuron3.xarr, linewidth=0.5, color="blue")

ax1.title.set_text("Neuron 1 (I = " + str(neuron1.current) + " ), x0 = " + str(neuron1.xR))
ax1.set_xlabel("time (ms)")
ax1.set_ylabel("au")
ax2.title.set_text("Neuron 2 (I = " + str(neuron2.current) + " ), x0 = " + str(neuron2.xR))
ax2.set_xlabel("time (ms)")
ax2.set_ylabel("au")
ax3.title.set_text("Neuron 1 Phase Portrait")
ax3.set_xlabel("x")
ax3.set_ylabel("y")
ax4.title.set_text("Neuron 2 Phase Portrait")
ax4.set_xlabel("x")
ax4.set_ylabel("y")

plt.subplots_adjust(left=0.1,
            bottom=0.1, 
            right=0.9, 
            top=0.9, 
            wspace=0.4, 
            hspace=0.4)
plt.savefig("coupled_phase_fast_spiking.png", dpi=300)
plt.show()
