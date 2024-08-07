class Solution:
    def compress(self, chars: List[str]) -> int:
        
        i = 0
        s = ""
        while i < len(chars):
            count = 1
            letter = chars[i]
            i += 1
            
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            if count > 1:
                s += letter + str(count)
            else:
                s += letter

    
        chars.clear()  
        for char in s:
            chars.append(char)
        
        return len(chars)


        
