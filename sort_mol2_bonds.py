"""
@author: Evan Yip

"""
# sort_mol2_bonds.pl - a script to reorder the listing in a .mol2 @<TRIPOS>BOND
# section so that the following conventions are preserved:
#   1. Atoms on each line are in increasing order (e.g. 1 2 not 2 1)
#   2. The bonds appear in order of ascending atom number
#   3. For bonds involving the same atom in the first position, the bonds appear
#       in order of ascending second atom
# Script requires 1 input
# e.g. Usage: python sort_mol2_bonds.py input.mol2 output.mol2

import sys
import argparse
import os

def check_file_types(input, output):
    """
    Tests to see that the input files are in mol2 format
    """

def file_choices(choices,fname, file_type):
    ext = os.path.splitext(fname)[1][1:]
    if ext not in choices:  # If file output/input file doesnt end with allowed types, error
       parser.error("{file} file doesn't end with one of {type}"\
                    .format(file = file_type, type = choices))
    return fname
    

def main():
    # Parsing the arguments
    global parser
    parser = argparse.ArgumentParser()
    parser.add_argument('input',help="Input mol2 file name", type=lambda s:file_choices(("mol2"),s, "Input"))
    parser.add_argument('output',help="Desired output mol2 filename", type=lambda s:file_choices(("mol2"),s, "Output"))

    args = parser.parse_args()
    print(args.input, args.output)

    # opening file
    with open(args.input) as f1, open(args.output, 'w') as f2:
        lines = f1.readlines()
        print(lines)


if __name__ == "__main__":
    main()
