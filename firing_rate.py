from imports import *
from HRneuron import *

c = constants()

neuron1 = HRneuron(1) 
time_vec = np.arange(0, c.ms, c.scale)
current_vec = np.zeros(c.iterations) + c.I
# print(time_vec[20])

# neuron1.set_current(3.15)

# for i in range(c.iterations):
#     neuron1.calculate_x(i)
#     neuron1.calculate_y(i)
#     neuron1.calculate_z(i)

# pot = neuron1.xarr

# peaks, other = find_peaks(pot, height=c.MIN_HEIGHT, threshold = 0, distance=c.MIN_DISTANCE, width=c.MIN_WIDTH)

# plt.plot(pot)
# plt.plot(peaks, pot[peaks], "x")
# plt.show()

#forward euler time :D

firing_rate = np.zeros(50)

for j in range(50):
    neuron1.set_current(j * 0.1)
    for i in range(c.iterations):
        neuron1.calculate_x(i)
        neuron1.calculate_y(i)
        neuron1.calculate_z(i)

    pot = neuron1.xarr

    peaks, other = find_peaks(pot, height=c.MIN_HEIGHT, threshold = 0, distance=c.MIN_DISTANCE, width=c.MIN_WIDTH)
    firing_rate[j] = len(peaks) / (c.ms)

firing_vec = np.arange(0, 5, 0.1)

plt.plot(firing_vec, firing_rate)
plt.xlabel("Injected Current")
plt.ylabel("Firing Rate (peaks / ms)")
plt.title("Firing Rate Based on Current")
plt.show()


