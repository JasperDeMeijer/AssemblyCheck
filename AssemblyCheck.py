from Bio import SeqIO
import sys
import numpy

def main():
    scafLength = scaffoldLength()
    nFiftyScore = nFifty(scafLength)


def scaffoldLength():
    scafLength = []
    for record in SeqIO.parse("scaffolds.fasta", "fasta"):

        scafLength.append(len(record.seq))


    return scafLength

def nFifty(scafLength):
    scafLength.sort(reverse=True)
    sumScaf = 0
    for x in scafLength:
        sumScaf += x

    halfSumScaf = sumScaf/2

    nSum = 0
    nFiftyCheck = False

    for x in scafLength:
        nSum += x
        if nSum >= halfSumScaf:
            nFifty = x
            break

    return nFifty






main()
