  def longestOnes(self, nums: List[int], k: int) -> int:
        mx,l =0,0
        for r,n in enumerate(nums):
            k -= 1 - n
            if k < 0:
                k += 1 -nums[l] 
                l +=1
            mx =max(mx, r- l +1)
        return m
