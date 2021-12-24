import numpy as np
import matplotlib.pyplot as plt

file = open("transition_points_text.txt", "r")
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
ax1.plot(data[:, 0], data[:, 1], linewidth=1, marker='<', color='orange', markersize=4,
         label='Transition pos. at Re=5e5')
ax1.plot(data[:, 0], data[:, 3], linewidth=1, marker='<', color='red', markersize=4,
         label='Transition pos. at Re=7e5')
ax1.plot(data[:, 0], data[:, 5], linewidth=1, marker='<', markersize=4,
         label='Transition pos. at Re=1e6')
ax1.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
ax1.set_ylabel(r'Transition point location [x/c]', fontsize=16)
plt.grid()
plt.legend()
plt.savefig('Transition_points_graph.pdf', dpi=200)