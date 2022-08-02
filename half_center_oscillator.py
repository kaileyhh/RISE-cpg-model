# A half center oscillator is a circuit of 2 inhibitory neurons.

from imports import *
from HRneuronseg import *
from synapseseg import *

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)

synapse = synapseseg([neuron1, neuron2])

synapse.attach_neurons(neuron1, neuron2)
synapse.attach_neurons(neuron2, neuron1)

neuron3 = HRneuronseg(3)
neuron4 = HRneuronseg(4)

synapse2 = synapseseg([neuron3, neuron4])

synapse2.attach_neurons(neuron3, neuron4)
synapse2.attach_neurons(neuron4, neuron3)

neuron5 = HRneuronseg(5)
neuron6 = HRneuronseg(6)

neuron5.set_k(2.8)
neuron6.set_k(2.8)

synapse3 = synapseseg([neuron5, neuron6])

synapse3.attach_neurons(neuron5, neuron6)
synapse3.attach_neurons(neuron6, neuron5)

for i in range(c.iterations):
    synapse.calculate_max_all(i)
    synapse2.calculate_all(i)
    synapse3.calculate_all(i)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)

ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
ax1.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)

ax2.plot(neuron1.time_vec, neuron3.xarr, linewidth=0.5, color=c.l_blue)
ax2.plot(neuron1.time_vec, neuron4.xarr, linewidth=0.5, color=c.l_yellow)

ax3.plot(neuron1.time_vec, neuron5.xarr, linewidth=0.5, color=c.l_blue)
ax3.plot(neuron1.time_vec, neuron6.xarr, linewidth=0.5, color=c.l_yellow)

ax1.set_title("Neurons 1 & 2 with Max(x)", fontsize=8)
ax1.set_xlabel("Time (ms)", fontsize=8)
ax1.set_ylabel("Membrane Potential (au)", fontsize=8)
ax2.set_title("Neurons 3 & 4 with Sigmoid(x), k = -10.0", fontsize=8)
ax2.set_xlabel("Time (ms)", fontsize=8)
ax2.set_ylabel("au", fontsize=8)
ax3.set_title("Neurons 5 & 6 with Sigmoid(x), k = -0.9", fontsize=8)
ax3.set_xlabel("Time (ms)", fontsize=8)
ax3.set_ylabel("au", fontsize=8)
# ax3.set_title("RTN/pFRG, [Pre-Botc = 2.1, PiCo = 2.0]", fontsize=8)
# ax3.set_xlabel("Time (ms)", fontsize=8)
# ax3.set_ylabel("Membrane Potential (au)", fontsize=8)
# ax4.set_title("All Complexes Together", fontsize=8)
# ax4.set_xlabel("Time (ms)", fontsize=8)
# ax4.set_ylabel("Membrane Potential (au)", fontsize=8)

# plt.rc('figure', titlesize=8) 
fig.suptitle("Half-Center Oscillator, I = 3.15")

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.savefig("cpg.png", dpi=300)

plt.show()