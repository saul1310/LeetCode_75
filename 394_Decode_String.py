class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
                continue
            innerstring = ""
            while stack and stack[-1] != '[':
                innerstring = stack.pop() +  innerstring
            stack.pop()

            multiplier = ""
            while stack and stack[-1].isdigit():
                multiplier = stack.pop() + multiplier
            stack.append(int(multiplier) * innerstring)
        return "".join(stack)
