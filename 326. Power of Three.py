class Solution(object):
    def isPowerOfThree(self, n):
        new=[]
        for i in range(1,n+1):
            if (i%3==0):
                new.append(i)
        if n in new:
            return True 
        return False 

c1=Solution()
print(c1.isPowerOfThree(-1))