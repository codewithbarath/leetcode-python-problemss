class Solution(object):
    def findTheDifference(self, s, t):
        for ss in s:
            if(ss not in t):
                print(ss)
               
            
c1=Solution()
print(c1.findTheDifference("abcd","abcde"))