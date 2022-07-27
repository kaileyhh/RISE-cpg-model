#hr coupled duplicate to map x vs y
from imports import *
from HRneuron import *
from synapse import *

# insert main code here :D

c = constants()
thiscurr = input("input current: ")

neuron1 = HRneuron(1) 
neuron1.set_current(float(thiscurr))
c.set_current(float(thiscurr))
time_vec = np.arange(0, c.ms, c.scale)
current_vec = np.zeros(c.iterations) + c.I
# print(time_vec[20])
# print("hi")
# print(thiscurr)
# print(neuron1.current)


#forward euler time :D

for i in range(c.iterations):
    neuron1.calculate_x(i)
    neuron1.calculate_y(i)
    neuron1.calculate_z(i)

# plt.plot(neuron1.xarr, neuron1.yarr)
# plt.title("x vs y")
# plt.xlabel("current")
# plt.ylabel("ion transport rate")
# plt.show()

#removing first data points in x and y
xshort = [0.0]*(len(neuron1.xarr)-2000)
yshort = [0.0]*(len(neuron1.yarr)-2000)
for i in range (2000,len(neuron1.xarr)):
    xshort[i-2000] = neuron1.xarr[i]
    yshort[i-2000] = neuron1.yarr[i]
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(xshort, yshort)
ax2.plot(neuron1.xarr, neuron1.yarr)
ax3.plot(time_vec, neuron1.zarr)
ax4.plot(time_vec, current_vec)

ax1.title.set_text("x vs y without init spike")
ax1.set_xlabel("current")
ax1.set_ylabel("ion transport rate")
ax2.title.set_text("x vs y full")
ax2.set_xlabel("current")
ax2.set_ylabel("ion transport rate")
ax3.title.set_text("Adaptation Current")
ax3.set_xlabel("time (ms)")
ax3.set_ylabel("au")
ax4.title.set_text("Injected Current")
ax4.set_xlabel("time (ms)")
ax4.set_ylabel("au")

if (c.I < 1.2):
    fig.suptitle("Quiescence")
elif (c.I < 1.4):
    fig.suptitle("Spiking")
elif (c.I < 3.1):
    fig.suptitle("Bursting")
elif (c.I < 3.2):
    fig.suptitle("Aperiodic")
else:
    fig.suptitle("Fast Spiking")


plt.subplots_adjust(left=0.1,
                    bottom=0.1, 
                    right=0.9, 
                    top=0.9, 
                    wspace=0.4, 
                    hspace=0.4)

plt.show()

