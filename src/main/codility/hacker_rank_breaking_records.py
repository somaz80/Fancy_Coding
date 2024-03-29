#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    max_val = scores[0]
    min_val = scores[0]
    max_count = 0
    min_count = 0
    for i  in scores:
        if i > max_val :
            max_count = max_count +  1
            max_val = i
        if i < min_val:
            min_count = min_count + 1
            min_val = i
    return [max_count, min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
