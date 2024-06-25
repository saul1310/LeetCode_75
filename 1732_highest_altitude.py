def largestAltitude(self, gain: List[int]) -> int:
        current=0
        maxalt=0
        i=0
        while i < len(gain):
            current += gain[i]
            maxalt=max(maxalt,current)
            i +=1
        return maxalt