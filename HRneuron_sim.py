from re import A
from imports import *
from HRneuron import *
# from synapse import *

# insert main code here :D

c = constants()

neuron1 = HRneuron(1) 
neuron2 = HRneuron(2)
time_vec = np.arange(0, c.ms, c.scale)
sensory_vec = np.zeros(c.iterations) 

temp = 0
oscillate = False
min_c = 10
max_c = 11


# print(time_vec[20])

gain = 1.0

#forward euler time :D

min_bound = 100 * 1000
max_bound = 225 * 1000

# a = [np.zeros(max_bound-min_bound)]
a = []

for j in range (100*1000, 200*1000, 1000):
    print(j)
    sensory_vec = np.zeros(c.iterations) 
    sensory_vec[j:j + 2 * 1000] = 1.0
    for i in range(c.iterations):
        neuron1.calculate_x_sensory(i, gain, sensory_vec[i])
        neuron1.calculate_y(i)
        neuron1.calculate_z(i)
        neuron2.calculate_x(i)
        neuron2.calculate_y(i)
        neuron2.calculate_z(i)
    # plt.figure()
    # plt.plot(neuron1.xarr)
    # plt.plot(neuron2.xarr, color="green")
    # plt.show()
    # neuron1.xarr = neuron1.xarr[min_bound:max_bound]
    # neuron2.xarr = neuron2.xarr[min_bound:max_bound]
    peaks1, other = find_peaks(neuron1.xarr, height=c.MIN_HEIGHT, threshold = 0, distance=c.MIN_DISTANCE, width=c.MIN_WIDTH)

    peaks2, other = find_peaks(neuron2.xarr, height=c.MIN_HEIGHT, threshold = 0, distance=c.MIN_DISTANCE, width=c.MIN_WIDTH)

    peaks1 = peaks1[np.where(peaks1 > j)]
    peaks2 = peaks2[np.where(peaks2 > j)]

    temp1 = peaks1[1]
    temp2 = peaks2[1]
    # temp1 = np.where(neuron1.xarr>=1)
    # print(temp1)
    # # print(temp1)

    # temp1 = temp1[0][-1]
    

    # temp2 = np.where(neuron2.xarr>=1)
    # temp2 = temp2[0][-1]
    a = np.append(a, temp1 - temp2)
    print(temp1, temp2, temp1-temp2)
    # a = np.append(a, [np.array(neuron1.xarr[min_bound:max_bound] - neuron2.xarr[min_bound:max_bound])], axis = 0)
# print(a)

np.save("a.npy", a)

# peaks1, other = find_peaks(neuron1.xarr, height=c.MIN_HEIGHT, threshold = 0, distance=c.ISI_DISTANCE, width=c.MIN_WIDTH)
# peaks2, other = find_peaks(neuron2.xarr, height=c.MIN_HEIGHT, threshold = 0, distance=c.ISI_DISTANCE, width=c.MIN_WIDTH)

# if len(peaks2) < len(peaks1):
#     peaks2 = np.append(peaks2, [0 for i in range(len(peaks1) - len(peaks2))])

# elif len(peaks1) < len(peaks2):
#     peaks1 = np.append(peaks1, [0 for i in range(len(peaks2) - len(peaks1))])

# peaksa = peaks1 - peaks2

# print(len(peaks1), len(peaks2))

fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)



ax1.plot(time_vec[min_bound:max_bound], neuron1.xarr[min_bound:max_bound], linewidth = 0.5, color="red")
# ax1.plot(peaks1, neuron1.xarr[peaks1], "x")
ax2.plot(time_vec[min_bound:max_bound], neuron2.xarr[min_bound:max_bound], linewidth = 0.5, color="green")
# ax2.plot(peaks2, neuron2.xarr[peaks2], "x")
ax3.plot(time_vec[min_bound:max_bound], neuron1.xarr[min_bound:max_bound], linewidth = 0.5, color="red")
ax3.plot(time_vec[min_bound:max_bound], neuron2.xarr[min_bound:max_bound], linewidth = 0.5, color="green")
ax4.plot(time_vec[min_bound:max_bound], neuron1.xarr[min_bound:max_bound] - neuron2.xarr[min_bound:max_bound], linewidth = 0.5, color="black")

plt.rc('font', size=8) 
plt.rc('figure', titlesize=8) 
plt.rc('axes', titlesize=8) 
plt.rc('axes', labelsize=8) 

ax1.title.set_text("Neuron 1 (Stimulated")
ax1.set_xlabel("time (ms)")
ax1.set_ylabel("au")
ax2.title.set_text("Neuron 2 (Normal)")
ax2.set_xlabel("time (ms)")
ax2.set_ylabel("au")
ax3.title.set_text("Both Membrane Potentials")
ax3.set_xlabel("time (ms)")
ax3.set_ylabel("au")
ax4.title.set_text("Phase Change")
ax4.set_xlabel("peak #")
ax4.set_ylabel("time (ms)")

# if (c.I < 1.2):
#     fig.suptitle("Quiescence")
# elif (c.I < 1.4):
#     fig.suptitle("Spiking")
# elif (c.I < 3.1):
#     fig.suptitle("Bursting")
# elif (c.I < 3.2):
#     fig.suptitle("Aperiodic")
# else:
#     fig.suptitle("Fast Spiking")

fig.suptitle("2 uncoupled neurons (I = 1.4); neuron 1 receives sensory excitation for 200ms")

# np.savetxt('data.csv', neuron1.xarr, delimiter=',', fmt='%f')


plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.savefig("sensory_phase_shift.png", dpi=300)

plt.show()

