mlp convert-cfg all_dft.cfg tmp.cfg --shuffle         


N=$(grep -c '^BEGIN_CFG' tmp.cfg)   
Ntrain=$(( N*8/10 ))                


awk -v ntrain="$Ntrain" '
  BEGIN{cfg=0}
/^BEGIN_CFG/{cfg++}
{ if (cfg<=ntrain) print > "train.cfg";
  else             print > "test.cfg" }
' tmp.cfg

rm tmp.cfg