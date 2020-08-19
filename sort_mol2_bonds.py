"""
@author: Evan Yip
8/18/2020
GEMSEC lab

"""
# sort_mol2_bonds.pl - a script to reorder the listing in a .mol2 @<TRIPOS>BOND
# section so that the following conventions are preserved:
#   1. Atoms on each line are in increasing order (e.g. 1 2 not 2 1)
#   2. The bonds appear in order of ascending atom number
#   3. For bonds involving the same atom in the first position, the bonds
#      appear in order of ascending second atom
# Script requires 1 input
# e.g. Usage: python sort_mol2_bonds.py input.mol2 output.mol2

import argparse
import os
import numpy as np


def check_file_types(input, output):
    """
    Tests to see that the input files are in mol2 format
    """


def file_choices(choices, fname, file_type):
    ext = os.path.splitext(fname)[1][1:]
    # If file output/input file doesnt end with allowed types, error
    if ext not in choices:
        parser.error("{file} file doesn't end with one of {type}"
                     .format(file=file_type, type=choices))
    return fname


def reorder_bond(array):
    """
    Takes in 2D np array of dimension (1, x)
    and reorders the atom numbers to be in ascending order
    e.g. [1   3   1   1] --> [1  1  3  1] where positions 1 and 2
    are swapped.
    """
    # atoms
    a1 = array[0, 1]
    a2 = array[0, 2]
    if a1 > a2:
        array[0, 1] = a2
        array[0, 2] = a1
    return array


def main():
    """
    Reorders the bonds in the mol2 file and writes them to
    desired output file.
    """
    # Parsing the arguments
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help="Input mol2 file name",
                        type=lambda s: file_choices(("mol2"), s, "Input"))
    parser.add_argument('output', help="Desired output mol2 filename",
                        type=lambda s: file_choices(("mol2"), s, "Output"))

    args = parser.parse_args()
    # print(args.input, args.output)

    # opening file
    with open(args.input) as f1, open(args.output, 'w') as f2:
        lines = f1.readlines()
        # Test for header lines that some scripts produce
        assert "TRIPOS" in lines[0],\
            "Nonstandard header found: " + lines[0].strip()\
            + ". Please delete header lines until\
             the TRIPOS molecule definition."

        # Get number of atoms and number of bonds from mol2 file
        struct = lines[2].split()
        natom = int(struct[0])
        nbond = int(struct[1])

        # Atom and bond check
        print("Found", natom, "atoms in the molecule with", nbond, "bonds.")
        print("Writing output to:", args.output)
        print("-----------------File Output--------------------")
        # Print out everything until the bond section
        i = 0
        while "BOND" not in lines[i]:
            print(lines[i])
            f2.write(lines[i])
            i += 1
        print(lines[i])  # Print out the BOND section header line
        f2.write(lines[i])
        i += 1

        # sort the bonds - e.g. the one that has the lowest atom number
        # in the first position and then the lowest atom number
        # in the second position (swap if necessary)
        for j in range(0, nbond):
            if j == 0:
                # Converting string to np array
                bonds = np.fromstring(lines[i + j], dtype=int, sep=" ")
                bonds = np.reshape(bonds, (1, -1))  # reshaping to 2D np array
                bonds = reorder_bond(bonds)  # reorders atoms within each bond
            else:
                bond = np.fromstring(lines[i + j], dtype=int, sep=" ")
                bond = np.reshape(bond, (1, -1))
                bond = reorder_bond(bond)  # reorders atoms within each bond
                bonds = np.append(bonds, bond, axis=0)
            final = bonds[bonds[:, 2].argsort()]  # sort rows by 2nd atom pos.
            final = final[final[:, 1].argsort()]  # sort rows by 1st atom pos.

        # Reindexing the numpy array first column
        for k in range(0, nbond):
            # print("k:", k)
            final[k, 0] = k + 1
            for l in range(0, len(final[k])):
                # print("l:", l)
                print("    ", str(final[k, l]), end='')
                f2.write("     " + str(final[k, l]))
            print("")
            f2.write("\n")


if __name__ == "__main__":
    main()
