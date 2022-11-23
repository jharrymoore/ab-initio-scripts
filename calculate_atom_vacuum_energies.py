from copy import deepcopy
import os
import sys
from xtb.ase.calculator import XTB
from ase.io.extxyz import write_extxyz, read_extxyz
from ase.calculators.orca import ORCA
from ase import Atoms


def main():
    elements = ["H","C", "N", "O", "F", "S", "Cl", "Br"]
    atoms = [Atoms(elem, positions=[(0,0,0)]) for elem in elements]
    mults = [2,1,2,1,2,1,2, 2]
    outputs = {}
    # read an input structure file, run xtb md calculation
    # os.environ["ASE_ORCA_COMMAND"] = "/home/jhm72/orca_5.0.0/orca PREFIX.inp > PREFIX.out"
    # read xyz file to atoms
    # atoms = ase.io.read(file)
    for a, m, elem in zip(atoms, mults, elements):
        calc = ORCA(orcasimpleinput="TightSCF wB97X def2-TZVPPD", mult=m, orcablock="NPROCS 16")
    
        a.calc = calc
        a.info["config_type"] = "IsolatedAtom"




        # a.calc = XTB(method="GFN2-xTB", mult=m)
        e = a.get_potential_energy()

        print(e)
        outputs[elem] = e

    with open("iso_atoms_wb97.xyz", 'w') as f:
        for a in atoms:
            
            write_extxyz(f,a, append=True)

    print(outputs)

    # run MD 


if __name__ == "__main__":
    main()
