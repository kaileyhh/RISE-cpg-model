from imports import *
from HRneuronseg import *
from synapseseg import *

# weight is 5.0 by default, positive is inhibitory
# -5.0 weight would be excitatory connections

pre_botc = HRneuronseg(1)
pico = HRneuronseg(2)
rtn = HRneuronseg(3)

pre_botc.set_current(3.55)
pico.set_current(3.5)
rtn.set_current(3.45)

# pico.set_current(2.5)
# rtn.set_current(2.0)

cpg = synapseseg([pre_botc, pico, rtn])

cpg.attach_neurons(pre_botc, pico)
cpg.attach_neurons(pico, pre_botc)
cpg.attach_neurons(pico, rtn)
cpg.attach_neurons(rtn, pico)
cpg.attach_neurons(pre_botc, rtn)
cpg.attach_neurons(rtn, pre_botc)

cpg.create_weight_mat(pre_botc, [50.2, 40.7])
cpg.create_weight_mat(pico, [50.0, 40.5])
cpg.create_weight_mat(rtn, [40.1, 40.0])

for i in range(c.iterations):
    cpg.calculate_weight_all(i)
    print(i)

a = [pre_botc.xarr, pico.xarr, rtn.xarr]
# np.save("cpg.npy", a)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(pre_botc.time_vec, pre_botc.xarr, linewidth=0.5, color=c.l_blue)
ax2.plot(pico.time_vec, pico.xarr, linewidth=0.5, color=c.l_yellow)
ax3.plot(rtn.time_vec, rtn.xarr, linewidth=0.5, color="black")

ax4.plot(pre_botc.time_vec, pre_botc.xarr, linewidth=0.5, color=c.l_blue)
ax4.plot(pico.time_vec, pico.xarr, linewidth=0.5, color=c.l_yellow)
ax4.plot(rtn.time_vec, rtn.xarr, linewidth=0.5, color="black")

ax1.set_title("Pre-BotC, [PiCo = 50.2, RTN/pFRG = 40.7]", fontsize=8)
ax1.set_xlabel("Time (ms)", fontsize=8)
ax1.set_ylabel("Membrane Potential (au)", fontsize=8)
ax2.set_title("PiCo, [Pre-BotC = 50.0, RTN/pFRG = 40.5]", fontsize=8)
ax2.set_xlabel("Time (ms)", fontsize=8)
ax2.set_ylabel("au", fontsize=8)
ax3.set_title("RTN/pFRG, [Pre-Botc = 40.1, PiCo = 40.0]", fontsize=8)
ax3.set_xlabel("Time (ms)", fontsize=8)
ax3.set_ylabel("Membrane Potential (au)", fontsize=8)
ax4.set_title("All Complexes Together", fontsize=8)
ax4.set_xlabel("Time (ms)", fontsize=8)
ax4.set_ylabel("Membrane Potential (au)", fontsize=8)

# plt.rc('figure', titlesize=8)
fig.suptitle("CPG Neurons (Pre-BotC I = " + str(pre_botc.current) +
             " PiCo I = " + str(pico.current) + " RTN/pFRG I = " + str(rtn.current) + ")")

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

plt.savefig("tonic_cpg.png", dpi=300)

plt.show()
