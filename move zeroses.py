class Solution(object):
    def moveZeroes(self, nums):
        none_zero_list=[]
        xero_list=[]
        b=sorted(nums)
        for n in nums:
            if n!=0:
                none_zero_list.append(n)
            else:
                xero_list.append(n)

        
                y= none_zero_list.extend(xero_list)
            return y



c1=Solution()
print(c1.moveZeroes([0,1,0,3,12]))


       



c1=Solution()
print(c1.moveZeroes([0,1,0,3,12]))