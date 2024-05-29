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
# takes a string, returns a list of all permutations of the string.

from itertools import permutations

def permute(input: str) -> list:
    return list("".join(perm) for perm in permutations(input))

# takes a string, returns a list of all vowel clusters in the string.
def getListOfVowelClusters(input: str) -> list:
    vowels = "aeiouAEIOU"
    vowel_clusters = []
    current_cluster = ""
    for letter in input:
        if letter in vowels:
            current_cluster += letter
        else:
            if current_cluster != "":
                vowel_clusters.append(current_cluster)
                current_cluster = ""
    if current_cluster != "":
        vowel_clusters.append(current_cluster)
    return vowel_clusters
# takes a list of vowel clusters, returns the "Happiest score" and the corresponding vowel cluster in dictionary {"<vowel_cluster": <happiest_score>}. "Happiness score" is the sum of all ASCII values of characters in vowel cluster. You can use built-in ord() to convert a char to ascii value.  "Happiness score" can be "Happy number" or not. "Happy number" is a prime number, and the sum of its digits is a power of base 2. "Happiest number" is the "Happy number" with the largest sum of digits. If there is more than one "Happy number" with the largest sum of digits, the "Happiest number" will be the largest number. If there is no "Happy number", the "Happiest number" is 0.

def findHappinestNumber(input):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def is_happy(num):
        def square_sum(num):
            return sum(int(i) ** 2 for i in str(num))
        
        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            num = square_sum(num)
        return num == 1
        
    def is_happiest(num):
        def digit_sum(num):
            return sum(int(i) for i in str(num))
        
        if is_happy(num):
            return digit_sum(num)
        return 0
    
    happiest = 0
    result = {}
    for cluster in input:
        score = sum(ord(c) for c in cluster)
        if is_happiest(score) > happiest:
            happiest = is_happiest(score)
            result = {cluster: score}
        elif is_happiest(score) == happiest and is_prime(score):
            happiest = is_happiest(score)
            result[cluster] = score
    return result

# take a list of permutations of the string, returns the largest "Happiest score" and the corresponding vowel cluster in dictionary {"<vowel_cluster": <largest_happiest_score>}.

from typing import Dict, List

def calculateLargestHappiestScore(input: List[str]) -> Dict[str, int]:
    vowel_clusters = []
    for string in input:
        vowel_clusters += getListOfVowelClusters(string)
    happiest_dict = findHappinestNumber(vowel_clusters)
    return happiest_dict

# takes a string, rearranges the string's characters to get the highest "Happiest score" and return output string in format: "Happiest String: <happiest_string> - Happiest Score: <happiness_score> (<status>)" (Does not include "). In which <happiest_string> is a vowel cluster arranged in ascending order according to the ASCII code corresponding to the Happiest score found; <happiness_score> is a non-negative integer; <status> is "Happy" or "Unhappy". You have the right to transpose all characters in the string. A permutation would be equivalent to an array of "Happiness scores". The "Happiness score" in this sentence is calculated as the sum of the ASCII codes of adjacent vowels (a, e, i, o, u, A, E, I, O, U) (vowel clusters). For example, "aebcdef" will be equivalent to a two-element array of "Happiness scores" corresponding to "ae" and "e". "Happiness score" can be "Happy number" or not. "Happy number" is a prime number and the sum of its digits is a power of base 2. "Happiest score" must be a "Happy number" and have the greatest sum of digits. If there is more than one "Happy number" with the largest sum of digits, the "Happiest number" will be the largest number. For each permutation of the string there will be a corresponding "Happiest score". You need to find the largest "Happiest score" and the vowel cluster corresponding to this number across all permutations of the string. If there are no vowels in the input string, the largest "Happiest score" is 0. In case there is more than one "Happiest score" with the same value, the vowel cluster has a shorter length and has more vowels (For example: "aia" has 2 vowels, 'a' and 'i') will prioritized. In the case of the same "Happiest score", the same length and number of vowels in the vowel cluster, the different first character of the vowel cluster with the larger ASCII code will be chosen.
from typing import List, Tuple

def is_happy(num: int) -> bool:
    def digit_sum(num: int) -> int:
        return sum(int(i) for i in str(num))
    
    def is_power_of_two(num: int) -> bool:
        return num != 0 and (num & (num - 1)) == 0
    
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return is_prime(num) and is_power_of_two(digit_sum(num))

def maximizeHappiestScore(input: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    permutations = permute(input)
    happiest_score = 0
    happiest_string = ""
    for perm in permutations:
        vowel_clusters = []
        vowel_cluster = ""
        for char in perm:
            if char in vowels:
                vowel_cluster += char
            else:
                if vowel_cluster != "":
                    vowel_clusters.append(vowel_cluster)
                    vowel_cluster = ""
        if vowel_cluster != "":
            vowel_clusters.append(vowel_cluster)
        happiness_scores = []
        for cluster in vowel_clusters:
            score = sum(ord(char) for char in cluster)
            if is_happy(score):
                happiness_scores.append(score)
        if happiness_scores:
            largest_happiness_score = max(happiness_scores)
            if largest_happiness_score > happiest_score:
                happiest_score = largest_happiness_score
                happiest_string = sorted([cluster for cluster in vowel_clusters if sum(ord(char) for char in cluster) == happiest_score], key=lambda x: (-len(x), -ord(x[0])))[-1]
    if happiest_score == 0:
        return "Happiest String:  - Happiest Score: 0 (Unhappy)"
    else:
        return f"Happiest String: {''.join(sorted(happiest_string))} - Happiest Score: {happiest_score} (Happy)"

assert repr(str(maximizeHappiestScore("aeiou "))) == repr(str("Happiest String: e - Happiest Score: 101 (Happy)")) or (maximizeHappiestScore("aeiou ") == "Happiest String: e - Happiest Score: 101 (Happy)")
assert repr(str(maximizeHappiestScore("a e"))) == repr(str("Happiest String: e - Happiest Score: 101 (Happy)")) or (maximizeHappiestScore("a e") == "Happiest String: e - Happiest Score: 101 (Happy)")

assert repr(str(permute("abc"))) == repr(str(["abc", "acb", "bac", "bca", "cab", "cba"])) or (permute("abc") == ["abc", "acb", "bac", "bca", "cab", "cba"])

assert repr(str(calculateLargestHappiestScore(["abc", "acb", "bac", "bca", "cab", "cba"]))) == repr(str({"a": 97})) or (calculateLargestHappiestScore(["abc", "acb", "bac", "bca", "cab", "cba"]) == {"a": 97})
assert repr(str(calculateLargestHappiestScore(["aeiou"]))) == repr(str({})) or (calculateLargestHappiestScore(["aeiou"]) == {})

assert repr(str(getListOfVowelClusters("abcde"))) == repr(str(["a", "e"])) or (getListOfVowelClusters("abcde") == ["a", "e"])
assert repr(str(getListOfVowelClusters("aeiou"))) == repr(str(["aeiou"])) or (getListOfVowelClusters("aeiou") == ["aeiou"])

assert repr(str(findHappinestNumber(["a", "e"]))) == repr(str({'a': 97})) or (findHappinestNumber(["a", "e"]) == {'a': 97})
assert repr(str(findHappinestNumber(["aeiou"]))) == repr(str({})) or (findHappinestNumber(["aeiou"]) == {})
