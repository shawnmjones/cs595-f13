#!/bin/bash

# if anything fails, QUIT ASAP!
set -e

input=$1
listfile=$2
workingdir=$3

echo "Removing ${listfile}"
if [ -f "${listfile}" ]; then
    rm "${listfile}"
fi

echo "Cleaning out ${workingdir}"
if [ -d "${workingdir}" ]; then
    rm -rf "${workingdir}"
fi

mkdir -p "${workingdir}"

for line in `cat ${input}`; do
    sha=`echo "${line}" | shasum | awk '{ print $1 }'`
    echo "working on ${line}, now ${sha}"
    echo "${line}    ${sha}" >> ${listfile}

    outfileraw="${sha}.raw"
    curl -A "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)" "${line}" >> "${workingdir}/${outfileraw}"

    outfileproc="${sha}.processed"
    lynx -dump -force_html "${workingdir}/${outfileraw}" >> "${workingdir}/${outfileproc}"
    sleep 1
done

echo "finished"
