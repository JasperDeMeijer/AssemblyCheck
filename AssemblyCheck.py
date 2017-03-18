from Bio import SeqIO
import sys
import numpy

def main():
    scafLength = scaffoldLength()
    nFifty(scafLength)


def scaffoldLength():
    scafLength = []
    for record in SeqIO.parse("scaffolds.fasta", "fasta"):

        scafLength.append(len(record.seq))

    print(scafLength)
    return scafLength

def nFifty(scafLength):
    scafLength.sort()

main()
