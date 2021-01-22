# GEMSEC_ADP4_ADP5_ions_project
Summer 2020 GEMSEC dental and computational biology research project: Evan Yip and Tatum Hennig
Files: analyze_fes.py, metaD_analysis.py, metaD_plot_fes.py, peptide_builder.py, plt_2d_fes.py, sort_mol2_bonds.py

## Motivation
To provide a molecular dynamics explanation for the differing nucleation characteristics between ADP4 and sADP5. 


## Contents
This project contains python code to build files needed for molecular and metadynamics simulation as well as analysis on metadynamics output files

**Note:** These files run under the assumption that the user has various python packages (numpy, matplotlib.pyplot, pandas). In addition, these files were utilized to analyze metadynamics output files from GROMACS.

**analyze_fes.py:** This file contains a sample python analysis of the HILLS file extracted from a metad simulation. To use this file, open it in spyder, make sure that the HILLS file is in the current working directory and adjust desired column names based off of the cvs of the simulation. The output plots of this file should include the Gaussian heights vs time steps and the sampled values of the collected variable (e.g. radius of gyration) vs time over the course of the metaD simulation. In addition, this file contains code to analyze the convergence file (e.g. "conv.txt") which is an output from the analyzefes.sh command.

**metaD_analysis.py:** This file contains python code to analyze the free energy surface of the peptide during the MetaDynamics simulation. This file assumes that the user has used the plumed sum_hills command on the trajectory file and generated an output file of the form pep_cv_fes.dat (which can then be converted to a .txt file). The information from the fes file can then be extracted to generate plots of Free Energy vs CV (e.g. distance or radius of gyration). Minima of these plots can give insights as to the low energy conformations of the peptide. If there are at least two distinct energy wells, their positions can be utilized to determine if the simulation has converged.

**metaD_plot_fes.py:** This is the same as metaD_analysis.py???

**peptide_builder.py:** This file contains example python code on how to create a pdb file for a peptide solely based upon amino acid sequence. This file utilizes the PeptideBuilder package and Bio.PDB. The pdb files can then be utilized for GROMACS simulations.

**plt_2d_fes.py:** This file plots the 2D free energy surface of a metadynamics simulation with 2 CVs. As a caveat it may require some fine tuning to ensure the plot titles and labels are correct. This file also assumes that the plumed sum_hills for 2 cvs has been utilized. See MetaD-PeptideAdsorptionGraphene Protocol.

**sort_mol2_bonds.py:** This file is a script to reorder atoms in a .mol2 file to adhere to a convention consistenet with GROMACS. It is necessary for the addition of ions or other ligands not already present within GROMACS. The sorting convention is described more in detail within the file. To run it, sort_mol2_bonds.py must be in the same directory as the .mol2 file. Run the file by typing 'python sort_mol2_bonds.py input.mol2 output.mol2' in the terminal. This will run the script on the input.mol2 file and save the output as output.mol2 in the same directory.

**phosphate folder:** The phosphate folder contains example files created for the phosphate ion following the Ions In GROMACS Protocol. Note: pho_ini_fix.mol2 is the output file after running sort_mol2_bonds.py on pho_ini.mol2.
