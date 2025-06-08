import os, numpy as np
from pathlib import Path
from ase.io import read
from ase.units import Bohr

REF_OUTCAR = "OUTCAR_ref"
OUT_DIR    = "deformed_cfg"
EPS_MIN, EPS_MAX, STEP = -0.03, 0.03, 0.005
DIRS = ["xx", "yy", "zz"]          


Path(OUT_DIR).mkdir(exist_ok=True)
atoms0 = read(REF_OUTCAR, format="vasp-out")
num    = len(atoms0)
types  = atoms0.get_chemical_symbols()

type_map = {'C': 0, 'Al': 1} 

def write_mlip_cfg(path, at):
    cell = at.get_cell()
    xyz  = at.get_positions()
    with open(path, "w") as f:
        f.write("BEGIN_CFG\n")
        f.write(f" Size\n    {len(at)}\n")
        f.write(" Supercell\n")
        for v in cell:
            f.write(f"    {v[0]:20.14f} {v[1]:20.14f} {v[2]:20.14f}\n")
        f.write(" AtomData:  id type cartes_x cartes_y cartes_z\n")
        for i, (sym, r) in enumerate(zip(at.get_chemical_symbols(), xyz), 1):
            t = type_map[sym]              
            f.write(f"    {i} {t} {r[0]:20.14f} {r[1]:20.14f} {r[2]:20.14f}\n")
        f.write(" PlusStress:  0.0 0.0 0.0 0.0 0.0 0.0\n")
        f.write("END_CFG\n")

eps_arr = np.arange(EPS_MIN, EPS_MAX + STEP/2, STEP)
for tag in DIRS:
    axis = "xyz".index(tag[0])          
    for eps in eps_arr:
        at = atoms0.copy()
        M  = np.eye(3);  M[axis,axis] += eps
        at.set_cell(atoms0.get_cell() @ M, scale_atoms=True)

        perc = f"{eps*100:+.1f}".rstrip('0').rstrip('.')
        cfg  = Path(OUT_DIR, f"{tag}_{perc}.cfg")
        write_mlip_cfg(cfg, at)

print(f"  {len(eps_arr)*len(DIRS)} all configurations saved into '{OUT_DIR}'")
