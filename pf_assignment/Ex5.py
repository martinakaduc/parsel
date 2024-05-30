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
# Given an array of members and a standard "Happiness level", write a function to group members into as many groups as possible so that the group's "Happiness level" is greater than or equal to the standard "Happiness level" (meets standard). A group has at least 1 member. Know that the "Happiness level" of a group will be the sum of the "Happiness level" of the members in that group. There may exist a group whose "Happiness level" is less than the standard "Happiness level". After grouping, the names of members of groups with a qualified "Happiness level" will be added with the phrase "Happy " at the beginning of the name. For example, "Andy" will become "Happy Andy". The result of this function will be an array containing only groups satisfying "Happiness level" standards, regardless of order. If there is no member, the function returns None. Given the Group and Member classes as below. class Group: def __init__(self, members, happinessLevel): self.members = members self.numMembers = len(members) self.happinessLevel = happinessLevel  def __repr__(self): return "Group(" + str(self.members) + ", " + str(self.happinessLevel) + ")"    class Member: def __init__(self, name, happinessLevel): self.name = name self.happinessLevel = happinessLevel  def __repr__(self): return "Member(\"" + self.name + "\", " + str(self.happinessLevel) + ")"
class Group: 
    def __init__(self, members, happinessLevel): 
        self.members = members 
        self.numMembers = len(members) 
        self.happinessLevel = happinessLevel  
    def __repr__(self): 
        return "Group(" + str(self.members) + ", " + str(self.happinessLevel) + ")"    
        
class Member: 
    def __init__(self, name, happinessLevel): 
        self.name = name 
        self.happinessLevel = happinessLevel 
    def __repr__(self): 
        return "Member(\"" + self.name + "\", " + str(self.happinessLevel) + ")"

def splitGroups(members: List[Member], numMembers: int, standardLevel: int) -> List[Group]:
    if numMembers == 0:
        return None
    
    def backtrack(start, currGroup):
        nonlocal res
        if currGroup.happinessLevel >= standardLevel:
            res.append(currGroup)
        for i in range(start, numMembers):
            newGroup = Group(currGroup.members + [members[i]], currGroup.happinessLevel + members[i].happinessLevel)
            backtrack(i + 1, newGroup)
    
    res = []
    backtrack(0, Group([], 0))
    for group in res:
        for i in range(len(group.members)):
            group.members[i].name = "Happy " + group.members[i].name
    return res

assert repr(str(splitGroups([Member("Andy", 5)], 1, 6))) == repr(str([])) or (splitGroups([Member("Andy", 5)], 1, 6) == [])
assert repr(str(splitGroups([Member("Bob", 7)], 1, 6))) == repr(str([Group([Member("Happy Bob", 7)], 7)])) or (splitGroups([Member("Bob", 7)], 1, 6) == [Group([Member("Happy Bob", 7)], 7)])
