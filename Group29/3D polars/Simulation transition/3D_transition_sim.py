import numpy as np
import matplotlib.pyplot as plt

def gettransdata(aoa):
    fstring = "wing_sim_trans_aoa" + str(aoa) + ".txt"
    file = open(fstring, 'r')
    lines = file.read().splitlines()
    file.close()

    datalst = []
    for i in range(0, len(lines) - 1):
        datalst.append(lines[i].split())
    data = np.array(datalst)
    tdata = data.astype(float)

    return tdata


data0 = gettransdata(0)
data2 = gettransdata(2)
data4 = gettransdata(4)
data6 = gettransdata(6)
data8 = gettransdata(8)
data10 = gettransdata(10)
data12 = gettransdata(12)
data14 = gettransdata(14)
data16 = gettransdata(16)
metadata = np.array([data0, data2, data4, data6, data8, data10, data12, data14, data16])

fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(data0[:, 1], data0[:, 0], linewidth=1, marker='o', markersize=4, label=r'$\alpha=0\degree$')
ax1.plot(data2[:, 1], data2[:, 0], linewidth=1, marker='1', color='turquoise', markersize=4, label=r'$\alpha=2\degree$')
ax1.plot(data4[:, 1], data4[:, 0], linewidth=1, marker='^', color='orange', markersize=4, label=r'$\alpha=4\degree$')
ax1.plot(data6[:, 1], data6[:, 0], linewidth=1, marker='<', color='red', markersize=4, label=r'$\alpha=6\degree$')
ax1.plot(data8[:, 1], data8[:, 0], linewidth=1, marker='>', color='green', markersize=4, label=r'$\alpha=8\degree$')
ax1.plot(data10[:, 1], data10[:, 0], linewidth=1, marker='s', color='lawngreen', markersize=4,
         label=r'$\alpha=10\degree$')
ax1.plot(data12[:, 1], data12[:, 0], linewidth=1, marker='d', color='blueviolet', markersize=4,
         label=r'$\alpha=12\degree$')
ax1.plot(data14[:, 1], data14[:, 0], linewidth=1, marker='p', color='deeppink', markersize=4,
         label=r'$\alpha=14\degree$')
ax1.plot(data16[:, 1], data16[:, 0], linewidth=1, marker='*', color='saddlebrown', markersize=4,
         label=r'$\alpha=16\degree$')
ax1.set_xlabel(r'Transition location on chord [x/c]', fontsize=16)
ax1.set_ylabel(r'Span [mm]', fontsize=16)
plt.grid()
plt.legend(loc=3, bbox_to_anchor=(0, 1), ncol=5, fontsize=16)
plt.tight_layout()
plt.savefig('Transitions_3d_sim.pdf', dpi=200)
