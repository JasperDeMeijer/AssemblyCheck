from Bio import SeqIO
import sys
import numpy

def main():
    records = scaffoldLength()
    nFiftyScore, nFiftyCount = nFifty(records)
    print(nFiftyScore, nFiftyCount)


def scaffoldLength():
    scafLength = []
    records =[]
    for record in SeqIO.parse("scaffolds.fasta", "fasta"):
        records.append(record)
        scafLength.append(len(record.seq))
    return records

def nFifty(records):
    scafLength = []
    for x in records:
        scafLength.append(len(x.seq))

    scafLength.sort(reverse=True)
    sumScaf = 0
    for x in scafLength:
        sumScaf += x

    halfSumScaf = sumScaf/2

    nSum = 0
    nFiftyCheck = False
    scaffCounter = 0
    for x in scafLength:
        scaffCounter += 1
        nSum += x
        if nSum >= halfSumScaf:
            nFifty = x
            nFiftyCount = scaffCounter
            break

    return nFifty, nFiftyCount

# def gapStats(records):
#
#     for y in records:
#         nCheck = False
#         gapCount = 0
#         gapSize = 0
#         for x in y.seq:
#             if x == "n":
#                 gapSize += 1
#                 while(nCheck == False):
#                     gapCount += 1
#                     nCheck = True
#             else:
#                 nCheck = False
#
#
#         gapCountList = []
#         averageGapSizeList = []








main()
