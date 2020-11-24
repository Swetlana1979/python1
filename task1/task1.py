import argparse
parser = argparse.ArgumentParser(description='A tutorial of argparse!')
parser.add_argument("--file",default="task1.txt")
args = parser.parse_args()
file = args.file
import numpy as np
#import matplotlib.pyplot as plt



#array1 = [1, 2, 5, 7, 8,10,-54,9,258,42,6] 
def nlogn_median(a):
    a = sorted(a)
    if len(a) % 2 == 1:
        m=a [int(len(a)/2)+1]
        return m
    else:
        return 0.5*(a[len(a)/2 - 1] + a[len(a)/2])

def arraySum(a):
    theSum = 0
    for i in a:
        theSum = theSum + i
    return theSum

def average(a):
    theSum = 0
    for i in a:
        theSum = theSum + i
    length=len(a)
    return round(theSum/length)
	
def main(file):
	f = open(file)
	a = f.readline()
	while line:
		a = f.readline()
	f.close()
	print("минимум -",min(a),"максимум -",max(a))
	median=nlogn_median(a)
	print("медиана - ",median)
	ave=average(a)
	print(ave)
	percentile=np.percentile(a, 90)
	print(percentile)
main(array1)
 