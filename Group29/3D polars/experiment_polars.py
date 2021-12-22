import numpy
import numpy as np
import csv
import matplotlib.pyplot as plt


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
# print(data)

# finding slope to find where change = sep bubble
slopelst = []
xlst = []
xrangelst = []
for i in range(len(data[:, 1])-1):
    xlst.append((data[i + 1, 1] + data[i, 1]) / 2)
    xrangelst.append(str(data[i, 1]) + " - " + str(data[i + 1, 1]))
    slopelst.append(round((data[i + 1, 3] - data[i, 3]) / (data[i + 1, 1] - data[i, 1]), 3))

reslst = [xrangelst, slopelst]
res = np.array(reslst)
res = np.transpose(res)
fields = ['AoA range', 'CL slope']

with open('CL_alpha_experiment.csv', 'w', newline='') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(res)

# fig1, ax1 = plt.subplots(figsize=(8,5))
# ax1.plot(xlst, slopelst, linewidth=1, marker='o', markersize=2.5, label='Cl slope')
# # ax1.set_title('$C_L-\alpha$')
# ax1.set_xlabel(r'$\alpha$ [deg]')
# ax1.set_ylabel(r'${C_L}_\alpha$ [-]')
# plt.grid()
# plt.show()



# print("Avaliable polars:\n 1. All\n 2.CL-alpha\n 3.CD-alpha\n 4.CMpitch-alpha\n 5.CMroll-alpha\n 6.CMyaw-alpha\n"
#       " 7.CL-CD")
# choice = int(input("Choose the desired polar (1-7): "))
# all = False
#
# if choice==1:
#     all = True
#     choice = 2
#
# if choice==2:
#     # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)  # only for visualising all 4 at once
#     # fig.set_size_inches(8, 5)
#     fig1, ax1 = plt.subplots(figsize=(8,5))
#     ax1.plot(data[:,1], data[:,3], linewidth=1, marker='o', markersize=2.5, label='Cl-alpha')
#     # ax1.set_title('$C_L-\alpha$')
#     ax1.set_xlabel(r'$\alpha$ [deg]')
#     ax1.set_ylabel(r'$C_L$ [-]')
#     plt.grid()
#     plt.savefig('CL_alpha_3dtest.pdf', dpi=200)
#     if all==True:
#         choice = 3
#
# if choice==3:
#     fig2, ax2 = plt.subplots(figsize=(8,5))
#     ax2.plot(data[:,1], data[:,4], linewidth=1, marker='^', markersize=2, color='purple', label='Cd-alpha')
#     # ax2.set_title('Cd-alpha')
#     ax2.set_xlabel(r'$\alpha$ [deg]')
#     ax2.set_ylabel(r'$C_D$ [-]')
#     plt.grid()
#     plt.savefig('CD_alpha_3dtest.pdf', dpi=200)
#     if all==True:
#         choice = 4
#
# if choice==4:
#     fig3, ax3 = plt.subplots(figsize=(8,5))
#     ax3.plot(data[:,1], data[:,11], linewidth=1, marker='s', markersize=2, color='orange', label='Cm-alpha')
#     # ax3.set_title('Cm_pitch-alpha')
#     ax3.set_xlabel(r'$\alpha$ [deg]')
#     ax3.set_ylabel(r'$(C_M)_{pitch}$ [-]')
#     plt.grid()
#     plt.savefig('CMpitch_alpha_3dtest.pdf', dpi=200)
#     if all==True:
#         choice = 5
#
# if choice==5:
#     fig4, ax4 = plt.subplots(figsize=(8,5))
#     ax4.plot(data[:,1], data[:,10], linewidth=1, marker='s', markersize=2, color='orange', label='Cm-alpha')
#     ax4.set_xlabel(r'$\alpha$ [deg]')
#     ax4.set_ylabel(r'$(C_M)_{roll}$ [-]')
#     plt.grid()
#     plt.savefig('CMroll_alpha_3dtest.pdf', dpi=200)
#     if all==True:
#         choice = 6
#
# if choice==6:
#     fig5, ax5 = plt.subplots(figsize=(8,5))
#     ax5.plot(data[:,1], data[:,12], linewidth=1, marker='s', markersize=2, color='orange', label='Cm-alpha')
#     ax5.set_xlabel(r'$\alpha$ [deg]')
#     ax5.set_ylabel(r'$(C_M)_{yaw}$ [-]')
#     plt.grid()
#     plt.savefig('CMyaw_alpha_3dtest.pdf', dpi=200)
#     if all==True:
#         choice = 7
#
# if choice==7:
#     fig6, ax6 = plt.subplots(figsize=(8,5))
#     ax6.plot(data[:,4], data[:,3], linewidth=1, marker='D', markersize=2, color='red', label='Cl-Cd')
#     # ax4.set_title('Cl-Cd')
#     ax6.set_xlabel(r'$C_D$ [-]')
#     ax6.set_ylabel(r'$C_L$ [-]')
#     plt.grid()
#     plt.savefig('CL_CD_3dtest.pdf', dpi=200)
#
# if choice > 7 or choice < 1 or isinstance(choice, int) is False:
#     print("Invalid choice!")
#
# plt.tight_layout()
# ax1.legend()
# ax2.legend()
# ax3.legend()
# ax4.legend()
# plt.savefig('3D_test_polars.pdf', dpi=200)

# plt.show()