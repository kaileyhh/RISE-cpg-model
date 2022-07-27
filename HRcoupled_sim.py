from imports import *
from HRcoupled import *
from HRneuron import *
from synapse import *

c = constants()

neuron1 = HRcoupled(1) 
neuron2 = HRcoupled(2)

time_vec = np.arange(0, c.ms, c.scale)
current_vec = np.zeros(c.iterations) + c.I

synapse1 = synapse([neuron1, neuron2])

synapse1.calculate_all()

# print(synapse1.sigmoid1)
# synapse1.graph_all()

x1 = synapse1.get_neuron1x()
x2 = synapse1.get_neuron2x()
y1 = synapse1.get_neuron1y()
y2 = synapse1.get_neuron2y()

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

fig.suptitle("Coupled Inhibitory HR Neurons Phase Portraits, Bursting")
ax1.plot(neuron1.time_vec, x1, linewidth=0.5)
ax2.plot(neuron1.time_vec, x2, linewidth=0.5)

ax3.plot(x1, y1, linewidth=0.5)
ax4.plot(x2, y2, linewidth=0.5)

ax1.title.set_text("Neuron 1 (I = 4.5)")
ax1.set_xlabel("time (ms)")
ax1.set_ylabel("au")
ax2.title.set_text("Neuron 2 (I = 4.0)")
ax2.set_xlabel("time (ms)")
ax2.set_ylabel("au")
ax3.title.set_text("Neuron 1 Phase Portrait")
ax3.set_xlabel("membrane potential")
ax3.set_ylabel("ion transport rate")
ax4.title.set_text("Neuron 2 Phase Portrait")
ax4.set_xlabel("membrane potential")
ax4.set_ylabel("ion transport rate")

plt.subplots_adjust(left=0.1,
            bottom=0.1, 
            right=0.9, 
            top=0.9, 
            wspace=0.4, 
            hspace=0.4)
plt.savefig("bursting_coupled_phase.png", dpi=300)
plt.show()
