#!/bin/sh


#  Path to Canu.

bin="/Users/pfb2024/PFB_problemsets/GenomeAssembly/canu-2.2/bin"

#  Report paths.

echo ""
echo "Found perl:"
echo "  " `which perl`
echo "  " `perl --version | grep version`
echo ""
echo "Found java:"
echo "  " `which java`
echo "  " `java -showversion 2>&1 | head -n 1`
echo ""
echo "Found canu:"
echo "  " $bin/canu
echo "  " `$bin/canu -version`
echo ""


#  Environment for any object storage.

export CANU_OBJECT_STORE_CLIENT=
export CANU_OBJECT_STORE_CLIENT_UA=
export CANU_OBJECT_STORE_CLIENT_DA=
export CANU_OBJECT_STORE_NAMESPACE=
export CANU_OBJECT_STORE_PROJECT=









#  Discover the job ID to run, from either a grid environment variable and a
#  command line offset, or directly from the command line.
#
if [ x$CANU_LOCAL_JOB_ID = x -o x$CANU_LOCAL_JOB_ID = xundefined -o x$CANU_LOCAL_JOB_ID = x0 ]; then
  baseid=$1
  offset=0
else
  baseid=$CANU_LOCAL_JOB_ID
  offset=$1
fi
if [ x$offset = x ]; then
  offset=0
fi
if [ x$baseid = x ]; then
  echo Error: I need CANU_LOCAL_JOB_ID set, or a job index on the command line.
  exit
fi
jobid=`expr -- $baseid + $offset`
if [ x$baseid = x0 ]; then
  echo Error: jobid 0 is invalid\; I need CANU_LOCAL_JOB_ID set, or a job index on the command line.
  exit
fi
if [ x$CANU_LOCAL_JOB_ID = x ]; then
  echo Running job $jobid based on command line options.
else
  echo Running job $jobid based on CANU_LOCAL_JOB_ID=$CANU_LOCAL_JOB_ID and offset=$offset.
fi

#  Check if the outputs exist.  If they do, just quit.  (The boilerplate
#  function for doing this fails if the file isn't strictly below the
#  current directory, so some gymnastics is needed.)

cd ..

if [ -e ecoli.ctgStore/seqDB.v001.tig ]; then
  exists=true
else
  exists=false
fi
cd 4-unitigger

if [ $exists = true ] ; then
  echo Unitigger outputs exist, stopping.
  exit 0
fi

$bin/bogart \
  -S ../../ecoli.seqStore \
  -O    ../ecoli.ovlStore \
  -o     ./ecoli \
  -gs 4800000 \
  -eg 0.045 \
  -eM 0.045 \
  -mo 500 \
  -covgapolap 500 \
  -covgaptype deadend \
  -lopsided 25  \
  -minolappercent   0.0  \
  -dg 12 \
  -db 1 \
  -dr 1 \
  -ca 2500 \
  -cp 15 \
  -threads 4 \
  -M 16 \
  -unassembled 2 0 1.0 0.5 3 \
> ./unitigger.err 2>&1

if [ 0 -ne 0 ] ; then
  echo Unitigger failed to complete successfully.
  exit 1
fi

#  Note that we have finished.  All the rest is optional; if
#  bogart is told to stop early, there won't be a ctgStore either.

touch ./unitigger.finished

if [ -e ./ecoli.ctgStore ] ; then
  mv ./ecoli.ctgStore ../ecoli.ctgStore
fi

#
#  Generate tig sizes here, so we can avoid another pull of
#  seqStore and ctgStore on cloud runs.  The output is generated
#  again if it is missing, so no damage done if it isn't made here.
#
if [ -e ../ecoli.ctgStore -a \
   ! -e ../ecoli.ctgStore/seqDB.v001.sizes.txt ] ; then
  $bin/tgStoreDump \
    -S ../../ecoli.seqStore \
    -T ../ecoli.ctgStore 1 \
    -sizes -s 4800000 \
   > ../ecoli.ctgStore/seqDB.v001.sizes.txt
fi

if [ -e ../ecoli.ctgStore ] ; then
  cd ../ecoli.ctgStore
  cd -
fi

exit 0
