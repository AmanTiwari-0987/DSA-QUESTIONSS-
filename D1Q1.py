'''
Week - 2
DAY 1 QUESTION 1 
VALID ANAGRAM
'''
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        count1 = Counter(s)
        count2 = Counter(t)

        if (count1 == count2):
            return True

        return False