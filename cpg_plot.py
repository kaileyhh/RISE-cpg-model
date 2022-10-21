from imports import *

# unless stated otherwise, v_syn = 2.0

c = constants()

a = np.load("cpg.npy")

pre_botc = a[0]
pico = a[1]
rtn = a[2]

time_vec = np.arange(0, c.ms, c.scale)

# pre_botc = pre_botc[:300000]
# pico = pico[:300000]
# rtn = rtn[:300000]
# time_vec = time_vec[:300000]

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(time_vec, pre_botc, linewidth=0.5, color=c.l_blue)
ax2.plot(time_vec, pico, linewidth=0.5, color=c.l_yellow)
ax3.plot(time_vec, rtn, linewidth=0.5, color="black")

ax4.plot(time_vec, pre_botc, linewidth=0.5, color=c.l_blue)
ax4.plot(time_vec, pico, linewidth=0.5, color=c.l_yellow)
ax4.plot(time_vec, rtn, linewidth=0.5, color="black")

ax1.set_title("Pre-BotC, [PiCo = 5.2, RTN/pFRG = 1.7]", fontsize=8)
ax1.set_xlabel("Time (ms)", fontsize=8)
ax1.set_ylabel("Membrane Potential (au)", fontsize=8)
ax2.set_title("PiCo, [Pre-BotC = 5.0, RTN/pFRG = 2.5]", fontsize=8)
ax2.set_xlabel("Time (ms)", fontsize=8)
ax2.set_ylabel("au", fontsize=8)
ax3.set_title("RTN/pFRG, [Pre-Botc = 2.1, PiCo = 2.0]", fontsize=8)
ax3.set_xlabel("Time (ms)", fontsize=8)
ax3.set_ylabel("Membrane Potential (au)", fontsize=8)
ax4.set_title("All Complexes Together", fontsize=8)
ax4.set_xlabel("Time (ms)", fontsize=8)
ax4.set_ylabel("Membrane Potential (au)", fontsize=8)

# plt.rc('figure', titlesize=8)
fig.suptitle("CPG Neuron Complex Simulation, I = 3.15")

plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.4,
                    hspace=0.4)

plt.savefig("cpg.png", dpi=300)

plt.show()
