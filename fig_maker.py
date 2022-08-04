from imports import *

# plt.figure()
# plt.title("Bifurcation of Membrane Potentials (Poincare section at y = -2.5)")
# plt.ylabel("membrane potential")
# plt.xlabel("injected current")
# plt.savefig("Bifurcation_clear.png", dpi=300)
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.set_title("t1 (Neuron 1, I = 5.0)")
ax1.set_xlabel("time (ms)", fontsize=8)
ax1.set_ylabel("t1", fontsize=8)
ax2.set_title("t1 (Neuron 2, I = 4.0")
ax2.set_xlabel("time (ms)", fontsize=8)
ax2.set_ylabel("t2", fontsize=8)
ax3.set_title("Both", fontsize=8)
ax3.set_xlabel("Time (ms)", fontsize=8)
ax3.set_ylabel("membrane potential (au)", fontsize=8)

ax4.set_title("conductance of Neuron 1", fontsize=8)
ax4.set_xlabel("time (ms)", fontsize=8)
ax4.set_ylabel("conductance (au)", fontsize=8)

# plt.rc('figure', titlesize=8) 
fig.suptitle("Coupled HR Neurons With Nonlinear Conductance Decay, c = 0.01")

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.savefig("nonlinear_g.png", dpi=300)

plt.show()