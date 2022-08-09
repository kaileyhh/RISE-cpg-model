from imports import *

# plt.figure()
# plt.title("Phase Portrait at I = 3.15 (Poincare section at y = -2.5)")
# plt.ylabel("ion transport rate",fontsize=12)
# plt.xlabel("membrane potential",fontsize=12)
# plt.savefig("helper.png", dpi=300)
# plt.show()

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.set_title("HR Neurons with Synchrony")
ax1.set_xlabel("time (ms)", fontsize=8)
ax1.set_ylabel("membrane potential (au)", fontsize=8)
ax2.set_title("Modulation Value (m)")
ax2.set_xlabel("time (ms)", fontsize=8)
ax2.set_ylabel("m (au)", fontsize=8)
ax3.set_title("Neuron 1, I = 7.0", fontsize=8)
ax3.set_xlabel("time (ms)", fontsize=8)
ax3.set_ylabel("membrane potential (au)", fontsize=8)

ax4.set_title("Neuron 2, I = 4.0", fontsize=8)
ax4.set_xlabel("time (ms)", fontsize=8)
ax4.set_ylabel("membrane potential (au)", fontsize=8)

# plt.rc('figure', titlesize=8) 
fig.suptitle("Coupled HR Neurons With Nonlinear Conductance Decay, c = 0.16")

plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.savefig("nonlinear_g.png", dpi=300)

plt.show()