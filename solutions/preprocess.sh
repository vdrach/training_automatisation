SRCDIR=/home/${USER}/HPC_training/training_automatisation/data
OUTDIR=/home/${USER}/HPC_training/training_automatisation/data_preprocessed

mkdir -p ${OUTDIR}

COUNTER=0
for f  in ${SRCDIR}/*.jpg
    do
    COUNTER=$(( COUNTER + 1 ))
    STR=`python /home/${USER}/HPC_training/training_automatisation/get_N_M.py "${f}"` 
    
    cp -v "$f"  ${OUTDIR}/${COUNTER}_${STR}.jpg

    done
