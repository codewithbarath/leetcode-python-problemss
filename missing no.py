class Solution(object):
    def missingNumber(self, nums):
        for i in range(len(nums)+1):
            if i not in nums:
                return i



c1=Solution()
print(c1.missingNumber([0,1]))



