'''
WEEK - 2 
DAY 3 QUESTION 3 
REPEATED SUBSTRING PATTERN
'''
class Solution(object):
    def repeatedSubstringPattern(self, s):
        return s in (s+s)[1:-1]
       
        