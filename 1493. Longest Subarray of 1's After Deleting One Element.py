class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums) -1
        L,R = 0,0
        zero_index = -1
        cursum= 0

        while R < len(nums):
            if nums[R] == 0:
                if zero_index != -1:
                    L = zero_index +1
                zero_index = R
            cursum=max(cursum,R-L)
            R +=1
        return cursum
                
        
