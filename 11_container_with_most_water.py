def maxArea(self, height: List[int]) -> int:
       i=0
       j=len(height)-1
       maxarea=0
       area=0
       while i < j:
           l= j - i
           h=min(height[i], height[j])
           area= l * h

           maxarea=max(maxarea,area)

           if height[i] <= height[j]:
               i +=1
           elif height[i] > height[j]:
                j -=1

       return maxarea