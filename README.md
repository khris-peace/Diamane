# Diamane

1st step:
  Convert all OUTCARs into cfg. files: put in all OUTCARs into one folder and in the same folder add 'bulk_outcar2cfg.py' script
  
  Run script to convert all files into cfg. format. Also this script joins all cfg. files into one single cfg. file called 'all_dft.cfg'

2nd step:
  Calculate minimal distance between atoms using command:
  
mlp mindist all_dft.cfg

After calculations you'll get: Global mindist: 1.26571 (for instance)

Add this info into '06.mtp' file

3rd step:
  We need to break down 'all_dft.cfg' into train/test parts and shuffle all files. It could be done using
  
  'train_test_shuffle.sh' script. To activate the script use command:
  
  chmod +x train_test_shuffle.sh
  
  and then: 
  
  ./train_test_shuffle.sh

In the end you'll get two files: "train.cfg" and "test.cfg"

4th step:
  Let's train potential, using command:
  
  mlp train 06.mtp train.cfg — trained-pot-name=$TMP_DIR/pot.mtp —max-iter=100

  //We can use tmux to run potential "offline": tmux new -s <session_name>, <session_name> is the name of the session//

  After we run a command to train potential in several hours we'll get a a file "Trained.mtp_"

5th step: (make strained structures)

  Create a folder named "Elastic_constant" and put into it script "m_s_new_new.py" and "OUTCAR_ref" and "OUTCAR_ref.cfg" files.

  To run a script "m_s_new_new.py", activate it first:

  chmod +x m_s_new_new.py

  and then:

  python3 m_s_new_new.py

  This script will give strained sctructures with 0-3% and 0.5% steps.

6th step: (calculate the energy of the strained structures)

  In the folder "Elastic constant" you'll get a folder "deformed_cfg" with all strained structures. Copy to this folder "Trained.mtp_" potential (which we got in 4th step) and a script "run_efs.sh". To activate the script use command:
  
  chmod +x run_efs.sh
  
  and then: 
  
  ./run_efs.sh

  After this command you'll get recalculated structures where you can find a value of energy of every structure.



