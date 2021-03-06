from Bio import SeqIO
import sys
import numpy

def main():
    records = scaffoldLength()
    nFiftyScore, nFiftyCount = nFifty(records)
    print(nFiftyScore, nFiftyCount)
    gapStats(records)


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

def gapStats(records):
    gapCountList = []
    averageGapSizeList = []
    scaffoldGapCountList = []

    sCheck = True
    nCheck = False
    gapCount = 0
    gapSize = 0

    for y in records:
        scaffoldGapCount = 0

        for x in y.seq:

            if x == "n":
                sCheck = False
                gapSize = gapSize + 1
                while(nCheck == False):
                    scaffoldGapCount = scaffoldGapCount + 1
                    gapCount = gapCount + 1
                    nCheck = True
            else:
                while(sCheck == False):
                    averageGapSizeList.append(gapSize)
                    sCheck = True
                gapSize = 0

                nCheck = False

        scaffoldGapCountList.append(scaffoldGapCount)


    print(averageGapSizeList)
    print(len(averageGapSizeList))
    print(gapCount)
    averageGapSize = sum(averageGapSizeList)/len(averageGapSizeList)
    print(averageGapSize)
    print(scaffoldGapCountList)
    print(len(scaffoldGapCountList))













main()
