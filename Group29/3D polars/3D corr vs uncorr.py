import numpy as np
import matplotlib.pyplot as plt

def getdata(filename):
    file = open(filename, "r")
    lines = file.read().splitlines()    # list of strings of lines
    file.close()

    title = lines[0].split()  # names of parameters (headers of columns in data file)
    lines = lines[2:len(lines)]  # remove headers and unit rows

    datalst = []
    for i in range(len(lines)):
        datalst.append(lines[i].split())  # making 2D list of strings of data in rows

    datastr = np.array(datalst)  # converting data string list to numpy array
    data = datastr.astype(float)  # turning the strings into floats
    return data


cdata = getdata("3D_corr_test.txt")
ucdata = getdata("3D_unc_test.txt")

print("Avaliable polars:\n 1. All\n 2.CL-alpha\n 3.CD-alpha\n 4.CMpitch-alpha\n 5.CMroll-alpha\n 6.CMyaw-alpha\n"
      " 7.CL-CD")
choice = int(input("Choose the desired polar (1-7): "))
all = False

if choice == 1:
    all = True
    choice = 2

if choice == 2:
    # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)  # only for visualising all 4 at once
    # fig.set_size_inches(8, 5)
    fig1, ax1 = plt.subplots(figsize=(8, 5))
    ax1.plot(cdata[:, 1], cdata[:, 3], linewidth=1, marker='o', markersize=4, label=r'Corrected $C_L-\alpha$')
    ax1.plot(ucdata[:, 1], ucdata[:, 3], linewidth=1, marker='o', markersize=3, color='grey',
             label=r'Uncorrected $C_L-\alpha$')
    # ax1.set_title('$C_L-\alpha$')
    ax1.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
    ax1.set_ylabel(r'$C_L$ [-]', fontsize=16)
    plt.grid()
    plt.legend(fontsize=11)
    plt.savefig('CL_alpha_3d_exp_unc_vs_corr.pdf', dpi=200)
    if all:
        choice = 3

if choice == 3:
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    ax2.plot(cdata[:, 1], cdata[:, 4], linewidth=1, marker='^', markersize=4, color='purple',
             label=r'Corrected $C_D-\alpha$')
    ax2.plot(ucdata[:, 1], ucdata[:, 4], linewidth=1, marker='^', markersize=3, color='grey',
             label=r'Uncorrected $C_D-\alpha$')
    # ax2.set_title('Cd-alpha')
    ax2.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
    ax2.set_ylabel(r'$C_D$ [-]', fontsize=16)
    plt.grid()
    plt.legend(fontsize=11)
    plt.savefig('CD_alpha_3d_exp_unc_vs_corr.pdf', dpi=200)
    if all:
        choice = 4

if choice == 4:
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    ax3.plot(cdata[:, 1], cdata[:, 11], linewidth=1, marker='s', markersize=4, color='orange',
             label=r'Corrected $(C_M)_{pitch}-\alpha$')
    ax3.plot(ucdata[:, 1], ucdata[:, 11], linewidth=1, marker='s', markersize=3, color='grey',
             label=r'Uncorrected $(C_M)_{pitch}-\alpha$')
    # ax3.set_title('Cm_pitch-alpha')
    ax3.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
    ax3.set_ylabel(r'$(C_M)_{pitch}$ [-]', fontsize=16)
    plt.grid()
    plt.legend(fontsize=11)
    plt.savefig('CMpitch_alpha_3d_exp_unc_vs_corr.pdf', dpi=200)
    if all:
        choice = 5

if choice == 5:
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    ax4.plot(cdata[:, 1], cdata[:, 10], linewidth=1, marker='s', markersize=4, color='orange',
             label=r'Corrected $(C_M)_{roll}-\alpha')
    ax4.plot(ucdata[:, 1], ucdata[:, 10], linewidth=1, marker='s', markersize=3, color='grey',
             label=r'Uncorrected $(C_M)_{roll}-\alpha')
    ax4.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
    ax4.set_ylabel(r'$(C_M)_{roll}$ [-]', fontsize=16)
    plt.grid()
    plt.legend(fontsize=11)
    plt.savefig('CMroll_alpha_3d_exp_unc_vs_corr.pdf', dpi=200)
    if all:
        choice = 6

if choice == 6:
    fig5, ax5 = plt.subplots(figsize=(8, 5))
    ax5.plot(cdata[:, 1], cdata[:, 12], linewidth=1, marker='s', markersize=4, color='orange',
             label=r'Corrected $(C_M)_{yaw}-\alpha')
    ax5.plot(ucdata[:, 1], ucdata[:, 12], linewidth=1, marker='s', markersize=3, color='grey',
             label=r'Uncorrected $(C_M)_{yaw}-\alpha')
    ax5.set_xlabel(r'$\alpha$ [deg]', fontsize=16)
    ax5.set_ylabel(r'$(C_M)_{yaw}$ [-]', fontsize=16)
    plt.grid()
    plt.legend(fontsize=11)
    plt.savefig('CMyaw_alpha_3d_exp_unc_vs_corr.pdf', dpi=200)
    if all:
        choice = 7

if choice == 7:
    fig6, ax6 = plt.subplots(figsize=(8, 5))
    ax6.plot(cdata[:, 4], cdata[:, 3], linewidth=1, marker='D', markersize=4, color='red', label=r'Corrected $C_L-C_D$')
    ax6.plot(ucdata[:, 4], ucdata[:, 3], linewidth=1, marker='D', markersize=3, color='grey',
             label=r'Uncorrected $C_L-C_D$')
    # ax4.set_title('Cl-Cd')
    ax6.set_xlabel(r'$C_D$ [-]', fontsize=16)
    ax6.set_ylabel(r'$C_L$ [-]', fontsize=16)
    plt.grid()
    plt.legend(fontsize=11)
    plt.savefig('CL_CD_3d_exp_unc_vs_corr.pdf', dpi=200)

if choice > 7 or choice < 1 or isinstance(choice, int) is False:
    print("Invalid choice!")

plt.tight_layout()
