# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:17:03 2020

@author: evan
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

    
hills = pd.DataFrame(np.loadtxt('HILLS'))
hills.columns = ['time', 'gyr', 'sigma_gyr', 'height', 'biasf']


# Plotting
fig = plt.figure()
plt.grid()
plt.plot(hills.time, hills.height)
plt.title('MetaD Gaussian Heights')
plt.ylabel('Gaussian height [kJoule/mol]')
plt.xlabel('simulation time')
plt.show()

# Plotting radius of gyration
fig = plt.figure()
plt.grid()
plt.scatter(hills.time, hills.gyr, marker='+', s=5, c='r')
plt.title('MetaD gyration')
plt.ylabel('radius of gyration [nm]')
plt.xlabel('simulation time')
plt.show()

# Convergence -- after running analyzefes.sh
energy_diff = pd.DataFrame(np.loadtxt('conv.txt')) # input file
energy_diff.columns = ['time', 'energy'] 
fig = plt.figure()
plt.grid()
plt.scatter(energy_diff.time, energy_diff.energy)
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Convergence')
plt.scatter()