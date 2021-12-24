import numpy as np
import matplotlib.pyplot as plt

file = open("transition_points_more.txt", "r")
lines = file.read().splitlines()    # list of strings of lines
file.close()


title = lines[0].split()  # names of parameters (headers of columns in data file)
lines = lines[1:len(lines)]  # remove headers

datalst = []
for i in range(len(lines)):
    datalst.append(lines[i].split())  # making 2D list of strings of data in rows

data = np.array(datalst)  # converting data string list to numpy array
data = data.astype(float)  # turning the strings into floats

fig, ax1 = plt.subplots(figsize=(8, 5))
ax1.plot(data[:, 2], data[:, 3], linewidth=1, marker='o', color='red', markersize=4,
         label='Simulated transition pos. at Re=7e5')
ax1.plot([-2, -1, 0, 1, 2, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13,
         13.5, 14, 14.5, 15, 15.5, 16, 16.5, 17, 16, 16.5, 15.5, 15, 14.5, 14, 13.5], [0.69, 0.69, 0.67, 0.64, 0.62,
                                                                                       0.6, 0.57, 0.57, 0.55, 0.51, 0.7,
                                                                                       0.21, 0.13, 0.08, 0.06, 0.05,
                                                                                       0.04, 0.03, 0.03, 0.03, 0.03,
                                                                                       0.02, 0.02, 0.02, 0.02, 0.02,
                                                                                       0.02, 0.02, 0.02, 0.02, 0.02, 0,
                                                                                       0, 0, 0, 0, 0, 0, 0, 0, 0],
         linewidth=1, marker='s', markersize=4, label='Experimental transition pos. at Re=1e6')
ax1.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
ax1.set_ylabel(r'Transition point location [x/c]', fontsize=16)
plt.grid()
plt.legend(fontsize=11)
plt.tight_layout()
plt.savefig('Transition_points_exp_vs_sim.pdf', dpi=200)
