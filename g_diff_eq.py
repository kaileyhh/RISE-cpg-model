# varying g using a custom differential equation, dg/dt = -c * | I_1 - I_2 |

from imports import *
from HRneuronseg import *
from synapseseg import *

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)

neuron1.set_current(2.15)
neuron2.set_current(2.1)

synapse = synapseseg([neuron1, neuron2])

synapse.attach_neurons(neuron1, neuron2)
synapse.attach_neurons(neuron2, neuron1)

const = 0.0002

for i in range(c.iterations):
    synapse.calculate_all(i)
    synapse.update_dg(i, const)
    print(i)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
ax2.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)
ax3.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
ax3.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)
ax4.plot(neuron1.time_vec, neuron1.garr, linewidth=0.5, color=c.l_blue)

ax1.set_title("Neuron 1, I = " + str(neuron1.current), fontsize=8)
ax1.set_xlabel("Time (ms)", fontsize=8)
ax1.set_ylabel("Membrane Potential (au)", fontsize=8)
ax2.set_title("Neuron 2, I = " + str(neuron2.current), fontsize=8)
ax2.set_xlabel("Time (ms)", fontsize=8)
ax2.set_ylabel("au", fontsize=8)
ax3.set_title("Both", fontsize=8)
ax3.set_xlabel("Time (ms)", fontsize=8)
ax3.set_ylabel("au", fontsize=8)

ax4.set_title("Conductance / Time", fontsize=8)
ax4.set_xlabel("Time (ms)", fontsize=8)
ax4.set_ylabel("Conductance (au)", fontsize=8)

# plt.rc('figure', titlesize=8) 
fig.suptitle("Coupled HR Neurons With Linear Conductance Decay, c = " + str(const))

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.savefig("cpg.png", dpi=300)

plt.show()