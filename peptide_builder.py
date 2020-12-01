
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 17:52:04 2020
@author: evan
Generating a pdb structure file using
peptide sequence.
*NOTE: hydrogens are not present in the
structure and must be added via Chimera or
in GROMACS via pdb2gmx
"""

# from PeptideBuilder import Geometry
import PeptideBuilder
import Bio.PDB

# Set the desired peptide sequence
pep_sequence = "SYEKSHSQAINTDRT"
file_name = "sADP5.pdb"

# Making the extended structure
structure = PeptideBuilder.make_extended_structure(pep_sequence)

# add terminal oxygen (OXT) to the final residue in the structure
PeptideBuilder.add_terminal_OXT(structure)

# Initializing output object
out = Bio.PDB.PDBIO()
# Making pdb structure
out.set_structure(structure)

# Saving pdb file
out.save(file_name)