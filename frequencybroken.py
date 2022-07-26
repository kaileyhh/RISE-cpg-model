from imports import *
from HRneuron import *

c = constants()

neuron1 = HRneuron(1) 
time_vec = np.arange(0, c.ms, c.scale)
current_vec = np.zeros(c.iterations) + c.I

threshold = -1.05
currently_spiking = False
total = np.zeros(40)
freq = np.zeros(40)


for j in range(40):
    dips = 0
    
    neuron1.set_current(j * 0.1)
    for i in range(c.iterations):
        neuron1.calculate_x(i)
        neuron1.calculate_y(i)
        neuron1.calculate_z(i)
        if (not currently_spiking):
            if (neuron1.x >= threshold-.00001 and neuron1.x <= threshold+.00001):
                currently_spiking = True
        else:
            if (neuron1.x >= threshold-.00001 and neuron1.x <= threshold+.00001):
                currently_spiking = False
                dips += 1
        
    print(j)           


    

    
    freq[j] = dips / (c.ms)
    total[j] = dips

firing_vec = np.arange(0, 4, 0.1)


fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax1.plot(firing_vec, freq)
ax2.plot(firing_vec, total)
plt.show()

# plt.plot(firing_vec, freq)
# plt.xlabel("Injected Current")
# plt.ylabel("Frequency (group of peaks / ms)")
# plt.title(" Frequency vs Current")
# plt.show()