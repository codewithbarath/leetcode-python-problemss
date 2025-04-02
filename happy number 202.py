class Solution(object):
    def isHappy(self, n):
        seen = set()
        
        while n != 1 and n not in seen:
            seen.add(n)
            
            digits = str(n)  
            squared_sum = 0

