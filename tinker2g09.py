#!/usr/bin/env python2

#Python Libraries 
import argparse, subprocess, sys, os, commands, string, math
from decimal import Decimal

parser = argparse.ArgumentParser()
parser.add_argument('-c', dest='charge',  help = 'define charge')
parser.add_argument('-m', help = 'define multiplicity')
parser.add_argument('-p', help = 'define number of processors')


# Input
#charge = raw_input("charge")
#multiplicity = raw_input("mult")
#proc = raw_input("proc")

# Read coordinates
coordinates = ""
file_name = sys.argv[1]
charge = sys.argv[2]
multiplicity =sys.argv[3] 
proc =sys.argv[4]

outputfile = file_name.split(".")[0] + "__output.txt"

with open(file_name, 'r') as f:
    _ = f.readline()  # header line
    for line in f:
        columns = line.split()
        at, x, y, z = columns[1:5]
        coordinates += "{} {} {} {}\n".format(at, x, y, z)

# Output
print """\
%mem=8GB
%nprocshared={proc}
%chk=1.chk
# opt freq M062X/6-311+G(2d,p)

 title

{charge} {multiplicity}
{coordinates}

--link1--
%mem=8GB
%nprocshared={proc}
%chk=1.chk
# geom=check guess=read M062X/6-311+G(2d,p)

 title

{charge} {multiplicity}
""".format(proc=proc, charge=charge,
           multiplicity=multiplicity,
           coordinates=coordinates)


