import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def getdata():
    file = open("3D_corr_test.txt", "r")
    lines = file.read().splitlines()    # list of strings of lines
    file.close()

    title = lines[0].split()  # names of parameters (headers of columns in data file)
    lines = lines[2:len(lines)]  # remove headers and unit rows

    datalst = []
    for i in range(len(lines)):
        datalst.append(lines[i].split())  # making 2D list of strings of data in rows

    data = np.array(datalst)  # converting data string list to numpy array
    data = data.astype(float)  # turning the strings into floats
    return data

testdata = getdata()
file = open("wing simulation.txt", "r")
lines = file.read().splitlines()
file.close()

templen = len(lines)
lines = lines[6:templen-2]
lines.pop(1)
datalst = []
for i in range(1, len(lines)):
    datalst.append(lines[i].split())
title = lines[0].split()
data = np.array(datalst)
data = data.astype(float)
# print(data)


print("Avaliable polars:\n 1. All\n 2.CL-alpha\n 3.CD-alpha\n 4.CM-alpha\n 5.CL-CD\n 6.All, exp+sim")
choice = int(input("Choose the desired polar (1-6): "))
doall = False
docomp = False

if choice == 1:
    doall = True
    choice = 2

if choice == 6:
    doall = True
    docomp = True
    choice = 2

if choice == 2:
    if docomp:
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        ax1.plot(testdata[:, 1], testdata[:, 3], linewidth=1, marker='<', color='turquoise', markersize=4,
                 label='Experimental CL-alpha')
        ax1.plot(data[:, 0], data[:, 1], linewidth=1, marker='o', markersize=4, label='Simulated CL-alpha')
        ax1.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax1.set_ylabel(r'$C_L$ [-]', fontsize=16)
        plt.grid()
        plt.legend()
        plt.savefig('CL_alpha_3d_test_vs_sim.pdf', dpi=200)
    else:
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        ax1.plot(data[:, 0], data[:, 1], linewidth=1, marker='o', markersize=4, label='Cl-alpha')
        ax1.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax1.set_ylabel(r'$C_L$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CL_alpha_3dsim.pdf', dpi=200)

    if doall:
        choice = 3

if choice == 3:
    if docomp:
        fig1, ax2 = plt.subplots(figsize=(8, 5))
        ax2.plot(testdata[:, 1], testdata[:, 4], linewidth=1, marker='*', color='deeppink', markersize=4,
                 label='Experimental CD-alpha')
        ax2.plot(data[:, 0], data[:, 2] + data[:, 3] + data[:, 4], linewidth=1, marker='^', markersize=4,
                 color='blueviolet', label='Simulated CD-alpha')
        ax2.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax2.set_ylabel(r'$C_D$ [-]', fontsize=16)
        plt.grid()
        plt.legend()
        plt.savefig('CD_alpha_3d_test_vs_sim.pdf', dpi=200)
    else:
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        ax2.plot(data[:, 0], data[:, 2] + data[:, 3] + data[:, 4], linewidth=1, marker='^', markersize=4,
                 color='purple', label='Cd-alpha')
        ax2.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax2.set_ylabel(r'$C_D$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CD_alpha_3dsim.pdf', dpi=200)
    if doall:
        choice = 4

if choice == 4:
    if docomp: # removed this because idk which of the experiment CM's to use :(
        boss = False
        # fig1, ax3 = plt.subplots(figsize=(8, 5))
        # ax3.plot(testdata[:, 1], testdata[:, 10], linewidth=1, marker='p', color='red', markersize=2.5,
        #          label='Experimental CM-alpha')
        # ax3.plot(data[:, 0], data[:, 6], linewidth=1, marker='s', markersize=2.5, color='orange',
        #          label='Simulated CM-alpha')
        # ax3.set_xlabel(r'$\alpha$ [deg]')
        # ax3.set_ylabel(r'$C_M$ [-]')
        # plt.grid()
        # plt.legend()
        # plt.savefig('CM_alpha_3d_test_vs_sim.pdf', dpi=200)
    else:
        fig3, ax3 = plt.subplots(figsize=(8, 5))
        ax3.plot(data[:, 0], data[:, 6], linewidth=1, marker='s', markersize=4, color='orange', label='Cm-alpha')
        ax3.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax3.set_ylabel(r'$C_M$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CM_alpha_3dsim.pdf', dpi=200)
    if doall:
        choice = 5

if choice == 5:
    if docomp:
        fig1, ax4 = plt.subplots(figsize=(8, 5))
        ax4.plot(testdata[:, 4], testdata[:, 3], linewidth=1, marker='2', color='lawngreen', markersize=4,
                 label='Experimental CL-CD')
        ax4.plot(data[:, 2] + data[:, 3] + data[:, 4], data[:, 1], linewidth=1, marker='1', markersize=4, color='green',
                 label='Simulated CL-CD')
        ax4.set_xlabel(r'$C_D$ [-]', fontsize=16)
        ax4.set_ylabel(r'$C_L$ [-]', fontsize=16)
        plt.grid()
        plt.legend()
        plt.savefig('CL-CD_3d_test_vs_sim.pdf', dpi=200)
    else:
        fig4, ax4 = plt.subplots(figsize=(8, 5))
        ax4.plot(data[:, 2] + data[:, 3] + data[:, 4], data[:, 1], linewidth=1, marker='s', markersize=4, color='red',
                 label='Cl-Cd')
        ax4.set_xlabel(r'$C_D$ [deg]', fontsize=16)
        ax4.set_ylabel(r'$C_L$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CL-CD_3dsim.pdf', dpi=200)


if choice > 6 or choice < 1 or isinstance(choice, int) is False:
    print("Invalid choice!")

plt.tight_layout()

# ax1.legend()
# ax2.legend()
# ax3.legend()
# ax4.legend()
# plt.show()
