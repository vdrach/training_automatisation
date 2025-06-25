#!/bin/bash

ROOTDIR=/users/vdrach/training_automatisation
SRCDIR=${ROOTDIR}/data_preprocessed
RUNDIR=${ROOTDIR}/rundir_parallel
HOMEDIR=$(pwd)

Nimg_per_job=64
Nimg=`ls ${SRCDIR}/*.jpg |wc -l | awk '{print $0}' `
for istart in `seq 1 ${Nimg_per_job} ${Nimg}`
    do
        mkdir  ${RUNDIR}/run$istart
        # generate sbatch file
        sed "s/jobname/job${istart}/g" job_template_parallel| sed "s/Nstart=1/Nstart=${istart}/g" >  ${RUNDIR}/run${istart}/job_${istart}

    #submit 
    #cd ${RUNDIR}/run${id}
    #sbatch job_${id}
    #cd
    #${HOMEDIR}

done    

