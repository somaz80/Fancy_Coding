#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    dict_schoc = {}
    temp_eml = None
    even_soc = 0
    for i in range(n):
        temp_eml = ar[i]
        if temp_eml in dict_schoc:
            dict_schoc[temp_eml] = dict_schoc[temp_eml] + 1
        else:
            dict_schoc[temp_eml] = 1

    for key, value in dict_schoc.items():
        if value >= 2:
            even_soc += value//2
    return even_soc

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
