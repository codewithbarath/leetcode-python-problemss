class Solution(object):
    def majorityElement(self, nums):
        unique_numbers = set(nums)  # Get unique numbers
        max_count = 0
        max_element = None
        
        for num in unique_numbers:
            count = nums.count(num)
            if count > max_count:
                max_count = count
                max_element = num
        
        return max_element  # Return the number with the highest count

# Example usage:
c1 = Solution()
result = c1.majorityElement([2, 2, 2, 1, 1, 1, 2, 2])
print(result)  # Output: 2
