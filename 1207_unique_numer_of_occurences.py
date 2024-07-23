class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hash={}
        for i in range(len(arr)):
            if arr[i] not in hash:
                hash[arr[i]] = 1
            else:
                hash[arr[i]] = hash[arr[i]] +1

        return len(set(hash.values())) == len(hash.values())
        
        
