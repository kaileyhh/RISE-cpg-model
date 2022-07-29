from imports import *
from HRneuron import *
# from synapse import *

# insert main code here :D

c = constants()

neuron1 = HRneuron(1) 
time_vec = np.arange(0, c.ms, c.scale)
current_vec = np.zeros(c.iterations) + c.I
# print(time_vec[20])



#forward euler time :D

for i in range(c.iterations):
    neuron1.calculate_x(i)
    neuron1.calculate_y(i)
    neuron1.calculate_z(i)

plt.figure()
plt.plot(time_vec, neuron1.xarr, linewidth=0.5, color="black")

plt.xlabel("time (ms)")
plt.ylabel("Membrane Potential (au)")

if (c.I < 1.2):
    plt.title("Quiescence, I = " + str(c.I))
elif (c.I < 1.4):
    plt.title("Spiking, I = " + str(c.I))
elif (c.I < 3.1):
    plt.title("Bursting, I = " + str(c.I))
elif (c.I < 3.2):
    plt.title("Aperiodic, I = " + str(c.I))
else:
    plt.title("Fast Spiking, I = " + str(c.I))

# np.savetxt('data.csv', neuron1.xarr, delimiter=',', fmt='%f')


plt.savefig("aperiodic_black.png", dpi=300)

plt.show()

