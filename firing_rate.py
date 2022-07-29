from imports import *
from HRneuron import *

c = constants()

neuron1 = HRneuron(1) 
time_vec = np.arange(0, c.ms, c.scale)
current_vec = np.zeros(c.iterations) + c.I
# print(time_vec[20])

# neuron1.set_current(1.2)
# neuron1.set_a(1.8)

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

# --------- VARYING I ---------

firing_rate = []
interspike_interval = []
for j in range(3000, 3300):
    neuron1.set_current(j * 0.001)
    for i in range(c.iterations):
        neuron1.calculate_x(i)
        neuron1.calculate_y(i)
        neuron1.calculate_z(i)

    pot = neuron1.xarr

    peaks, other = find_peaks(pot, height=c.MIN_HEIGHT, threshold = 0, distance=c.MIN_DISTANCE, width=c.MIN_WIDTH)
    firing_rate.append(len(peaks) / (c.ms))
    if len(peaks) != 0:
        interspike_interval.append(c.ms/ len(peaks))
    else:
        interspike_interval.append(0) 
    print(j*0.001)

firing_vec = np.arange(3, 3.3, 0.001)

#plt.plot(firing_vec, firing_rate)

# np.save("firing_rate.npy", firing_rate)

plt.plot(firing_vec, firing_rate, linewidth = 1, color="black")
plt.xlabel("Injected Current")
plt.ylabel("Firing Rate (peaks / ms)")
plt.title("Firing Rate Based on Current")
plt.savefig("firing_rate_owo.png", dpi=300)
plt.show()


# --------- VARYING A ---------


# neuron1.set_current(1.5)
# firing_rate = []

# for k in range(10, 20):
#     neuron1.set_current(k * 0.1)
#     for j in range(5, 15):
#         neuron1.set_a(j * 0.2)
#         for i in range(c.iterations):
#             neuron1.calculate_x(i)
#             neuron1.calculate_y(i)
#             neuron1.calculate_z(i)

#         pot = neuron1.xarr

#         peaks, other = find_peaks(pot, height=c.MIN_HEIGHT, threshold = 0, distance=c.MIN_DISTANCE, width=c.MIN_WIDTH)
#         print("current: ", k * 0.1, " a: ", j * 0.2, len(peaks))
#         firing_rate.append(len(peaks) / (c.ms))
#         print(j*0.2)
#     print("K ", k * 0.1)

"""
firing_rate = []
a_list = [1.2, 1.4, 1.6, 1.8]
color_list = ["red", "yellow", "green", "blue"]

for k in range(len(a_list)):
    firing_rate = []
    neuron1.set_a(a_list[k])
    for j in range(50):
        neuron1.set_current(j * 0.1)
        for i in range(c.iterations):
            neuron1.calculate_x(i)
            neuron1.calculate_y(i)
            neuron1.calculate_z(i)

        pot = neuron1.xarr

        peaks, other = find_peaks(pot, height=c.MIN_HEIGHT, threshold = 0, distance=c.MIN_DISTANCE, width=c.MIN_WIDTH)
        firing_rate.append(len(peaks))
        print(j*0.1)

    firing_vec = np.arange(0, 5, 0.1)

    plt.plot(firing_vec, firing_rate, color=color_list[k], label=str(a_list[k]))

plt.xlabel("Injected Current")
plt.ylabel("Firing Rate (peaks / ms)")
plt.title("Firing Rate Based on Current")
leg = plt.legend()
plt.show()
"""