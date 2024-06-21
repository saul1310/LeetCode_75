def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=[]
        l2=[]
        answer=[]
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        l1=[i for i in nums1 if i not in nums2 ]
        l2=[j for j in nums2 if j not in nums1 ]
        answer.append(l1)
        answer.append(l2)
        return(answer)

        