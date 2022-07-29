from imports import *
from HRneuronseg import *
from synapseseg import *

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)

neuron3 = HRneuronseg(3)
neuron4 = HRneuronseg(4)
# neuron3 = HRneuronseg(3)

neuron1.set_current(2.0)
neuron3.set_current(2.0)
neuron2.set_current(2.1)
neuron4.set_current(2.1)
# neuron3.set_current(2.0)

synapse = synapseseg([neuron1, neuron2])
synapse2 = synapseseg([neuron3, neuron4])

synapse.attach_neurons(neuron1, neuron2)
synapse.attach_neurons(neuron2, neuron1)

synapse.attach_neurons(neuron3, neuron4)
synapse.attach_neurons(neuron4, neuron3)

# synapse.attach_neurons(neuron1, neuron3)
# synapse.attach_neurons(neuron3, neuron1)
# synapse.attach_neurons(neuron2, neuron3)
# synapse.attach_neurons(neuron3, neuron2)
sensory_vec = np.zeros(c.iterations) 

temp = 0
oscillate = False

for i in range(int(c.iterations *2/5.0), int(c.iterations*3/5)):
    sensory_vec[i] = 1.0

for i in range(c.iterations):
    synapse.calculate_sensory_all(i, 1.0, 1.0, sensory_vec[i])#, 5.0, 0.0, 1)
    synapse2.calculate_all(i)


fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# fig.suptitle("HR Neurons 2 inhibited by Neuron 1, conductance = " + str(c.g))



# x_y1 = neuron1.xarr[np.where(np.logical_and(neuron1.yarr < -2.5,neuron1.yarr > -2.6))]
# print(x_y1)
# x_y2 = neuron1.xarr[np.where(np.logical_and(neuron2.yarr < -2.5,neuron1.yarr > -2.6))]


# Y GRAPHS
# ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
# ax2.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color="green")
# ax3.plot(neuron1.xarr, neuron1.yarr, linewidth=0.5, color="red")
# ax3.scatter(x_y1, linewidth=0.5, color="red")
# ax4.scatter(x_y2, linewidth=0.5, color="green")

# ax4.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
# ax4.plot(neuron2.time_vec, neuron2.xarr, linewidth=0.5, color="green")

# NORMAL GRAPHS
ax1.plot(neuron1.time_vec, neuron3.xarr, linewidth=0.5, color="purple")
ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
ax2.plot(neuron1.time_vec, neuron4.xarr, linewidth=0.5, color="blue")
ax2.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color="green")
# ax3.plot(neuron1.xarr, neuron1.yarr, linewidth=0.5, color="red")
# ax3.plot(neuron2.xarr, neuron2.yarr, linewidth=0.5, color="green")
ax3.plot(neuron1.time_vec, neuron3.xarr, linewidth=0.5, color="purple")
ax3.plot(neuron1.time_vec, neuron4.xarr, linewidth=0.5, color="blue")
ax4.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
ax4.plot(neuron2.time_vec, neuron2.xarr, linewidth=0.5, color="green")


ax1.title.set_text("Neuron 1 (red, I = " + str(neuron1.current) + " ), x0 = " + str(neuron1.xR))
ax1.set_xlabel("time (ms)")
ax1.set_ylabel("au")
ax2.title.set_text("Neuron 2 (green, I = " + str(neuron2.current) + " ), x0 = " + str(neuron2.xR))
ax2.set_xlabel("time (ms)")
ax2.set_ylabel("au")
ax3.title.set_text("3, 4 Neurons, No Stimulus")
ax3.set_xlabel("time (ms)")
ax3.set_ylabel("au")
ax4.title.set_text("1, 2 Neurons; Neuron 1 Stimulus")
ax4.set_xlabel("time (ms)")
ax4.set_ylabel("au")

plt.rc('figure', titlesize=8) 
fig.suptitle("2 coupled neurons (I = 1.4); neuron 1 receives sensory excitation for 200ms")

plt.subplots_adjust(left=0.1,
            bottom=0.1, 
            right=0.9, 
            top=0.9, 
            wspace=0.4, 
            hspace=0.4)
plt.savefig("coupled_phase_fast_spiking.png", dpi=300)
plt.show()
