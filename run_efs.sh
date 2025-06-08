POT="Trained.mtp_"                   
if [[ ! -f $POT ]]; then
  echo "There is no potential $POT "; exit 1
fi


for cfg in *.cfg; do
  [[ $cfg == *_efs.cfg ]] && continue     
  out=${cfg%.cfg}_efs.cfg
  echo "> $out"
  mlp calc-efs "$POT" "$cfg" "$out" || { echo "  ! error on $cfg"; exit 1; }
done

echo "Ready: configurations e/f/s for $(ls *_efs.cfg | wc -l) structures are ready"
