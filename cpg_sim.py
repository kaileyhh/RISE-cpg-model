from imports import *
from HRneuronseg import *
from synapseseg import *

# weight is 5.0 by default, positive is inhibitory
# -5.0 weight would be excitatory connections

pre_botc = HRneuronseg(1)
pico = HRneuronseg(2)
rtn = HRneuronseg(3)

# pico.set_current(2.5)
# rtn.set_current(2.0)

cpg = synapseseg([pre_botc, pico, rtn])

cpg.attach_neurons(pre_botc, pico)
cpg.attach_neurons(pico, pre_botc)
cpg.attach_neurons(pico, rtn)
cpg.attach_neurons(rtn, pico)
cpg.attach_neurons(pre_botc, rtn)
cpg.attach_neurons(rtn, pre_botc)

cpg.create_weight_mat(pre_botc, [5.2, 1.7])
cpg.create_weight_mat(pico, [5.0, 2.5])
cpg.create_weight_mat(rtn, [2.1, 2.0])

for i in range(c.iterations):
    cpg.calculate_weight_all(i)
    print(i)

a = [pre_botc.xarr, pico.xarr, rtn.xarr]
np.save("cpg.npy", a)

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(pre_botc.time_vec, pre_botc.xarr, linewidth=0.5, color="red")
ax2.plot(pico.time_vec, pico.xarr, linewidth=0.5, color="green")
ax3.plot(rtn.time_vec, rtn.xarr, linewidth=0.5, color="blue")

ax4.plot(pre_botc.time_vec, pre_botc.xarr, linewidth=0.5, color="red")
ax4.plot(pico.time_vec, pico.xarr, linewidth=0.5, color="green")
ax4.plot(rtn.time_vec, rtn.xarr, linewidth=0.5, color="blue")

ax1.title.set_text("Pre-BotC (red, I = " + str(pre_botc.current) + " ), x0 = " + str(pre_botc.xR))
ax1.set_xlabel("time (ms)")
ax1.set_ylabel("au")
ax2.title.set_text("PiCo (green, I = " + str(pico.current) + " ), x0 = " + str(pico.xR))
ax2.set_xlabel("time (ms)")
ax2.set_ylabel("au")
ax3.title.set_text("RTN/pFRG (green, I = " + str(rtn.current) + " ), x0 = " + str(rtn.xR))
ax3.set_xlabel("time (ms)")
ax3.set_ylabel("au")
ax4.title.set_text("All Neurons Together")
ax4.set_xlabel("time (ms)")
ax4.set_ylabel("au")

# plt.rc('figure', titlesize=8) 
fig.suptitle("CPG Neurons (I = " + str(c.I) + ")")

plt.show()