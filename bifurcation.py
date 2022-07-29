#from sniffio import current_async_library
from imports import *
from HRneuron import *

c = constants()
neuron1 = HRneuron(1)

currents = np.arange(0,4.0,0.002)

# y = []
# for current in currents:
#     timeintervals = []

#     for j in range(c.iterations):
#         neuron1.calculate_x(j,current)
#         neuron1.calculate_y(j)
#         neuron1.calculate_z(j)
#     print("done with ",current)

#     pot = neuron1.xarr

#     peaks, other = find_peaks(pot, height=c.MIN_HEIGHT, threshold = 0, distance=c.MIN_DISTANCE, width=c.MIN_WIDTH)
#     for k in range(len(peaks)-1):
#         time = (peaks[k+1]-peaks[k]) * c.scale
#         timeintervals.append(time)
    

#     y.append(timeintervals)

# np.save("y.npy", y)

y = np.load("y.npy", allow_pickle=True)

for l in range(len(currents)):
    for m in range(len(y[l])):
        plt.scatter(currents[l],y[l][m], s = 0.5, color = 'black')

plt.title("Bifurcation Diagram - HR Neuron")
plt.ylabel("ISI")
plt.xlabel("I (a.u.)")
plt.savefig("Bifurcation_clear.png", dpi=300)
plt.show()
#print(y)

