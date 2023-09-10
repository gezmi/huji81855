#!/bin/csh

set pdb=$1
set model=$2

cat $pdb | awk 'BEGIN{f=0}{if (f==1 && $1=="ATOM") print $0; if ($1=="MODEL" && $2=='$model') f=1; if (f==1 && $1=="ENDMDL") f=0}'

