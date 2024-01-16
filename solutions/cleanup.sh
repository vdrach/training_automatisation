#!/bin/bash


for f in  *.jpg
    do
        MD5=`md5sum "${f}" |awk '{print $1}'`
        #echo $MD5,$f
        x=`grep "${MD5}"  log_checksum | wc -l`
        if (( ${x} == 0 )); then
            rm  -v "${f}"
        fi

    done
