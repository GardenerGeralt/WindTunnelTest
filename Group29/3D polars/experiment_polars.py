import numpy
import numpy as np
import matplotlib.pyplot as plt
import simulation_polars as sp

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
# print(data)

data = getdata()

if sp.runrest:
    print("Avaliable polars:\n 1. All\n 2.CL-alpha\n 3.CD-alpha\n 4.CMpitch-alpha\n 5.CMroll-alpha\n 6.CMyaw-alpha\n"
          " 7.CL-CD")
    choice = int(input("Choose the desired polar (1-7): "))
    all = False

    if choice==1:
        all = True
        choice = 2

    if choice==2:
        # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)  # only for visualising all 4 at once
        # fig.set_size_inches(8, 5)
        fig1, ax1 = plt.subplots(figsize=(8,5))
        ax1.plot(data[:,1], data[:,3], linewidth=1, marker='o', markersize=4, label='Cl-alpha')
        # ax1.set_title('$C_L-\alpha$')
        ax1.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax1.set_ylabel(r'$C_L$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CL_alpha_3dtest.pdf', dpi=200)
        if all:
            choice = 3

    if choice==3:
        fig2, ax2 = plt.subplots(figsize=(8,5))
        ax2.plot(data[:,1], data[:,4], linewidth=1, marker='^', markersize=4, color='purple', label='Cd-alpha')
        # ax2.set_title('Cd-alpha')
        ax2.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax2.set_ylabel(r'$C_D$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CD_alpha_3dtest.pdf', dpi=200)
        if all:
            choice = 4

    if choice==4:
        fig3, ax3 = plt.subplots(figsize=(8,5))
        ax3.plot(data[:,1], data[:,11], linewidth=1, marker='s', markersize=4, color='orange', label='Cm-alpha')
        # ax3.set_title('Cm_pitch-alpha')
        ax3.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax3.set_ylabel(r'$(C_M)_{pitch}$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CMpitch_alpha_3dtest.pdf', dpi=200)
        if all:
            choice = 5

    if choice==5:
        fig4, ax4 = plt.subplots(figsize=(8,5))
        ax4.plot(data[:,1], data[:,10], linewidth=1, marker='s', markersize=4, color='orange', label='Cm-alpha')
        ax4.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax4.set_ylabel(r'$(C_M)_{roll}$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CMroll_alpha_3dtest.pdf', dpi=200)
        if all:
            choice = 6

    if choice==6:
        fig5, ax5 = plt.subplots(figsize=(8,5))
        ax5.plot(data[:,1], data[:,12], linewidth=1, marker='s', markersize=4, color='orange', label='Cm-alpha')
        ax5.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
        ax5.set_ylabel(r'$(C_M)_{yaw}$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CMyaw_alpha_3dtest.pdf', dpi=200)
        if all:
            choice = 7

    if choice==7:
        fig6, ax6 = plt.subplots(figsize=(8,5))
        ax6.plot(data[:,4], data[:,3], linewidth=1, marker='D', markersize=4, color='red', label='Cl-Cd')
        # ax4.set_title('Cl-Cd')
        ax6.set_xlabel(r'$C_D$ [-]', fontsize=16)
        ax6.set_ylabel(r'$C_L$ [-]', fontsize=16)
        plt.grid()
        plt.savefig('CL_CD_3dtest.pdf', dpi=200)

    if choice > 7 or choice < 1 or isinstance(choice, int) is False:
        print("Invalid choice!")
