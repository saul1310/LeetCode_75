class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return float(nums[0])
        
        if len(nums) < k:
            return sum(nums) / len(nums)
        
        # Initial sum of the first 'k' elements
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        # Sliding window to find the maximum sum of subarrays of length 'k'
        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)
        
        # Calculate and return the maximum average
        return max_sum / k
