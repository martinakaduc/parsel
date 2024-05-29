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
# calculate the "Happiness score" of a given string. Happiness score is the sum of the ASCII codes of all vowels (a, e, i, o, u, A, E, I, O, U) in the string. The function will print the happiness score and a message indicating whether the score is "Happy" (score > 100) or "Unhappy" (score <= 100). Format of output: "Happiness Score: <happiness_score> (<status>)". (Do not include "). In which <happiness_score> is a non-negative integer; <status> is "Happy" or "Unhappy".

def calculateHappinessScore(input: str) -> str:
    vowels = "aeiouAEIOU"
    score = 0
    for char in input:
        if char in vowels:
            score += ord(char)
    status = "Happy" if score > 100 else "Unhappy"
    return f"Happiness Score: {score} ({status})"


assert repr(str(calculateHappinessScore("Hello, World!"))) == repr(str("Happiness Score: 323 (Happy)")) or (calculateHappinessScore("Hello, World!") == "Happiness Score: 323 (Happy)")
assert repr(str(calculateHappinessScore("Sad"))) == repr(str("Happiness Score: 97 (Unhappy)")) or (calculateHappinessScore("Sad") == "Happiness Score: 97 (Unhappy)")
