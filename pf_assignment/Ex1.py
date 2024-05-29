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
# Takes a string then returns that string with the string "Happy " at the beginning of it.
def makeHappiness(input: str) -> str:
    return "Happy " + input

assert repr(str(makeHappiness("Tiger"))) == repr(str("Happy Tiger")) or (makeHappiness("Tiger") == "Happy Tiger")
assert repr(str(makeHappiness("Hi"))) == repr(str("Happy Hi")) or (makeHappiness("Hi") == "Happy Hi")
