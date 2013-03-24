import wave
from numpy import *
from pylab import *
from scipy import *

trainset = []
testset = []

noSplits = 500

def calcDHash(w):
    splits = []
    for i in range(noSplits):
	splits.append(len(w)/noSplits + i*len(w)/noSplits)
    sums = []
    for i in range(noSplits-1):
	sums.append(sum(w[splits[i]:splits[i+1]]))
    bits = []
    for i in range(noSplits-2):
	if sums[i] < sums[i+1]:
		bits.append(1)
	else:
		bits.append(0)
    if sums[noSplits-2] < sums[0]:
	bits.append(1)
    else:
	bits.append(0)
    return bits

for i in range(10):
    wr = wave.open("D:\\aai\\train\\" + str(i) + ".wav")
    trainset.append(calcDHash(map(ord, wr.readframes(wr.getnframes()))))

for i in range(10):
    wr = wave.open("D:\\aai\\test\\" + str(i) + ".wav")
    testset.append(calcDHash(map(ord, wr.readframes(wr.getnframes()))))

def getBest(num):
    diff = []
    for i in range(10):
        d = 0
        for j in range(len(trainset[num])):
            if trainset[num][j] <> testset[i][j]:
                d += 1
        diff.append(d)

    print diff
    print str(num) + " : " + str(argmin(diff)) + " => " + str(min(diff))
    print ""

for i in range(10):
    getBest(i)
    
