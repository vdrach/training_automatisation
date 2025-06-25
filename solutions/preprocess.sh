SRCDIR=${HOME}/training_automatisation
DATADIR=${HOME}/training_automatisation/data
OUTDIR=${HOME}/training_automatisation/data_preprocessed

mkdir -p ${OUTDIR}

COUNTER=0
for f  in ${DATADIR}/*.jpg
    do
    COUNTER=$(( COUNTER + 1 ))
    STR=`python ${SRCDIR}/solutions/get_N_M.py "${f}"` 
    
    cp -v "$f"  ${OUTDIR}/${COUNTER}_${STR}.jpg

    done
