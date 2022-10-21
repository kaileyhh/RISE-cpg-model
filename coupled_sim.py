from imports import *
from HRneuronseg import *
from synapseseg import *

c = constants()

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)

neuron1.set_current(5.0)
neuron2.set_current(4.0)

synapse = synapseseg([neuron1, neuron2])

synapse.attach_neurons(neuron1, neuron2)
synapse.attach_neurons(neuron2, neuron1)

for i in range(c.iterations):
    synapse.calculate_all(i)
    print(i)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
# ax4 = fig.add_subplot(224)

ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
ax2.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)
ax3.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
ax3.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)

plt.show()
