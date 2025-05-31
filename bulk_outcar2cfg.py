import glob, subprocess as sp, os, sys
from pathlib import Path

outcars = sorted(glob.glob("OUTCAR*"))       
if not outcars:
    sys.exit("There is no any OUTCAR*")

print(f"I found {len(outcars)} OUTCAR-files")


cfg_files = []
for f in outcars:
    cfg = Path(f).with_suffix(".cfg")         
    print(f"  > {cfg.name}")
    sp.run(
        ["mlp", "convert-cfg", f, cfg,
         "--input-format=vasp-outcar", "--output-format=txt"],
        check=True
    )
    cfg_files.append(cfg)


out = Path("all_dft.cfg")
with open(out, "w") as fout:
    for i, cfg in enumerate(cfg_files):
        with open(cfg) as fin:
            txt = fin.read().rstrip()         
        if i:                                 
            fout.write("\n")                  
        fout.write(txt+"\n")

print(f"All cfg are joint  {out.resolve()}")
