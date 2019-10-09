#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b


def lcm(a, b):
    return a * b // gcd(a, b)


def getTotalX(a, b):
    # Write your code here
    lcm_num = a[0]
    gcd_num = b[0]
    if len(a) > 1:
        for x in range(1,len(a)):
            lcm_num =  (lcm_num * a[x])/gcd(lcm_num,a[x])
    if len(b) > 1:
        for x in range(1,len(b)):
            gcd_num = gcd(gcd_num,b[x])
    count = 0
    for x in range(int(lcm_num), int(gcd_num+1), int(lcm_num)):
        if gcd(x, gcd_num) == x:
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
