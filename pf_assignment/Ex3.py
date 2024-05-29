import sys
import time
import itertools
from itertools import accumulate, product, permutations, combinations
import collections
from collections import Counter, OrderedDict, deque, defaultdict, ChainMap
from functools import lru_cache
import math
from math import sqrt, sin, cos, tan, ceil, fabs, floor, gcd, exp, log, log2
import fractions
from typing import List, Tuple
import numpy as np
import random
import heapq
# Takes a string consisting of non-negative integers separated by commas as input. The function will then find and return the "Happiest number" in the string. "Happy number" is a prime number, and the sum of its digits is a power of base 2. "Happiest number" is the "Happy number" with the largest sum of digits. If there is more than one "Happy number" with the largest sum of digits, the "Happiest number" will be the largest number. If there is no "Happy number", the "Happiest number" is 0.
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def is_happy(num: int) -> bool:
    def sum_of_squares(n: int) -> int:
        return sum(int(i)**2 for i in str(n))
    
    seen = set()
    while True:
        num = sum_of_squares(num)
        if num == 1:
            return True
        if num in seen:
            return False
        seen.add(num)

def findHappinestNumber(input: str) -> int:
    nums = [int(num) for num in input.split(",")]
    happiest_num = 0
    happiest_num_sum = 0
    for num in nums:
        if is_prime(num) and (sum(int(i) for i in str(num)) in [2**n for n in range(1,11)]):
            if sum(int(i) for i in str(num)) > happiest_num_sum:
                happiest_num = num
                happiest_num_sum = sum(int(i) for i in str(num))
    return happiest_num

assert repr(str(findHappinestNumber("13,89,53,45,67"))) == repr(str(53)) or (findHappinestNumber("13,89,53,45,67") == 53)
assert repr(str(findHappinestNumber("0,1,243,6434,96232,0"))) == repr(str(0)) or (findHappinestNumber("0,1,243,6434,96232,0") == 0)
