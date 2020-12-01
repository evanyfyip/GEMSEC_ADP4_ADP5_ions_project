#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:44:54 2020

@author: Evan Yip
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12})

##### DIST CV
dist = pd.DataFrame(np.loadtxt('WT_dist_fes.txt')) # input file
dist.columns = ['cv', 'fe'] # renaming columns
dist.fe = dist.fe * 0.239006 # kJ/mol to kCal/mol

# plot
fig = plt.figure()
plt.grid()
plt.plot(dist.cv, dist.fe)
plt.title('Free Energy Surface - Dist CV')
plt.ylabel('Free Energy (kCal/mol)')
plt.xlabel('Dist to graphene (nm)')
plt.show()
fig.savefig('wt_fes_dist.png')


##### RGYR CV
gyr = pd.DataFrame(np.loadtxt('WT_gyr_fes.txt'))
gyr.columns = ['cv', 'fe']
gyr.fe = gyr.fe * 0.239006 # kJ/mol to kCal/mol

fig = plt.figure()
plt.grid()
plt.plot(gyr.cv, gyr.fe)
plt.title('Free Energy Surface - RGYR CV')
plt.ylabel('Free Energy (kCal/mol)')
plt.xlabel('Radius of Gyration (nm)')
plt.show()
fig.savefig('wt_fes_gyr.png')


##### CONVERGENCE
conv = pd.DataFrame(np.loadtxt('fes_conv_8A_100ns.txt'))
conv.columns = ['step', 'fe']
conv.fe = conv.fe * 0.239006 # kJ/mol to kCal/mol

# taking differences in convergence
a = conv.fe[:-1]
b = conv.fe[1:]
a.index = b.index
diff = a - b
diff.index = diff.index/2

fig = plt.figure()
plt.grid()
plt.plot(diff)
plt.title('Free Energy Convergence of WT-GrBP5-8A')
plt.ylabel('Free Energy (kCal/mol)')
plt.xlabel('Time (ns)')
plt.show()
fig.savefig('fes_conv_wt8a_100ns.png')
