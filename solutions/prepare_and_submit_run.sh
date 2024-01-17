#!/bin/bash
SRCDIR=./data_preprocessed
RUNDIR=./rundir
HOMEDIR=$(pwd)

# loop over all SRC
for f in ${SRCDIR}/?_*.jpg # to process only the first 10 images... and let the other user have a chance to use the machine !
    do
        f=`basename ${f}` 

        TMP=`basename  ${f} .jpg`
        id=`echo ${TMP} | cut -d'_' -f1`
        N=`echo ${TMP} | cut -d'_' -f2`
        M=`echo ${TMP} | cut -d'_' -f3`
        
        mkdir ${RUNDIR}/run${id}

        # generate sbatch file
        sed "s/jobname/job${id}/g" job_template   | sed "s/1_1024_429.jpg/${f}/g" > ${RUNDIR}/run${id}/job_${id}

        #submit 
        cd ${RUNDIR}/run${id}
        sbatch job_${id}
        cd ${HOMEDIR}
    done  



# submit

