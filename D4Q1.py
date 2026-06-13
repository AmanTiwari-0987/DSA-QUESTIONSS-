'''
WEEK - 2 
DAY 4 QUESTION 1 
REVERSE WORDS IN A STRING 3 
'''
class Solution(object):
    def reverseWords(self, s):
        words = s.split()

        result = []

        for word in words:
            result.append(word[::-1])
        
        return " ".join(result)
        
      
       
        