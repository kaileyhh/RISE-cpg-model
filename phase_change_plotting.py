from imports import *

c = constants()

a = np.load("a.npy")
# print(a)

a = a / 1000


time_vec = np.arange(100, 200, 1)
# print(len(a[1]), len(time_vec))

arr = []


plt.figure()
plt.scatter(time_vec, a, s=1, color="black")
plt.xlabel("stimulus start (ms)")
plt.ylabel("phase change (ms)")

plt.title("Phase Change based on Stimulus Timing")

# for i in range(len(a))
    # plt.savefig("figs/"+str(i)+".png")
    # arr += ["figs/"+str(i)+".png"]

plt.savefig("phase_change_scatter.png", dpi=300)
plt.show()
# print(arr)
# # plt.scatter(time_vec, a[4], s=1, color="black")
# # plt.show()

# with imageio.get_writer('mygif.gif', mode='I') as writer:
#     for filename in arr:
#         image = imageio.imread(filename)
#         writer.append_data(image)