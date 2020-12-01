import numpy as np
import matplotlib.pyplot as plt
import sys
import pandas as pd

if str(sys.argv[1]) == '-h':
    print('Usage: python plt_2d_fes.py inputfile outputfile')
else:
    inputfile = str(sys.argv[1])
    outputfile = str(sys.argv[2])
    
    f = open(inputfile, 'r') #open file, read only

    header = f.readline()
    min_gyr = float(f.readline().strip().split()[3])
    max_gyr = float(f.readline().strip().split()[3])
    gyr_bins = int(f.readline().strip().split()[3])
    header = f.readline()
    min_distz = float(f.readline().strip().split()[3])
    max_distz = float(f.readline().strip().split()[3])
    distz_bins = int(f.readline().strip().split()[3])
    header = f.readline()

    gyr = np.linspace(min_gyr, max_gyr, gyr_bins)
    distz = np.linspace(min_distz, max_distz, distz_bins)
    fes = np.zeros([gyr_bins, distz_bins])
    row = 0
    col = 0

    for line in f:
        useful_info = line.strip()
        if len(useful_info) != 0:
            columns = useful_info.split()
            fes[row][col] = float(columns[2])
            row += 1
        else:
            col += 1
            row = 0

    plt.rcParams.update({'font.size': 12})
    # Blues_r, terrain, ocean
    c = plt.contourf(distz,gyr,fes*0.239006,20,cmap='Blues_r')
    cbar = plt.colorbar(c)
#    cbar.set_label('Free Energy (kCal/mol)', rotation=270)
    ax = plt.gca()
    
#    for i in range(len(x)):
#        plt.scatter(data.distz[x[i]], data.gyr[x[i]])
    
    plt.title('WT-GrBP5 Free Energy Surface')
    plt.xlabel('Distance from Graphene (nm)')
    plt.ylabel('Radius of Gyration (nm)')
    plt.savefig(outputfile)
