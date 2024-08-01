class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
       inf = 10 ** 20

        s1,s2 = inf, inf 

        for x in nums:
            if x > s2:
                return True

            if x > s1:
                s2 = min (s2,x)

            s1 = min(s1,x)
        return False
