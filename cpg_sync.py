from imports import *
from HRneuronseg import *
from synapseseg import *

pre_botc = HRneuronseg(1)
pico = HRneuronseg(2)
rtn = HRneuronseg(3)

pre_botc.set_current(5.5)
pico.set_current(3.1)
rtn.set_current(4.0)

cpg = synapseseg([pre_botc, pico, rtn])

cpg.attach_neurons(pre_botc, pico)
cpg.attach_neurons(pico, pre_botc)
cpg.attach_neurons(pico, rtn)
cpg.attach_neurons(rtn, pico)
cpg.attach_neurons(pre_botc, rtn)
cpg.attach_neurons(rtn, pre_botc)

cpg.create_weight_mat(pre_botc, [5.2, 2.7])
cpg.create_weight_mat(pico, [5.0, 2.5])
cpg.create_weight_mat(rtn, [4.1, 2.0])

const = 0.016

for i in range(c.iterations):
    cpg.calculate_weight_all(i)
    cpg.update_dg_peaks(i, const)
    cpg.update_dg_peaks2(i, const)
    print(i, pre_botc.weights[0], pico.weights[0], rtn.weights[1])

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


# a = [3 for i in range(len(cpg.swaps))]
# b = [3 for i in range(len(cpg.time_arr2))]

# for i in range(len(synapse.time_arr2)):
#     synapse.time_arr2[i] *= c.scale

# for i in range(len(synapse.swaps)):
#     synapse.swaps[i] *= c.scale

ax4.plot(pre_botc.time_vec, pre_botc.xarr, linewidth=0.5, color=c.l_blue)
ax4.plot(pre_botc.time_vec, pico.xarr, linewidth=0.5, color=c.l_yellow)
ax4.plot(pre_botc.time_vec, rtn.xarr, linewidth=0.5, color="black")

ax3.plot(pre_botc.time_vec, rtn.xarr, linewidth=0.5, color="black")
# ax2.plot(neuron1.time_vec, neuron4.xarr, linewidth=0.5, color=c.l_yellow)

ax2.plot(pre_botc.time_vec, pre_botc.xarr, linewidth=0.5, color=c.l_blue)
# ax3.plot(synapse.swaps, a, "x")

ax3.plot(pre_botc.time_vec, pico.xarr, linewidth=0.5, color=c.l_yellow)
ax1.plot(pre_botc.time_vec, pre_botc.garr, linewidth=0.5, color=c.l_yellow)
ax1.plot(pre_botc.time_vec, pico.garr, linewidth=0.5, color=c.l_blue)
ax1.plot(pre_botc.time_vec, rtn.garr, linewidth=0.5, color="black")


ax1.set_title("Modulation values", fontsize=8)
ax1.set_xlabel("Time (ms)", fontsize=8)
ax1.set_ylabel("modulation value (au)", fontsize=8)
ax2.set_title("PiCo, [Pre-BotC = 5.0, RTN/pFRG = 2.5]", fontsize=8)
ax2.set_xlabel("Time (ms)", fontsize=8)
ax2.set_ylabel("au", fontsize=8)
ax3.set_title("Pre-BotC, [PiCo = 5.2, RTN/pFRG = 2.7], RTN/pFRG [Pre-Botc = 4.1, PiCo = 2.0]", fontsize=6)
ax3.set_xlabel("Time (ms)", fontsize=8)
ax3.set_ylabel("Membrane Potential (au)", fontsize=8)
ax4.set_title("All Complexes Together", fontsize=8)
ax4.set_xlabel("Time (ms)", fontsize=8)
ax4.set_ylabel("Membrane Potential (au)", fontsize=8)

# plt.rc('figure', titlesize=8) 
# fig.suptitle("CPG Neurons (Pre-BotC I = " + str(pre_botc.current) + " PiCo I = " + str(pico.current) + " RTN/pFRG I = " + str(rtn.current) +")")

# plt.rc('figure', titlesize=8) 
fig.suptitle("CPG With Nonlinear Conductance Decay, c = " + str(const), fontsize=8)

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.savefig("nonlinear_g.png", dpi=300)

plt.show()