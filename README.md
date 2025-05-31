# Diamane

1st step:
  Convert all OUTCARs into cfg. files: put in all OUTCARs into one folder and in the same folder add 'bulk_outcar2cfg.py' script
  Run script to convert all files into cfg. format. Also this script joins all cfg. files into one single cfg. file called 'all_dft.cfg'

2nd step:
  Calculate minimal distance between atoms using command:
mlp mindist all_dft.cfg
After calculations you'll get: Global mindist: 1.26571
Add this info into '06.mtp' file

3rd step:
  We need to break down 'all_dft.cfg' into train/test parts and shuffle all files. It could be done using 'train_test_shuffle.sh' script. To activate the script use command:
  chmod +x train_test_shuffle.sh
  and then: 
  ./train_test_shuffle.sh
  



