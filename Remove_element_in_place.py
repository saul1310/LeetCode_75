class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #original_length = len(nums)
        nums[:] = [num for num in nums if num != val]