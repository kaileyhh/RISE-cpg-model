# varying g using a custom differential equation, dg/dt = -c * | I_1 - I_2 |

from imports import *
from HRneuronseg import *
from synapseseg import *

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)

neuron1.set_current(5.0)
neuron2.set_current(4.0)

synapse = synapseseg([neuron1, neuron2])

synapse.attach_neurons(neuron1, neuron2)
synapse.attach_neurons(neuron2, neuron1)

synapse.create_weight_mat(neuron1, [5.0])
synapse.create_weight_mat(neuron2, [5.0])


const = 0.01 #fast spiking 
# const = 0.05

for i in range(c.iterations):
    synapse.calculate_weight_all(i)

    synapse.update_new_dg2(i, const)

    print(i, neuron1.weights[0])

np.save("nonlinear.npy", np.array([neuron1.xarr, neuron2.xarr]))

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

temp = []
temp2 = []

for i in range(int(len(neuron1.zarr)/10000)):
    temp.append(neuron1.zarr[10000 * i])

for i in range(int(len(neuron2.zarr)/10000)):
    temp2.append(neuron2.zarr[10000 * i])

ax1.plot(neuron1.time_vec, neuron1.tarr, linewidth=0.5, color=c.l_blue)
ax4.plot(neuron1.time_vec, neuron1.garr, linewidth=0.5, color=c.l_yellow)
# ax2.plot(neuron1.time_vec, neuron2.tarr - neuron1.tarr, linewidth=0.5, color=c.l_yellow)
ax3.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
ax3.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)
ax2.plot(neuron1.time_vec, neuron2.tarr, linewidth=0.5, color=c.l_yellow)
# ax4.plot(neuron1.time_vec, neuron1.zarr, linewidth=0.5, color=c.l_blue)
# ax4.plot(neuron1.time_vec, neuron2.zarr, linewidth=0.5, color=c.l_yellow)

ax1.set_title("T1")
ax1.set_xlabel("Time (ms)", fontsize=8)
ax1.set_ylabel("t1", fontsize=8)
ax2.set_title("T2")
ax2.set_xlabel("Time (ms)", fontsize=8)
ax2.set_ylabel("t2", fontsize=8)
ax3.set_title("Both", fontsize=8)
ax3.set_xlabel("Time (ms)", fontsize=8)
ax3.set_ylabel("au", fontsize=8)

ax4.set_title("conductance of Neuron 1", fontsize=8)
ax4.set_xlabel("conductance (au)", fontsize=8)
ax4.set_ylabel("time (ms)", fontsize=8)

# plt.rc('figure', titlesize=8) 
fig.suptitle("Coupled HR Neurons With Nonlinear Conductance Decay, c = " + str(const))

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.savefig("nonlinear_g.png", dpi=300)

plt.show()