'''
Week - 2
DAY 1 QUESTION 2 
FIRST UNIQUE CHARACTER IN A STING 
'''
from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):

        count = Counter(s)
        for i in range(len(s)):

            if count[s[i]] == 1 :
                return i 

        return -1
       
