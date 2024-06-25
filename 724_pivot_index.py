def pivotIndex(self, nums: List[int]) -> int:
        i =0
        l=[]
        r=[]
        if len(nums) == 0:
            return -1
        else:

            while i < len(nums):
                if i > 0:
                    l=nums[:i] 
                else:
                    l ==[0]
                if i != len(nums)-1:
                    r=nums[i+1:]
                else:
                    r =[0]
                

                if sum(l) == sum(r):
                    return (i)
                
                
                    
            
                i +=1
            return -1