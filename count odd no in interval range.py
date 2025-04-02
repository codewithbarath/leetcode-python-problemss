class Solution(object):
    def countOdds(self, low, high):
        new=[]
        for i in range(low,high+1):
            if(i%2!=0):
                new.append(i)
        return len(new)
c1=Solution()
print(c1.countOdds(3,7))
 