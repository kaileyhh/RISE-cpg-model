# varying g using a custom differential equation, dg/dt = -c * | I_1 - I_2 |

from imports import *
from HRneuronseg import *
from synapseseg import *

neuron1 = HRneuronseg(1)
neuron2 = HRneuronseg(2)

neuron1.set_current(7.0)
neuron2.set_current(4.0)

neuron3 = HRneuronseg(3)
neuron4 = HRneuronseg(4)

neuron3.set_current(7.0)
neuron4.set_current(4.0)

synapse = synapseseg([neuron1, neuron2])
synapse_normal = synapseseg([neuron3, neuron4])

synapse.attach_neurons(neuron1, neuron2)
synapse.attach_neurons(neuron2, neuron1)

synapse_normal.attach_neurons(neuron3, neuron4)
synapse_normal.attach_neurons(neuron4, neuron3)


synapse.create_weight_mat(neuron1, [7.0])
synapse.create_weight_mat(neuron2, [5.0])


const = 0.16 #fast spiking 
# const = 0.05

for i in range(c.iterations):
    synapse.calculate_weight_all(i)
    # synapse_normal.calculate_all(i)

    synapse.update_dg_peaks(i, const)

    print(i, neuron1.weights[0])

np.save("nonlinear.npy", np.array([neuron1.xarr, neuron2.xarr]))

#ANALYZE INTERVAL TIMES
interval1 = [x/1000 for x in synapse.everything1]
interval2 = [x/1000 for x in synapse.everything2]

avg2 = np.average(np.array(interval1))
avg1 = np.average(np.array(interval2))

ratio = avg1/avg2


print(avg1)
print(avg2)
print("Ratio is", ratio)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

# temp = []
# temp2 = []

# for i in range(int(len(neuron1.zarr)/10000)):
#     temp.append(neuron1.zarr[10000 * i])

# for i in range(int(len(neuron2.zarr)/10000)):
#     temp2.append(neuron2.zarr[10000 * i])

# f1 = np.array(synapse.warr)
# f2 = np.array(synapse.warr2)

# f1 = f1/c.scale
# f2 = f2/c.scale


a = [3 for i in range(len(synapse.swaps))]
b = [3 for i in range(len(synapse.time_arr2))]

for i in range(len(synapse.time_arr2)):
    synapse.time_arr2[i] *= c.scale

for i in range(len(synapse.swaps)):
    synapse.swaps[i] *= c.scale

ax1.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
ax1.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)

ax2.plot(neuron1.time_vec, neuron1.garr, linewidth=0.5, color="black")
# ax2.plot(neuron1.time_vec, neuron4.xarr, linewidth=0.5, color=c.l_yellow)

ax3.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
# ax3.plot(synapse.swaps, a, "x")

ax4.plot(neuron2.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)
# ax4.plot(synapse.time_arr2, b, "x")
# ax4.plot(neuron1.time_vec, neuron1.garr, linewidth=0.5, color=c.l_blue)


# ax1.plot(neuron1.time_vec, neuron1.tarr, linewidth=0.5, color=c.l_blue)
# ax4.plot(neuron1.time_vec, neuron1.garr, linewidth=0.5, color=c.l_yellow)
# # ax2.plot(neuron1.time_vec, neuron2.tarr - neuron1.tarr, linewidth=0.5, color=c.l_yellow)
# ax3.plot(neuron1.time_vec, neuron1.xarr, linewidth=0.5, color=c.l_blue)
# ax3.plot(neuron1.time_vec, neuron2.xarr, linewidth=0.5, color=c.l_yellow)
# ax2.plot(neuron1.time_vec, neuron2.tarr, linewidth=0.5, color=c.l_yellow)
# ax4.plot(neuron1.time_vec, neuron1.zarr, linewidth=0.5, color=c.l_blue)
# ax4.plot(neuron1.time_vec, neuron2.zarr, linewidth=0.5, color=c.l_yellow)

ax1.set_title("HR Neurons with Synchrony")
ax1.set_xlabel("time (ms)", fontsize=8)
ax1.set_ylabel("membrane potential (au)", fontsize=8)
ax2.set_title("Modulation Value")
ax2.set_xlabel("time (ms)", fontsize=8)
ax2.set_ylabel("m (au)", fontsize=8)
ax3.set_title("Neuron 1, I = 7.0, x = swap", fontsize=8)
ax3.set_xlabel("Time (ms)", fontsize=8)
ax3.set_ylabel("membrane potential (au)", fontsize=8)

ax4.set_title("Neuron 2, I = 4.0, x = firing", fontsize=8)
ax4.set_xlabel("time (ms)", fontsize=8)
ax4.set_ylabel("membrane potential (au)", fontsize=8)

# plt.rc('figure', titlesize=8) 
fig.suptitle("Coupled HR Neurons With Nonlinear Conductance Decay, c = " + str(const), fontsize=8)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.savefig("nonlinear_g.png", dpi=300)

plt.show()