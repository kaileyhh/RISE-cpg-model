from imports import *
from HRneuronseg import *
from synapseseg import *

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)
neuron3 = HRneuronseg(3)

print(neuron3)

neuron1.set_current(2.0)
neuron2.set_current(2.2)
neuron3.set_current(3.0)

synapse = synapseseg([neuron1, neuron2, neuron3])

synapse.attach_neurons(neuron1, neuron2)
synapse.attach_neurons(neuron2, neuron1)
synapse.attach_neurons(neuron1, neuron3)
synapse.attach_neurons(neuron3, neuron1)
# synapse.attach_neurons(neuron2, neuron3)
# synapse.attach_neurons(neuron3, neuron2)


print(synapse.neuron_dict)
print(synapse.get_neuron(3))
print(neuron1.get_connections())

for i in range(c.iterations):
    synapse.calculate_all(i)

x1 = neuron1.xarr
x2 = neuron2.xarr
y1 = neuron1.yarr
y2 = neuron2.yarr

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

fig.suptitle("3-way Coupled Inhibitory HR Neurons (1 & 2), (1 & 3)")
        
ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")

ax2.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color="green")
ax3.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color="red")
ax3.plot(neuron2.time_vec, neuron2.xarr, linewidth=0.5, color="green")
ax3.plot(neuron2.time_vec, neuron3.xarr, linewidth=0.5, color="blue")
# ax3.plot(self.neuron1.time_vec, self.neuron1.yarr, linewidth=0.5)
ax4.plot(neuron1.time_vec, neuron3.xarr, linewidth=0.5, color="blue")

ax1.title.set_text("Neuron 1 (I = " + str(neuron1.current) + " ), x0 = " + str(neuron1.xR))
ax1.set_xlabel("time (ms)")
ax1.set_ylabel("au")
ax2.title.set_text("Neuron 2 (I = " + str(neuron2.current) + " ), x0 = " + str(neuron2.xR))
ax2.set_xlabel("time (ms)")
ax2.set_ylabel("au")
ax3.title.set_text("Both")
ax3.set_xlabel("time (ms)")
ax3.set_ylabel("au")
ax4.title.set_text("Neuron 3 (I = " + str(neuron3.current) + " ), x0 = " + str(neuron3.xR))
ax4.set_xlabel("time (ms)")
ax4.set_ylabel("au")

plt.subplots_adjust(left=0.1,
            bottom=0.1, 
            right=0.9, 
            top=0.9, 
            wspace=0.4, 
            hspace=0.4)
plt.savefig("coupled_phase_fast_spiking.png", dpi=300)
plt.show()
